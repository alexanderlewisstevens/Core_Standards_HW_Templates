#!/usr/bin/env python3
"""Insert the authoritative full prompt above every Core worked solution.

The generated callouts are deliberately collapsed in Obsidian so the solution
pages remain easy to scan. Running this script again replaces the generated
callouts instead of duplicating them.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = Path(__file__).resolve().parent
ASSESSMENTS = ROOT / "core_assessments"
COUNTING = ROOT / "counting_problem_sections"
ATTEMPTS = ROOT / "core_attempt_packets"


def strip_comments(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def replace_braced_command(text: str, command: str, left: str, right: str) -> str:
    """Replace a one-argument TeX command, including arguments with nested braces."""
    needle = "\\" + command + "{"
    while needle in text:
        start = text.find(needle)
        depth = 1
        cursor = start + len(needle)
        while cursor < len(text) and depth:
            if text[cursor] == "{" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth += 1
            elif text[cursor] == "}" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth -= 1
            cursor += 1
        if depth:
            raise ValueError(f"Unclosed argument for {needle}")
        inner = text[start + len(needle) : cursor - 1]
        text = text[:start] + left + inner + right + text[cursor:]
    return text


def expand_choices(text: str) -> str:
    """Turn the local choice macro into ordinary list items."""
    return replace_braced_command(text, "choice", r"\item ", "")


def render_lists(text: str) -> str:
    """Convert the simple itemize/enumerate structures used by the banks."""
    output: list[str] = []
    stack: list[dict[str, object]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        enum = re.fullmatch(r"\\begin\{enumerate\}(?:\[label=\((\\?[A-Za-z]+)\*\)\])?", line)
        if enum:
            label = enum.group(1) or "arabic"
            stack.append({"kind": "enumerate", "label": label.lstrip("\\"), "count": 0})
            continue
        if line == r"\end{enumerate}":
            if stack:
                stack.pop()
            continue
        if line == r"\begin{itemize}":
            stack.append({"kind": "itemize", "label": "bullet", "count": 0})
            continue
        if line == r"\end{itemize}":
            if stack:
                stack.pop()
            continue
        if line.startswith(r"\item"):
            body = line[len(r"\item") :].strip()
            if stack:
                stack[-1]["count"] = int(stack[-1]["count"]) + 1
                count = int(stack[-1]["count"])
                label = str(stack[-1]["label"])
                if label == "alph":
                    prefix = f"- **({chr(96 + count)})** "
                elif label == "Alph":
                    prefix = f"- **({chr(64 + count)})** "
                elif label == "arabic":
                    prefix = f"- **({count})** "
                else:
                    prefix = "- "
            else:
                prefix = "- "
            output.append(prefix + body)
            continue
        output.append(raw_line.rstrip())
    return "\n".join(output)


def latex_to_markdown(text: str) -> str:
    text = strip_comments(text)
    text = expand_choices(text)
    text = text.replace("``", "“").replace("''", "”")
    text = text.replace("---", "—").replace("--", "–")
    text = text.replace(r"B\'ezout", "Bézout")
    text = re.sub(
        r"\\includegraphics(?:\[[^]]*\])?\{\.\./\.\./images/(set_plot[1-5]\.jpg)\}",
        r"![[assets/\1]]",
        text,
    )
    text = re.sub(
        r"\\begin\{(?:document|multicols\*?|center|flushleft|flushright)\}"
        r"(?:\{[^}]*\})?",
        "",
        text,
    )
    text = re.sub(
        r"\\end\{(?:document|multicols\*?|center|flushleft|flushright)\}",
        "",
        text,
    )
    text = re.sub(r"\\begin\{tcolorbox\}(?:\[[^]]*\])?", "", text)
    text = re.sub(r"\\end\{tcolorbox\}", "", text)
    text = re.sub(r"\\begin\{minipage\}(?:\[[^]]*\])?\{[^}]*\}", "", text)
    text = re.sub(r"\\end\{minipage\}", "", text)
    text = re.sub(
        r"\\(?:columnbreak|newpage|clearpage|vfill|smallskip|medskip|bigskip|"
        r"noindent|par|hfill|small|raggedcolumns|vennworkspace)\b",
        "",
        text,
    )
    text = re.sub(r"\\thispagestyle\{[^}]*\}", "", text)
    text = re.sub(r"\\vspace\*?\{[^}]*\}", "", text)
    text = text.replace(r"\[", "\n$$\n").replace(r"\]", "\n$$\n")
    text = render_lists(text)
    for command, left, right in (
        ("textbf", "**", "**"),
        ("emph", "*", "*"),
        ("textit", "*", "*"),
        ("texttt", "`", "`"),
    ):
        text = replace_braced_command(text, command, left, right)
    text = text.replace(r"\ ", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def marked_blocks(path: Path, marker: re.Pattern[str]) -> dict[str, str]:
    text = path.read_text()
    matches = list(marker.finditer(text))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end]
        # A page-level definitions box belongs to the next section, not to the
        # final problem on the preceding page (notably Divisibility C.5).
        boundary = re.search(
            r"(?m)^\\(?:(?:section|subsection)\*\{|end\{multicols\*?\}|(?:clearpage|newpage)\b)",
            body,
        )
        if boundary:
            body = body[: boundary.start()]
        blocks[match.group(1)] = latex_to_markdown(body)
    return blocks


def section_preambles(text: str, marker: re.Pattern[str]) -> dict[str, str]:
    """Return the shared directions that precede each standard-bank section."""
    preambles: dict[str, str] = {}
    sections = list(re.finditer(r"\\section\*\{[^}]*\}", text))
    for index, section in enumerate(sections):
        end = sections[index + 1].start() if index + 1 < len(sections) else len(text)
        section_body = text[section.end() : end]
        first_problem = marker.search(section_body)
        if not first_problem:
            continue
        letter = first_problem.group(1)[0]
        preamble = latex_to_markdown(section_body[: first_problem.start()])
        if preamble:
            preambles[letter] = preamble
    return preambles


def standard_questions(filename: str) -> dict[str, str]:
    path = ASSESSMENTS / filename
    text = path.read_text()
    if r"\problem{" in text:
        marker = re.compile(r"\\problem\{([A-E]\.\d+)\}")
    else:
        marker = re.compile(r"\\subsection\*\{([A-E]\.\d+)\}")
    questions = marked_blocks(path, marker)
    preambles = section_preambles(text, marker)
    return {
        label: "\n\n".join(part for part in (preambles.get(label[0], ""), body) if part)
        for label, body in questions.items()
    }


def argument_questions() -> dict[str, str]:
    return marked_blocks(
        ASSESSMENTS / "arguments_extended_practice.tex",
        re.compile(r"\\bankitem\{([A-E]\.\d\.\d{2})\}"),
    )


def counting_questions() -> dict[str, str]:
    questions: dict[str, str] = {}
    for path in sorted(COUNTING.glob("*.tex")):
        text = strip_comments(path.read_text())
        section_matches = list(re.finditer(r"\\section\*\{([A-E])\.[^}]*\}", text))
        for section_index, section_match in enumerate(section_matches):
            end = (
                section_matches[section_index + 1].start()
                if section_index + 1 < len(section_matches)
                else len(text)
            )
            section_text = text[section_match.end() : end]
            enum = re.search(
                r"\\begin\{enumerate\}\[[^]]*\](.*?)\\end\{enumerate\}",
                section_text,
                re.DOTALL,
            )
            if not enum:
                raise ValueError(f"No problem list found for Section {section_match.group(1)} in {path}")
            items = re.split(r"(?m)^\s*\\item\s+", enum.group(1))[1:]
            if len(items) != 5:
                raise ValueError(f"Expected five items in Section {section_match.group(1)}, found {len(items)}")
            for number, item in enumerate(items, start=1):
                questions[f"{section_match.group(1)}.{number}"] = latex_to_markdown(item)
    return questions


def induction_questions() -> dict[str, str]:
    text = (ATTEMPTS / "induction_core_60_forms.tex").read_text()
    pattern = re.compile(
        r"\\begin\{CompactCoreProblem\}\{([A-C]\.\d+)\}\{[^}]*\}"
        r"(.*?)\\end\{CompactCoreProblem\}",
        re.DOTALL,
    )
    variants: dict[str, set[str]] = {}
    for label, body in pattern.findall(text):
        variants.setdefault(label, set()).add(latex_to_markdown(body))
    if set(variants) != {f"{letter}.{number}" for letter in "ABC" for number in range(1, 6)}:
        raise ValueError("The Induction attempt packet does not contain the expected A.1–C.5 bank")
    inconsistent = {label: bodies for label, bodies in variants.items() if len(bodies) != 1}
    if inconsistent:
        raise ValueError(f"Induction labels have conflicting prompts: {sorted(inconsistent)}")
    return {label: next(iter(bodies)) for label, bodies in variants.items()}


def callout(question: str) -> str:
    lines = question.splitlines() or [""]
    quoted = "\n".join("> " + line if line else ">" for line in lines)
    return "> [!QUESTION]- Full question statement\n" + quoted


def update_solution(path: Path, questions: dict[str, str], *, arguments: bool = False) -> None:
    text = path.read_text()
    width = r"\d+\.\d{2}" if arguments else r"\d+"
    heading = re.compile(rf"(?m)^(###{{1,2}}) ([A-E]\.{width})(?:\s.*)?$")
    matches = list(heading.finditer(text))
    found = {match.group(2) for match in matches}
    if found != set(questions):
        missing = sorted(set(questions) - found)
        extra = sorted(found - set(questions))
        raise ValueError(f"{path.name}: heading/source mismatch; missing={missing}, extra={extra}")

    generated = re.compile(
        r"\n*> \[!QUESTION\]- Full question statement\n"
        r"(?:>(?: .*)?\n?)+(?=\n(?!>)|\Z)"
    )
    pieces: list[str] = []
    cursor = 0
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        pieces.append(text[cursor : match.end()])
        body = text[match.end() : block_end]
        body = generated.sub("\n", body, count=1)
        body = body.lstrip("\n")
        pieces.append("\n\n" + callout(questions[match.group(2)]) + "\n\n" + body)
        cursor = block_end
    pieces.append(text[cursor:])
    path.write_text("".join(pieces))


def main() -> None:
    jobs = [
        ("2300_Logic_Solutions.md", standard_questions("logic_assessment.tex"), False),
        ("2300_Arguments_Solutions.md", argument_questions(), True),
        ("2300_Sets_Solutions.md", standard_questions("sets_assessment.tex"), False),
        ("2300_Proofs_Solutions.md", standard_questions("proofs_assessment.tex"), False),
        ("2300_Divisibility_Solutions.md", standard_questions("divisibility_assessment.tex"), False),
        ("2300_Induction_Solutions.md", induction_questions(), False),
        ("2300_Counting_Solutions.md", counting_questions(), False),
    ]
    for filename, questions, is_arguments in jobs:
        update_solution(SOLUTIONS / filename, questions, arguments=is_arguments)
        print(f"Updated {filename}: {len(questions)} full questions")


if __name__ == "__main__":
    main()
