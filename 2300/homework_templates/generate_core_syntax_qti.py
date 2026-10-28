#!/usr/bin/env python3
"""Build one Canvas QTI practice quiz for each COMP 2300 Core.

The question text, correct answers, explanations, and minimal repairs come
directly from ``generate_core_syntax_bank.py`` so the Canvas quizzes and the
printable T/F/N bank cannot silently drift apart.

Each quiz contains all sixty items for one Core (twenty concept families,
three forms).  The Canvas import is intentionally left unpublished; course
placement, dates, and publication are instructor decisions made in Canvas.

By default, preserve the durable imported identities for course 213452. Use
``--new-identifiers`` only for a clean-course import. Every build also creates
one combined package containing all seven independent assessments.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import uuid
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree

from generate_core_syntax_bank import CORES, CORE_NOTATION_GUIDES, form_items


CHOICES = (
    ("T", "True"),
    ("F", "False"),
    ("N", "Not a truth-evaluable proposition as written"),
)

# Sixty short items at 0.05 point each make the completed Canvas practice worth
# three points: enough to count as Participation and Practice, but far less than
# the substantive Core result.  Canvas derives a Classic Quiz's total from the
# question points, so keep this value synchronized with the audit script.
POINTS_PER_ITEM = "0.05"

# Keep identifiers stable across content revisions so Canvas can overwrite an
# earlier import instead of creating a second quiz. Never change this namespace.
IDENTIFIER_NAMESPACE = uuid.UUID("99303fb7-28c4-5319-a478-e49b231e54af")
DEFAULT_IDENTIFIER_FILE = Path(__file__).with_name("core_syntax_canvas_identifiers.json")


def stable_identifier(kind: str, core_name: str, item_key: str = "") -> str:
    name = f"COMP2300/core-syntax/{core_name}/{kind}/{item_key}"
    return f"{kind}_{uuid.uuid5(IDENTIFIER_NAMESPACE, name).hex}"


@dataclass(frozen=True)
class ReusedIdentifiers:
    assessment: str
    resource: str
    items: tuple[str, ...]
    responses: tuple[str, ...]
    feedback: tuple[str, ...]


def deterministic_identifiers(core_name: str) -> ReusedIdentifiers:
    keys = [f"{form}.{number}" for form in "ABC" for number in range(1, 21)]
    return ReusedIdentifiers(
        stable_identifier("assessment", core_name), stable_identifier("resource", core_name),
        *(tuple(stable_identifier(kind, core_name, key) for key in keys)
          for kind in ("question", "response", "feedback")),
    )


def validate_identifiers(identifiers: ReusedIdentifiers, source: str) -> None:
    if any(len(values) != 60 for values in (identifiers.items, identifiers.responses, identifiers.feedback)):
        raise ValueError(f"{source}: expected 60 item, response and feedback IDs")
    all_ids = (identifiers.assessment, identifiers.resource, *identifiers.items,
               *identifiers.responses, *identifiers.feedback)
    if any(not isinstance(value, str) or not value for value in all_ids) or len(all_ids) != len(set(all_ids)):
        raise ValueError(f"{source}: empty, invalid or repeated imported identifiers")


def saved_identifiers(path: Path = DEFAULT_IDENTIFIER_FILE) -> dict[str, ReusedIdentifiers]:
    """Load the durable identity map for the seven existing course 213452 quizzes."""
    data = json.loads(path.read_text())
    if data.get("schema_version") != 1 or data.get("canvas_course_id") != 213452:
        raise ValueError(f"{path}: unrecognized identifier-map schema or course")
    if set(data.get("cores", {})) != {core.name for core in CORES}:
        raise ValueError(f"{path}: identifier map must cover exactly the seven current cores")
    result: dict[str, ReusedIdentifiers] = {}
    for name, core in data["cores"].items():
        identifiers = ReusedIdentifiers(
            core["assessment"], core["resource"], tuple(core["items"]),
            tuple(core["responses"]), tuple(core["feedback"]),
        )
        validate_identifiers(identifiers, f"{path}: {name}")
        result[name] = identifiers
    return result


def reused_identifiers(directory: Path) -> dict[str, ReusedIdentifiers]:
    """Read the IDs of previously imported packages, preserving item order.

    This is a migration bridge for packages created before stable UUIDs were
    introduced. The original downloaded ZIPs need not be modified; the saved
    JSON map is used by default for the existing course.
    """
    if not directory.is_dir():
        raise ValueError(f"Identifier source is not a directory: {directory}")
    result: dict[str, ReusedIdentifiers] = {}
    for core in CORES:
        filename = f"Core_{core.name}_Syntax_Practice_Canvas_QTI.zip"
        path = directory / filename
        if not path.is_file():
            raise ValueError(f"Missing original package for {core.name}: {path}")
        with zipfile.ZipFile(path) as bundle:
            assessment_root = ElementTree.fromstring(bundle.read("assessment.xml"))
            manifest_root = ElementTree.fromstring(bundle.read("imsmanifest.xml"))
        assessment = next(
            (node for node in assessment_root.iter() if node.tag.rsplit("}", 1)[-1] == "assessment"),
            None,
        )
        resource = next(
            (node for node in manifest_root.iter()
             if node.tag.rsplit("}", 1)[-1] == "resource" and node.get("href") == "assessment.xml"),
            None,
        )
        if assessment is None or resource is None:
            raise ValueError(f"{path}: missing assessment or assessment resource")
        title = assessment.get("title", "")
        if not re.search(rf"\b{re.escape(core.name)}\b", title, re.IGNORECASE):
            raise ValueError(f"{path}: assessment title does not match {core.name}: {title!r}")
        items = [node for node in assessment.iter() if node.tag.rsplit("}", 1)[-1] == "item"]
        if len(items) != 60:
            raise ValueError(f"{path}: expected 60 original item IDs, found {len(items)}")

        def child_id(item: ElementTree.Element, kind: str) -> str:
            node = next((node for node in item.iter() if node.tag.rsplit("}", 1)[-1] == kind), None)
            return node.get("ident", "") if node is not None else ""

        identifiers = ReusedIdentifiers(
            assessment.get("ident", ""), resource.get("identifier", ""),
            tuple(item.get("ident", "") for item in items),
            tuple(child_id(item, "response_lid") for item in items),
            tuple(child_id(item, "itemfeedback") for item in items),
        )
        validate_identifiers(identifiers, str(path))
        result[core.name] = identifiers
    return result


MATH_SYMBOLS = {
    "leftrightarrow": "↔", "Rightarrow": "⇒", "therefore": "∴",
    "because": "∵", "subseteq": "⊆", "setminus": "∖", "varnothing": "∅",
    "models": "⊨", "equiv": "≡", "forall": "∀", "exists": "∃",
    "nmid": "∤", "mid": "∣", "land": "∧", "lor": "∨", "neg": "¬",
    "to": "→", "in": "∈", "cup": "∪", "cap": "∩", "le": "≤",
    "ge": "≥", "ne": "≠", "cdot": "·", "times": "×", "bot": "⊥",
    "sum": "∑", "ldots": "…", "cdots": "…", "Gamma": "Γ",
    "Omega": "Ω", "Box": "□", "uparrow": "↑", "gcd": "gcd", "Pr": "Pr",
    "bmod": " mod ", "iff": " iff ",
}
BLACKBOARD_SYMBOLS = {"Z": "ℤ", "N": "ℕ", "Q": "ℚ", "R": "ℝ", "E": "𝔼"}
NEGATED_SYMBOLS = {"∈": "∉", "≡": "≢", "∣": "∤", "⊆": "⊈", "=": "≠"}


class _MathRenderer:
    r"""Read TeX tokens instead of replacing prefixes or dropping commands.

    A single unbraced token is an argument in TeX: \frac12 and \binom nr
    are not the numbers 12 and nr. Unknown commands fail the build instead
    of silently changing a question's meaning. Intentionally malformed math
    (missing operands, literal set braces, blank boxes) stays malformed.
    """

    def __init__(self, source: str, *, html_output: bool = False):
        self.source = source
        self.position = 0
        self.html_output = html_output

    def literal(self, value: str) -> str:
        return html.escape(value, quote=False) if self.html_output else value

    def argument(self) -> str:
        while self.position < len(self.source) and self.source[self.position].isspace():
            self.position += 1
        if self.position == len(self.source) or self.source[self.position] == "}":
            raise ValueError(f"Missing TeX argument in {self.source!r}")
        return self.atom()

    def atom(self) -> str:
        character = self.source[self.position]
        self.position += 1
        if character == "{":
            return self.render(group=True)
        if character != "\\":
            return self.literal(character)
        match = re.match(r"[A-Za-z]+|.", self.source[self.position:])
        if match is None:
            raise ValueError(f"Unfinished TeX command in {self.source!r}")
        command = match.group()
        self.position += len(command)
        if command in MATH_SYMBOLS:
            return self.literal(MATH_SYMBOLS[command])
        if command in {",", ";", " ", "!"}:
            return "" if command == "!" else " "
        if command in {"{", "}", "%"}:
            return self.literal(command)
        if command in {"frac", "binom"}:
            first, second = self.argument().strip(), self.argument().strip()
            return (f"({first})/({second})" if command == "frac"
                    else f"C({first}, {second})")
        if command == "sqrt":
            return f"√({self.argument()})"
        if command == "pmod":
            return f" (mod {self.argument()})"
        if command == "operatorname":
            return self.argument()
        if command in {"mathbb", "mathcal"}:
            argument = self.argument()
            symbols = BLACKBOARD_SYMBOLS if command == "mathbb" else {"P": "𝒫"}
            if argument not in symbols:
                raise ValueError(f"Unsupported \\{command} argument {argument!r}")
            return self.literal(symbols[argument])
        if command == "not":
            relation = self.argument()
            if relation not in NEGATED_SYMBOLS:
                raise ValueError(f"Unsupported negated relation {relation!r}")
            return self.literal(NEGATED_SYMBOLS[relation])
        raise ValueError(f"Unsupported TeX command \\{command} in {self.source!r}")

    def render(self, *, group: bool = False) -> str:
        output: list[str] = []
        while self.position < len(self.source):
            character = self.source[self.position]
            if character == "}":
                if not group:
                    raise ValueError(f"Unmatched TeX group in {self.source!r}")
                self.position += 1
                return "".join(output)
            if character in "_^":
                self.position += 1
                argument = self.argument()
                if self.html_output:
                    tag = "sub" if character == "_" else "sup"
                    output.append(f"<{tag}>{argument}</{tag}>")
                else:
                    # a_(n+1) is not a_n + 1; 2^(k+1) is not 2^k + 1.
                    output.append(character + (argument if len(argument) == 1 else f"({argument})"))
            else:
                output.append(self.atom())
        if group:
            raise ValueError(f"Unclosed TeX group in {self.source!r}")
        return "".join(output)


def math_to_unicode(source: str) -> str:
    """Render the bank's TeX as unambiguous portable Unicode plain text."""
    return re.sub(r"\s+", " ", _MathRenderer(source).render()).strip()


