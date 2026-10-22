#!/usr/bin/env python3
"""Check that each published Core solution page covers its current source bank."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = Path(__file__).resolve().parent
ASSESSMENTS = ROOT / "core_assessments"
COUNTING = ROOT / "counting_problem_sections"


def expected_standard() -> set[str]:
    return {f"{section}.{number}" for section in "ABCDE" for number in range(1, 6)}


def source_problem_ids(path: Path) -> set[str]:
    text = path.read_text()
    marked = re.findall(r"\\problem\{([A-E]\.\d+)\}", text)
    if not marked:
        marked = re.findall(r"\\subsection\*\{([A-E]\.\d+)\}", text)
    return set(marked)


def solution_ids(path: Path, *, arguments: bool = False) -> list[str]:
    width = r"\d+\.\d{2}" if arguments else r"\d+"
    return re.findall(rf"(?m)^####? ([A-E]\.{width})(?:\s|$)", path.read_text())


def report_alignment(name: str, expected: set[str], found: list[str]) -> bool:
    counts = Counter(found)
    duplicates = sorted(label for label, count in counts.items() if count > 1)
    missing = sorted(expected - set(found))
    extras = sorted(set(found) - expected)
    okay = not duplicates and not missing and not extras
    status = "PASS" if okay else "FAIL"
    print(f"{status:4} {name:12} expected={len(expected):3} found={len(found):3}")
    if duplicates:
        print(f"     duplicate headings: {', '.join(duplicates)}")
    if missing:
        print(f"     missing solutions:  {', '.join(missing)}")
    if extras:
        print(f"     unexpected IDs:     {', '.join(extras)}")
    return okay


def check_page_basics(path: Path) -> bool:
    text = path.read_text()
    required = ("publish: true", "Full-credit and grader guidance", "decisive check")
    missing = [phrase for phrase in required if phrase.lower() not in text.lower()]
    if missing:
        print(f"FAIL {path.stem:12} missing page guidance: {', '.join(missing)}")
        return False
    return True


def main() -> int:
    okay = True
    standard_sources = {
        "Logic": ASSESSMENTS / "logic_assessment.tex",
        "Sets": ASSESSMENTS / "sets_assessment.tex",
        "Proofs": ASSESSMENTS / "proofs_assessment.tex",
        "Divisibility": ASSESSMENTS / "divisibility_assessment.tex",
    }
    for name, source in standard_sources.items():
        expected = source_problem_ids(source)
        page = SOLUTIONS / f"2300_{name}_Solutions.md"
        okay &= expected == expected_standard()
        okay &= report_alignment(name, expected, solution_ids(page))
        okay &= check_page_basics(page)

    counting_items = 0
    for path in COUNTING.glob("*.tex"):
        counting_items += len(re.findall(r"(?m)^\s*\\item\s", path.read_text()))
    counting_expected = expected_standard()
    if counting_items != len(counting_expected):
        print(f"FAIL Counting source has {counting_items} items, expected 25")
        okay = False
    counting_page = SOLUTIONS / "2300_Counting_Solutions.md"
    okay &= report_alignment("Counting", counting_expected, solution_ids(counting_page))
    okay &= check_page_basics(counting_page)

    arguments_source = (ASSESSMENTS / "arguments_extended_practice.tex").read_text()
    arguments_expected = set(re.findall(r"\\bankitem\{([A-E]\.\d\.\d{2})\}", arguments_source))
    arguments_page = SOLUTIONS / "2300_Arguments_Solutions.md"
    arguments_text = arguments_page.read_text()
    okay &= report_alignment(
        "Arguments", arguments_expected, solution_ids(arguments_page, arguments=True)
    )
    okay &= check_page_basics(arguments_page)
    argument_blocks = {
        match.group(1): match.group(2).strip()
        for match in re.finditer(
            r"(?ms)^#### ([A-E]\.\d\.\d{2})\s*\n(.*?)(?=^#### [A-E]\.\d\.\d{2}\s*$|\Z)",
            arguments_text,
        )
    }
    mc_expected = {
        label
        for label in arguments_expected
        if label[0] in "BCD" or label.startswith("E.2.")
    }
    open_expected = arguments_expected - mc_expected
    missing_answer_callouts = sorted(
        label for label in mc_expected if "[!NOTE]- Answer:" not in argument_blocks.get(label, "")
    )
    missing_solution_callouts = sorted(
        label for label in open_expected if "[!NOTE]- Solution" not in argument_blocks.get(label, "")
    )
    undersized = sorted(label for label, body in argument_blocks.items() if len(body) < 80)
    if missing_answer_callouts or missing_solution_callouts or undersized:
        print("FAIL Arguments has incomplete solution blocks")
        if missing_answer_callouts:
            print(f"     missing answer callouts: {', '.join(missing_answer_callouts)}")
        if missing_solution_callouts:
            print(f"     missing solution callouts: {', '.join(missing_solution_callouts)}")
        if undersized:
            print(f"     unusually short blocks: {', '.join(undersized)}")
        okay = False
    else:
        print(
            f"PASS Arguments    {len(mc_expected)} keyed choice solutions and "
            f"{len(open_expected)} worked responses are nonempty"
        )

    induction_expected = {
        f"{section}.{number}" for section in "ABC" for number in range(1, 6)
    }
    induction_page = SOLUTIONS / "2300_Induction_Solutions.md"
    induction_text = induction_page.read_text()
    okay &= report_alignment("Induction", induction_expected, solution_ids(induction_page))
    okay &= check_page_basics(induction_page)
    stale_phrases = ("one from each section A–E", "exactly five problems")
    stale = [phrase for phrase in stale_phrases if phrase in induction_text]
    if stale:
        print(f"FAIL Induction retains stale format text: {', '.join(stale)}")
        okay = False

    print("\nAll solution pages align with their current banks." if okay else "\nAlignment audit failed.")
    return 0 if okay else 1


if __name__ == "__main__":
    sys.exit(main())
