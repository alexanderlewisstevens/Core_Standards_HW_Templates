#!/usr/bin/env python3
"""Check that each published Core solution page covers its current source bank."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

from insert_full_questions import standard_questions


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = Path(__file__).resolve().parent
ASSESSMENTS = ROOT / "core_assessments"
COUNTING = ROOT / "counting_problem_sections"
ASSETS = SOLUTIONS / "assets"


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


def check_full_questions(path: Path, found: list[str], *, arguments: bool = False) -> bool:
    width = r"\d+\.\d{2}" if arguments else r"\d+"
    text = path.read_text()
    blocks = {
        match.group(1): match.group(2).strip()
        for match in re.finditer(
            rf"(?ms)^###{{1,2}} ([A-E]\.{width})[^\n]*$\n(.*?)"
            rf"(?=^###{{1,2}} [A-E]\.{width}[^\n]*$|\Z)",
            text,
        )
    }
    missing = sorted(
        label
        for label in found
        if "[!QUESTION]- Full question statement" not in blocks.get(label, "")
    )
    too_short = sorted(
        label
        for label in found
        if (question := re.search(
            r"(?ms)> \[!QUESTION\]- Full question statement\n(.*?)(?=\n(?!>)|\Z)",
            blocks.get(label, ""),
        ))
        and len(re.sub(r"(?m)^> ?", "", question.group(1)).strip()) < 25
    )
    leaked_patterns = {
        r"\\end\{document\}": r"\end{document}",
        r"\\vennworkspace\b": r"\vennworkspace",
        r"\\includegraphics\b": r"\includegraphics",
        r"\\hfill\b": r"\hfill",
        r"\\small\b": r"\small",
        r"\\\\item\b": r"\\item",
    }
    question_text = "\n".join(
        question.group(1)
        for block in blocks.values()
        if (question := re.search(
            r"(?ms)> \[!QUESTION\]- Full question statement\n(.*?)(?=\n(?!>)|\Z)",
            block,
        ))
    )
    leaked = [label for pattern, label in leaked_patterns.items() if re.search(pattern, question_text)]
    if missing or too_short or leaked:
        print(f"FAIL {path.stem:12} has incomplete question callouts")
        if missing:
            print(f"     missing callouts: {', '.join(missing)}")
        if too_short:
            print(f"     unusually short prompts: {', '.join(too_short)}")
        if leaked:
            print(f"     leaked TeX layout commands: {', '.join(leaked)}")
        return False
    print(f"PASS {path.stem:12} {len(found)} full question statements")
    return True


def check_divisibility_page_boundary(path: Path) -> bool:
    """Catch next-page reference material accidentally appended to C.5."""
    block = re.search(
        r"(?ms)^### C\.5[^\n]*\n(.*?)(?=^### [A-E]\.\d+|\Z)",
        path.read_text(),
    )
    question = re.search(
        r"(?ms)> \[!QUESTION\]- Full question statement\n(.*?)(?=\n(?!>)|\Z)",
        block.group(1) if block else "",
    )
    actual = re.sub(r"(?m)^> ?", "", question.group(1)).strip() if question else ""
    expected = standard_questions("divisibility_assessment.tex")["C.5"]
    if actual != expected:
        print("FAIL Divisibility C.5 full question differs from source or includes next-page material")
        return False
    print("PASS Divisibility C.5 question ends before next-page definitions")
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
        okay &= check_full_questions(page, solution_ids(page))

    okay &= check_divisibility_page_boundary(SOLUTIONS / "2300_Divisibility_Solutions.md")

    sets_text = (SOLUTIONS / "2300_Sets_Solutions.md").read_text()
    missing_set_plots = [
        number
        for number in range(1, 6)
        if f"![[assets/set_plot{number}.jpg]]" not in sets_text
        or not (ASSETS / f"set_plot{number}.jpg").is_file()
    ]
    if missing_set_plots:
        print(f"FAIL Sets is missing relation plot assets: {missing_set_plots}")
        okay = False
    else:
        print("PASS Sets          five relation plot prompts have local publishable images")

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
    okay &= check_full_questions(counting_page, solution_ids(counting_page))

    arguments_source = (ASSESSMENTS / "arguments_extended_practice.tex").read_text()
    arguments_expected = set(re.findall(r"\\bankitem\{([A-E]\.\d\.\d{2})\}", arguments_source))
    arguments_page = SOLUTIONS / "2300_Arguments_Solutions.md"
    arguments_text = arguments_page.read_text()
    okay &= report_alignment(
        "Arguments", arguments_expected, solution_ids(arguments_page, arguments=True)
    )
    okay &= check_page_basics(arguments_page)
    okay &= check_full_questions(
        arguments_page, solution_ids(arguments_page, arguments=True), arguments=True
    )
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
    okay &= check_full_questions(induction_page, solution_ids(induction_page))
    stale_phrases = ("one from each section A–E", "exactly five problems")
    stale = [phrase for phrase in stale_phrases if phrase in induction_text]
    if stale:
        print(f"FAIL Induction retains stale format text: {', '.join(stale)}")
        okay = False

    print("\nAll solution pages align with their current banks." if okay else "\nAlignment audit failed.")
    return 0 if okay else 1


if __name__ == "__main__":
    sys.exit(main())