def math_to_html(source: str) -> str:
    """Use the same token parser, with safe HTML for subscripts/superscripts."""
    return re.sub(r"\s+", " ", _MathRenderer(source, html_output=True).render()).strip()


def tex_fragment_to_html(source: str) -> str:
    """Convert emphasis plus inline TeX into Canvas-safe HTML and Unicode."""

    # The source uses only simple, non-nested \emph groups.  Convert those
    # before splitting on TeX math delimiters.
    source = re.sub(
        r"\\emph\{([^{}]*)\}",
        lambda match: "\x00EMOPEN\x00" + match.group(1) + "\x00EMCLOSE\x00",
        source,
    )
    parts = source.split("$")
    if len(parts) % 2 == 0:
        raise ValueError(f"Unbalanced inline-math delimiters in {source!r}")
    rendered: list[str] = []
    for index, part in enumerate(parts):
        if index % 2:
            rendered.append(math_to_html(part))
        else:
            rendered.append(html.escape(part, quote=False))
    result = (
        "".join(rendered)
        .replace("\x00EMOPEN\x00", "<em>")
        .replace("\x00EMCLOSE\x00", "</em>")
    )
    if re.search(r"\\[A-Za-z]+", result):
        raise ValueError(f"Unconverted prose command in {source!r}")
    return result


