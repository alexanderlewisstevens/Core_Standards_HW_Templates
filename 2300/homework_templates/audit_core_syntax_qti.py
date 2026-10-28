#!/usr/bin/env python3
"""Audit the seven Canvas QTI packages built from the Core syntax bank."""

from __future__ import annotations

import argparse
import html
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

from generate_core_syntax_bank import CORES
from generate_core_syntax_qti import (
    CHOICES, POINTS_PER_ITEM, ReusedIdentifiers, deterministic_identifiers, saved_identifiers,
)


QTI = {"q": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2"}
EXPECTED_CHOICES = {choice_id: label for choice_id, label in CHOICES}


def text_of(parent: ET.Element, path: str) -> str:
    node = parent.find(path, QTI)
    if node is None or node.text is None:
        return ""
    return html.unescape(node.text).strip()


def metadata(item: ET.Element) -> dict[str, str]:
    result: dict[str, str] = {}
    for field in item.findall("./q:itemmetadata/q:qtimetadata/q:qtimetadatafield", QTI):
        label = text_of(field, "q:fieldlabel")
        value = text_of(field, "q:fieldentry")
        result[label] = value
    return result


def audit_archive(path: Path, core_name: str,
                  expected_ids: ReusedIdentifiers | None = None) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(path) as bundle:
        members = sorted(bundle.namelist())
        if members != ["assessment.xml", "imsmanifest.xml"]:
            errors.append(f"unexpected archive members: {members}")
        assessment_bytes = bundle.read("assessment.xml")
        manifest_bytes = bundle.read("imsmanifest.xml")

    return errors + audit_documents(assessment_bytes, manifest_bytes, core_name, expected_ids)


def audit_documents(assessment_bytes: bytes, manifest_bytes: bytes, core_name: str,
                    expected_ids: ReusedIdentifiers | None = None) -> list[str]:
    errors: list[str] = []
    if expected_ids is None:
        expected_ids = saved_identifiers()[core_name]

    try:
        root = ET.fromstring(assessment_bytes)
        manifest = ET.fromstring(manifest_bytes)
    except ET.ParseError as exc:
        return [f"malformed XML: {exc}"]

    assessment = root.find("q:assessment", QTI)
    if assessment is None:
        return ["missing assessment"]
    expected_title = f"Core Practice — {core_name} Syntax and Definitions"
    if assessment.get("title") != expected_title:
        errors.append(f"title is {assessment.get('title')!r}, expected {expected_title!r}")

    assessment_metadata: dict[str, str] = {}
    for field in assessment.findall("./q:qtimetadata/q:qtimetadatafield", QTI):
        label = text_of(field, "q:fieldlabel")
        value = text_of(field, "q:fieldentry")
        assessment_metadata[label] = value
    if assessment_metadata.get("cc_maxattempts") != "-1":
        errors.append(
            "quiz is not configured for unlimited attempts "
            f"(cc_maxattempts={assessment_metadata.get('cc_maxattempts')!r})"
        )

    items = assessment.findall("./q:section/q:item", QTI)
    if len(items) != 60:
        errors.append(f"contains {len(items)} items, expected 60")
    resources = [node for node in manifest.iter() if node.tag.rsplit("}", 1)[-1] == "resource"]
    if assessment.get("ident") != expected_ids.assessment:
        errors.append("assessment identifier differs from the saved Canvas identity")
    if expected_ids.resource not in {node.get("identifier") for node in resources}:
        errors.append("resource identifier differs from the saved Canvas identity")

    answers: Counter[str] = Counter()
    titles: list[str] = []
    total_points = 0.0
    identifiers = [assessment.get("ident", "")]
    identifiers.extend(
        node.get("identifier", "") for node in manifest.iter()
        if node.tag.rsplit("}", 1)[-1] == "resource"
    )
    for number, item in enumerate(items, start=1):
        title = item.get("title", "")
        titles.append(title)
        meta = metadata(item)
        item_id = item.get("ident", "")
        response = item.find("./q:presentation/q:response_lid", QTI)
        response_id = response.get("ident", "") if response is not None else ""
        feedback_node = item.find("./q:itemfeedback", QTI)
        feedback_id = feedback_node.get("ident", "") if feedback_node is not None else ""
        identifiers.extend((item_id, response_id, feedback_id))
        if number <= len(expected_ids.items) and (item_id, response_id, feedback_id) != (
            expected_ids.items[number-1], expected_ids.responses[number-1], expected_ids.feedback[number-1]
        ):
            errors.append(f"item {number}: identifiers differ from the saved Canvas identity")
        if meta.get("assessment_question_identifierref") != item_id:
            errors.append(f"item {number}: question identifier reference does not match")
        if any(node.get("respident") != response_id for node in item.findall(".//q:varequal", QTI)):
            errors.append(f"item {number}: answer condition references the wrong response")
        if any(node.get("linkrefid") != feedback_id for node in item.findall(".//q:displayfeedback", QTI)):
            errors.append(f"item {number}: feedback reference does not match")
        if meta.get("question_type") != "multiple_choice_question":
            errors.append(f"item {number}: wrong question type {meta.get('question_type')!r}")
        if meta.get("points_possible") != POINTS_PER_ITEM:
            errors.append(f"item {number}: wrong points {meta.get('points_possible')!r}")
        try:
            total_points += float(meta.get("points_possible", "nan"))
        except ValueError:
            errors.append(f"item {number}: nonnumeric points")

        labels = item.findall("./q:presentation/q:response_lid/q:render_choice/q:response_label", QTI)
        rendered_choices = {
            label.get("ident", ""): re.sub(
                r"<[^>]+>", "", text_of(label, "q:material/q:mattext")
            ).strip()
            for label in labels
        }
        if rendered_choices != EXPECTED_CHOICES:
            errors.append(f"item {number}: choices are {rendered_choices!r}")

        correct = item.find(
            "./q:resprocessing/q:respcondition/q:conditionvar/q:varequal", QTI
        )
        if correct is None or (correct.text or "").strip() not in EXPECTED_CHOICES:
            errors.append(f"item {number}: missing or invalid correct answer")
            continue
        answer = (correct.text or "").strip()
        answers[answer] += 1

        prompt = text_of(item, "q:presentation/q:material/q:mattext")
        feedback = text_of(item, "q:itemfeedback/q:flow_mat/q:material/q:mattext")
        if "Judge the statement as written" not in prompt:
            errors.append(f"item {number}: missing common directions")
        if f"Correct answer: {EXPECTED_CHOICES[answer]}." not in feedback:
            errors.append(f"item {number}: feedback does not state the key")
        if answer == "N" and "One minimal repair:" not in feedback:
            errors.append(f"item {number}: incoherent statement lacks a minimal repair")
        if "$" in prompt or re.search(r"\\[A-Za-z]+", prompt):
            errors.append(f"item {number}: unconverted TeX remains in prompt")

    if len(titles) != len(set(titles)):
        errors.append("item titles are not unique")
    if any(not identifier for identifier in identifiers) or len(identifiers) != len(set(identifiers)):
        errors.append("assessment/resource/item/response/feedback identifiers are missing or repeated")
    if answers != Counter({"T": 20, "F": 20, "N": 20}):
        errors.append(f"answer distribution is {dict(answers)}, expected 20/20/20")
    if abs(total_points - 3.0) > 1e-9:
        errors.append(f"quiz totals {total_points:g} points, expected 3")
    return errors


def audit_combined(path: Path, expected: dict[str, ReusedIdentifiers] | None = None) -> list[str]:
    """Validate all seven independent QTI resources in the one-upload package."""
    expected = expected if expected is not None else saved_identifiers()
    errors: list[str] = []
    expected_paths = {f"{core.name}/assessment.xml" for core in CORES}
    with zipfile.ZipFile(path) as bundle:
        if set(bundle.namelist()) != {"imsmanifest.xml", *expected_paths}:
            return ["combined archive does not contain exactly one manifest and seven assessment paths"]
        manifest_bytes = bundle.read("imsmanifest.xml")
        try:
            manifest = ET.fromstring(manifest_bytes)
        except ET.ParseError as exc:
            return [f"malformed combined manifest: {exc}"]
        resources = [node for node in manifest.iter() if node.tag.rsplit("}", 1)[-1] == "resource"]
        if len(resources) != 7:
            errors.append(f"combined manifest contains {len(resources)} resources, expected 7")
        resource_paths = {node.get("identifier"): node.get("href") for node in resources}
        for core in CORES:
            href = f"{core.name}/assessment.xml"
            if resource_paths.get(expected[core.name].resource) != href:
                errors.append(f"{core.name}: original resource identifier does not point to {href}")
            resource = next((node for node in resources if node.get("href") == href), None)
            files = [] if resource is None else [node.get("href") for node in resource
                                                if node.tag.rsplit("}", 1)[-1] == "file"]
            if resource is None or resource.get("type") != "imsqti_xmlv1p2" or files != [href]:
                errors.append(f"{core.name}: incorrect resource type or file path")
            errors.extend(f"{core.name}: {error}" for error in audit_documents(
                bundle.read(href), manifest_bytes, core.name, expected[core.name],
            ))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "qti_dir",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "output" / "qti",
    )
    parser.add_argument("--new-identifiers", action="store_true",
                        help="Audit clean-course UUID5 identifiers instead of saved course 213452 IDs.")
    args = parser.parse_args()
    expected = ({core.name: deterministic_identifiers(core.name) for core in CORES}
                if args.new_identifiers else saved_identifiers())

    failed = False
    for core in CORES:
        path = args.qti_dir / f"Core_{core.name}_Syntax_Practice_Canvas_QTI.zip"
        if not path.exists():
            print(f"FAIL {core.name}: missing {path}")
            failed = True
            continue
        errors = audit_archive(path, core.name, expected[core.name])
        if errors:
            failed = True
            print(f"FAIL {core.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {core.name}: 60 items; T/F/N = 20/20/20; 3 points")
    combined = args.qti_dir / "Core_All_Syntax_Practice_Canvas_QTI.zip"
    if not combined.exists():
        print(f"FAIL Combined: missing {combined}")
        failed = True
    elif errors := audit_combined(combined, expected):
        print("FAIL Combined")
        for error in errors:
            print(f"  - {error}")
        failed = True
    else:
        print("PASS Combined: 7 original resource paths/IDs; 420 keyed items; 3 points per quiz")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