def qti_html(fragment: str) -> str:
    """Escape an HTML fragment for the body of a QTI mattext element."""

    return html.escape(fragment, quote=True)


def feedback_html(answer: str, explanation: str, repair: str) -> str:
    label = dict(CHOICES)[answer]
    lines = [f"<p><strong>Correct answer: {label}.</strong></p>"]
    lines.append(f"<p>{tex_fragment_to_html(explanation)}</p>")
    if repair:
        lines.append(
            "<p><strong>One minimal repair:</strong> "
            f"{tex_fragment_to_html(repair)}</p>"
        )
    return "".join(lines)


def qti_item(
    *,
    core_name: str,
    form_label: str,
    item_number: int,
    category: str,
    statement: str,
    answer: str,
    explanation: str,
    repair: str,
    identifiers: tuple[str, str, str] | None = None,
) -> str:
    item_key = f"{form_label}.{item_number}"
    item_id, response_id, feedback_id = identifiers or tuple(
        stable_identifier(kind, core_name, item_key)
        for kind in ("question", "response", "feedback")
    )
    item_id, response_id, feedback_id = (
        html.escape(value, quote=True) for value in (item_id, response_id, feedback_id)
    )
    title = html.escape(f"{category} — Form {form_label}, Item {item_number}", quote=True)
    prompt = qti_html(
        "<p><strong>Judge the statement as written.</strong></p>"
        f"<p>{tex_fragment_to_html(statement)}</p>"
    )
    choices = "\n".join(
        f'''          <response_label ident="{choice_id}">
            <material><mattext texttype="text/html">{qti_html(f"<p>{label}</p>")}</mattext></material>
          </response_label>'''
        for choice_id, label in CHOICES
    )
    feedback = qti_html(feedback_html(answer, explanation, repair))
    return f'''    <item ident="{item_id}" title="{title}">
      <itemmetadata>
        <qtimetadata>
          <qtimetadatafield><fieldlabel>question_type</fieldlabel><fieldentry>multiple_choice_question</fieldentry></qtimetadatafield>
          <qtimetadatafield><fieldlabel>points_possible</fieldlabel><fieldentry>{POINTS_PER_ITEM}</fieldentry></qtimetadatafield>
          <qtimetadatafield><fieldlabel>assessment_question_identifierref</fieldlabel><fieldentry>{item_id}</fieldentry></qtimetadatafield>
          <qtimetadatafield><fieldlabel>question_bank_name</fieldlabel><fieldentry>Core {html.escape(core_name)}</fieldentry></qtimetadatafield>
        </qtimetadata>
      </itemmetadata>
      <presentation>
        <material><mattext texttype="text/html">{prompt}</mattext></material>
        <response_lid ident="{response_id}" rcardinality="Single">
          <render_choice shuffle="No">
{choices}
          </render_choice>
        </response_lid>
      </presentation>
      <resprocessing>
        <outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>
        <respcondition continue="No">
          <conditionvar><varequal respident="{response_id}">{answer}</varequal></conditionvar>
          <setvar action="Set" varname="SCORE">100</setvar>
          <displayfeedback feedbacktype="Response" linkrefid="{feedback_id}"/>
        </respcondition>
        <respcondition continue="No">
          <conditionvar><other/></conditionvar>
          <setvar action="Set" varname="SCORE">0</setvar>
          <displayfeedback feedbacktype="Response" linkrefid="{feedback_id}"/>
        </respcondition>
      </resprocessing>
      <itemfeedback ident="{feedback_id}">
        <flow_mat><material><mattext texttype="text/html">{feedback}</mattext></material></flow_mat>
      </itemfeedback>
    </item>'''


def assessment_xml(core, assessment_id: str, reused: ReusedIdentifiers | None = None) -> str:
    title = f"Core Practice — {core.name} Syntax and Definitions"
    description = (
        "<p><strong>Purpose:</strong> Practice reading the notation and definitions "
        f"used in the {html.escape(core.name)} Core.</p>"
        "<p>This practice contains 60 short statements. Read each statement as "
        "written; the goal is accurate parsing, not fast guessing.</p>"
        "<p>For each item choose <strong>True</strong>, <strong>False</strong>, or "
        "<strong>Not a truth-evaluable proposition as written</strong>. Choose the "
        "third option when the expression is incomplete, ill-formed, undefined, "
        "or has a free variable and therefore does not yet make a proposition.</p>"
        f"<p><strong>Given:</strong> {tex_fragment_to_html(core.context)}</p>"
        f"<p><strong>Notation:</strong> {tex_fragment_to_html(CORE_NOTATION_GUIDES[core.name])}</p>"
    )
    items: list[str] = []
    answers: list[str] = []
    for form_index, form_label in enumerate("ABC"):
        for item_number, (_family_number, family, version) in enumerate(
            form_items(core, form_index), start=1
        ):
            answers.append(version.answer)
            items.append(
                qti_item(
                    core_name=core.name,
                    form_label=form_label,
                    item_number=item_number,
                    category=family.category,
                    statement=version.body,
                    answer=version.answer,
                    explanation=version.explanation,
                    repair=version.repair,
                    identifiers=(reused.items[len(items)], reused.responses[len(items)],
                                 reused.feedback[len(items)]) if reused else None,
                )
            )

    counts = Counter(answers)
    if len(items) != 60 or counts != Counter({"T": 20, "F": 20, "N": 20}):
        raise ValueError(f"{core.name}: expected 60 balanced items, got {counts}")

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2">
  <assessment ident="{html.escape(assessment_id, quote=True)}" title="{html.escape(title, quote=True)}">
    <qtimetadata>
      <qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>-1</fieldentry></qtimetadatafield>
    </qtimetadata>
    <rubric view="All"><material><mattext texttype="text/html">{qti_html(description)}</mattext></material></rubric>
    <section ident="root_section">
{chr(10).join(items)}
    </section>
  </assessment>
</questestinterop>
'''


def manifest_xml(assessment_id: str, resource_id: str) -> str:
    return package_manifest_xml(f"manifest_{assessment_id}", [(resource_id, "assessment.xml")])


def package_manifest_xml(manifest_id: str, resources: list[tuple[str, str]]) -> str:
    resource_elements = "\n".join(
        f'''    <resource identifier="{html.escape(identifier, quote=True)}" type="imsqti_xmlv1p2" href="{html.escape(href, quote=True)}">
      <file href="{html.escape(href, quote=True)}"/>
    </resource>'''
        for identifier, href in resources
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{html.escape(manifest_id, quote=True)}"
  xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
  xmlns:imsqti="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <metadata>
    <schema>IMS Content</schema>
    <schemaversion>1.1.3</schemaversion>
  </metadata>
  <organizations/>
  <resources>
{resource_elements}
  </resources>
</manifest>
'''


def write_package(archive: Path, members: list[tuple[str, str]]) -> None:
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for filename, contents in members:
            member = zipfile.ZipInfo(filename, date_time=(1980, 1, 1, 0, 0, 0))
            member.compress_type = zipfile.ZIP_DEFLATED
            member.external_attr = 0o644 << 16
            bundle.writestr(member, contents)


def build(output_dir: Path, reuse_identifiers_from: Path | None = None, *,
          new_identifiers: bool = False) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    if new_identifiers and reuse_identifiers_from:
        raise ValueError("Cannot combine new identifiers with identifiers from an original import")
    if reuse_identifiers_from:
        originals = reused_identifiers(reuse_identifiers_from)
    elif new_identifiers:
        originals = {core.name: deterministic_identifiers(core.name) for core in CORES}
    else:
        originals = saved_identifiers()
    archives: list[Path] = []
    combined_members: list[tuple[str, str]] = []
    combined_resources: list[tuple[str, str]] = []
    for core in CORES:
        reused = originals.get(core.name)
        assessment_id = reused.assessment if reused else stable_identifier("assessment", core.name)
        resource_id = reused.resource if reused else stable_identifier("resource", core.name)
        assessment = assessment_xml(core, assessment_id, reused)
        # Fail before producing a package if either XML document is malformed.
        ElementTree.fromstring(assessment)
        manifest = manifest_xml(assessment_id, resource_id)
        ElementTree.fromstring(manifest)

        archive = output_dir / f"Core_{core.name}_Syntax_Practice_Canvas_QTI.zip"
        write_package(archive, [("imsmanifest.xml", manifest), ("assessment.xml", assessment)])
        archives.append(archive)
        href = f"{core.name}/assessment.xml"
        combined_members.append((href, assessment))
        combined_resources.append((resource_id, href))
    combined_manifest = package_manifest_xml(
        stable_identifier("manifest", "All"), combined_resources,
    )
    ElementTree.fromstring(combined_manifest)
    combined_archive = output_dir / "Core_All_Syntax_Practice_Canvas_QTI.zip"
    write_package(combined_archive, [("imsmanifest.xml", combined_manifest), *combined_members])
    archives.append(combined_archive)
    return archives


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_dir",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "output" / "qti",
    )
    identity_options = parser.add_mutually_exclusive_group()
    identity_options.add_argument(
        "--reuse-identifiers-from", type=Path, metavar="DIRECTORY",
        help="Reuse IDs from the seven original imported Core_*_Syntax_Practice_Canvas_QTI.zip files.",
    )
    identity_options.add_argument(
        "--new-identifiers", action="store_true",
        help="Use clean deterministic IDs for a new course instead of preserving course 213452 imports.",
    )
    args = parser.parse_args()
    for archive in build(args.output_dir, args.reuse_identifiers_from, new_identifiers=args.new_identifiers):
        print(archive)


if __name__ == "__main__":
    main()
