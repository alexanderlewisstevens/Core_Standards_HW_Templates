#!/usr/bin/env python3
"""Build balanced, reproducibly randomized one-page attempt forms for every Core.

The public assessment banks remain the content source of truth. This script
preserves every source ID while recombining problems into unique print forms,
except for Induction, whose three-part format uses stable A/B/C variant IDs.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import random
import re
import shutil
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
ASSESSMENTS = HERE.parent / "core_assessments"
COUNTING = HERE.parent / "counting_problem_sections"
DEFAULT_OUTPUT = HERE.parents[1] / "output" / "pdf" / "comp2300_core_attempts"
CORE_ORDER = ("logic", "arguments", "sets", "proofs", "divisibility", "induction", "counting")


@dataclass(frozen=True)
class BankProblem:
    """A problem whose source-bank identifier must survive into the packet."""

    source_id: str
    body: str


def clean_block(body: str) -> str:
    """Remove bank-only layout commands while preserving problem content."""
    body = re.split(r"\\(?:sub)?section\*\{", body, maxsplit=1)[0]
    body = re.split(r"\\end\{(?:multicols\*?|document)\}", body, maxsplit=1)[0]
    body = re.sub(r"\\(?:columnbreak|clearpage|newpage)\b", "", body)
    body = re.sub(r"\\vfill\b", "", body)
    body = re.sub(r"\\vspace\*?\{[^{}]*\}", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def extract_problem_markers(path: Path, marker: str) -> dict[str, str]:
    text = path.read_text()
    matches = list(re.finditer(marker, text))
    found: dict[str, str] = {}
    for i, match in enumerate(matches):
        label = match.group(1)
        if label in found:
            raise RuntimeError(f"Duplicate source ID {label} in {path}")
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        found[label] = clean_block(text[match.end() : end])
    if not found:
        raise RuntimeError(f"No problem markers found in {path}")
    return found


def extract_counting_sections() -> dict[str, list[BankProblem]]:
    files = [
        COUNTING / "counting_section_a_intro.tex",
        COUNTING / "counting_section_b_principles_and_formulas.tex",
        COUNTING / "counting_section_c_applied_mcq.tex",
        COUNTING / "counting_section_d_advanced_free_response.tex",
    ]
    text = "\n".join(path.read_text() for path in files)
    section_matches = list(re.finditer(r"\\section\*\{([A-E])\.[^}]*\}", text))
    banks: dict[str, list[BankProblem]] = {}
    for i, match in enumerate(section_matches):
        label = match.group(1)
        end = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(text)
        section = text[match.end() : end]
        enum = re.search(r"\\begin\{enumerate\}.*?\n(.*?)\\end\{enumerate\}", section, re.S)
        if not enum:
            raise RuntimeError(f"Could not find counting list for section {label}")
        raw_items = re.split(r"(?m)^\s*\\item\s+", enum.group(1))[1:]
        banks[label] = [
            BankProblem(f"{label}.{number}", clean_block(item))
            for number, item in enumerate(raw_items, start=1)
        ]
    return banks


def extract_argument_bank() -> dict[str, str]:
    text = (ASSESSMENTS / "arguments_extended_practice.tex").read_text()
    matches = list(re.finditer(r"\\bankitem\{([A-E]\.\d\.\d{2})\}", text))
    found: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        label = match.group(1)
        if label in found:
            raise RuntimeError(f"Duplicate source ID {label} in Arguments bank")
        found[label] = clean_block(text[match.end() : end])
    return found


def organize_marked_bank(raw: dict[str, str], sections: str = "ABCDE") -> dict[str, list[BankProblem]]:
    """Validate and preserve the exact identifiers declared by a source bank."""
    banks: dict[str, list[BankProblem]] = {}
    for section in sections:
        labels = [f"{section}.{number}" for number in range(1, 6)]
        missing = [label for label in labels if label not in raw]
        if missing:
            raise RuntimeError(f"Missing source IDs: {', '.join(missing)}")
        banks[section] = [BankProblem(label, raw[label]) for label in labels]
    expected = {problem.source_id for problems in banks.values() for problem in problems}
    extras = sorted(set(raw) - expected)
    if extras:
        raise RuntimeError(f"Unexpected source IDs: {', '.join(extras)}")
    return banks


def core_rng(seed: str, slug: str) -> random.Random:
    """Return a stable core-specific RNG, independent of build order."""
    digest = hashlib.sha256(f"{seed}:{slug}".encode()).digest()
    return random.Random(int.from_bytes(digest[:16], "big"))


def balanced_random_forms(
    sections: Sequence[str], bank_size: int, form_count: int, rng: random.Random
) -> list[dict[str, int]]:
    """Create unique seeded forms with perfectly/near-perfectly balanced use.

    Equal-sized banks are decomposed into cyclic orbits.  Every full orbit uses
    every problem exactly once in every section.  Consequently 60 forms from a
    five-item bank use every problem exactly 12 times per section while still
    producing 60 distinct combinations.
    """
    if form_count < 1:
        raise ValueError("form_count must be positive")
    capacity = bank_size ** len(sections)
    if form_count > capacity:
        raise ValueError(
            f"Requested {form_count} forms, but {len(sections)} sections with "
            f"{bank_size} items each permit only {capacity} unique combinations"
        )

    item_maps: dict[str, list[int]] = {}
    for section in sections:
        values = list(range(bank_size))
        rng.shuffle(values)
        item_maps[section] = values

    # Each offset vector represents one disjoint orbit in Z_m^s.
    orbit_offsets = list(itertools.product(range(bank_size), repeat=len(sections) - 1))
    rng.shuffle(orbit_offsets)
    quotient, remainder = divmod(form_count, bank_size)
    chosen = orbit_offsets[: quotient + (1 if remainder else 0)]
    rows: list[dict[str, int]] = []
    for orbit_number, offsets in enumerate(chosen):
        xs = list(range(bank_size))
        rng.shuffle(xs)
        take = remainder if orbit_number == quotient and remainder else bank_size
        for x in xs[:take]:
            raw_indices = (x,) + tuple((x + offset) % bank_size for offset in offsets)
            rows.append(
                {
                    section: item_maps[section][index]
                    for section, index in zip(sections, raw_indices)
                }
            )
    rng.shuffle(rows)
    if len({tuple(row[section] for section in sections) for row in rows}) != form_count:
        raise RuntimeError("Randomizer produced duplicate forms")
    return rows


def tex_preamble(extra: str = "") -> str:
    return rf"""\documentclass[9pt]{{extarticle}}
\usepackage{{core_attempt_forms}}
{extra}
\begin{{document}}
"""


def write_five_section_packet(
    slug: str,
    form_prefix: str,
    core_name: str,
    banks: dict[str, list[BankProblem]],
    titles: dict[str, str],
    directions: dict[str, str],
    split_after: int,
    form_count: int,
    seed: str,
    extra_preamble: str = "",
    dense: bool = False,
    header_note: str = "",
) -> list[dict[str, str]]:
    sections = tuple("ABCDE")
    sizes = {len(banks[section]) for section in sections}
    if len(sizes) != 1:
        raise RuntimeError(f"{core_name} bank sections must have equal sizes; got {sorted(sizes)}")
    bank_size = sizes.pop()
    forms = balanced_random_forms(sections, bank_size, form_count, core_rng(seed, slug))
    env = "DenseCoreProblem" if dense else "CoreProblem"
    lines = [tex_preamble(extra_preamble)]
    manifest: list[dict[str, str]] = []
    for number, selection in enumerate(forms, start=1):
        width = max(2, len(str(form_count)))
        form_code = f"{form_prefix}{number:0{width}d}"
        header_tail = r"\FivePartScoring" + (f" {header_note}" if header_note else "")
        lines.append(
            rf"\CoreHeader{{{core_name}}}{{{form_code}}}{{A--E}}{{{header_tail}}}"
        )
        lines.append(r"\begin{multicols}{2}")
        row = {"form": form_code}
        for position, section in enumerate("ABCDE", start=1):
            item_index = selection[section]
            problem = banks[section][item_index]
            row[section] = problem.source_id
            lines.append(rf"\begin{{{env}}}{{{problem.source_id}}}{{{titles[section]}}}")
            if directions.get(section):
                lines.append(rf"{{\scriptsize\textit{{{directions[section]}}}\par}}")
            lines.append(problem.body)
            lines.append(rf"\end{{{env}}}")
            if position == split_after:
                lines.append(r"\columnbreak")
        lines.append(r"\end{multicols}")
        lines.append(r"\CoreWorkArea")
        if number != len(forms):
            lines.append(r"\FormBreak")
        manifest.append(row)
    lines.append(r"\end{document}")
    (HERE / f"{slug}_core_{form_count}_forms.tex").write_text("\n".join(lines) + "\n")
    return manifest


def write_arguments_packet(form_count: int, seed: str) -> list[dict[str, str]]:
    bank = extract_argument_bank()

    # Use 100 distinct prompts.  A and E avoid the longest integrated-writing
    # family so that a complete five-problem question sheet remains one page.
    codes: dict[str, list[str]] = {
        "A": [code for n in range(1, 11) for code in (f"A.2.{n:02d}", f"A.3.{n:02d}")],
        "B": [f"B.{kind}.{n:02d}" for n in range(1, 5) for kind in range(1, 6)],
        "C": [f"C.{kind}.{n:02d}" for n in range(1, 5) for kind in range(1, 6)],
        "D": [f"D.{kind}.{n:02d}" for n in range(1, 5) for kind in range(1, 6)],
        "E": [code for n in range(1, 11) for code in (f"E.1.{n:02d}", f"E.2.{n:02d}")],
    }
    missing = [code for section in codes.values() for code in section if code not in bank]
    if missing:
        raise RuntimeError(f"Missing Arguments bank items: {missing}")

    titles = {
        "A": "Reconstruct or test an argument",
        "B": "Argument anatomy and inference",
        "C": "Assumptions and evidence",
        "D": "Principles and explanations",
        "E": "Evaluate and revise",
    }
    directions = {
        "A": (
            "Give only the short response requested: no more than two compact "
            "results and no extra justification."
        ),
        "B": "Choose one answer only. No written justification is required.",
        "C": "Choose one answer only. No written justification is required.",
        "D": "Choose one answer only. No written justification is required.",
        "E": (
            "Give only the requested answer and one brief reason. One sentence "
            "is enough for any explanation."
        ),
    }
    problem_banks = {
        section: [BankProblem(code, bank[code]) for code in section_codes]
        for section, section_codes in codes.items()
    }
    forms = balanced_random_forms(
        tuple("ABCDE"), len(codes["A"]), form_count, core_rng(seed, "arguments")
    )
    lines = [tex_preamble(r"\newcommand{\choice}[1]{\item #1}")]
    manifest: list[dict[str, str]] = []
    for index, selection in enumerate(forms):
        width = max(2, len(str(form_count)))
        form_code = f"A{index + 1:0{width}d}"
        lines.append(rf"\CoreHeader{{Arguments}}{{{form_code}}}{{A--E}}{{\FivePartScoring}}")
        lines.append(r"\begin{multicols}{2}")
        row = {"form": form_code}
        for position, section in enumerate("ABCDE", start=1):
            problem = problem_banks[section][selection[section]]
            row[section] = problem.source_id
            lines.append(
                rf"\begin{{DenseCoreProblem}}{{{problem.source_id}}}{{{titles[section]}}}"
            )
            lines.append(rf"{{\scriptsize\textit{{{directions[section]}}}\par}}")
            lines.append(problem.body)
            lines.append(r"\end{DenseCoreProblem}")
            if position == 2:
                lines.append(r"\columnbreak")
        lines.append(r"\end{multicols}")
        lines.append(r"\CoreWorkArea")
        if index != form_count - 1:
            lines.append(r"\FormBreak")
        manifest.append(row)
    lines.append(r"\end{document}")
    (HERE / f"arguments_core_{form_count}_forms.tex").write_text("\n".join(lines) + "\n")
    return manifest


def induction_banks() -> dict[str, list[BankProblem]]:
    a = [
        r"""For the claim that every integer $n\ge2$ is a product of one or more primes, state (i) the base case, (ii) the strong induction hypothesis for an arbitrary $k\ge2$, (iii) what must be proved for $k+1$, and (iv) the two cases used in the induction step. Do not complete the proof.""",
        r"""For $1+2+\cdots+n=n(n+1)/2$ for every $n\ge1$, state $P(n)$, verify the base case, state the induction hypothesis $P(k)$, and state exactly what must be shown for $P(k+1)$. Do not complete the next-case algebra.""",
        r"""For the claim $7\mid(8^n-1)$ for every integer $n\ge0$, state $P(n)$, the base case, the induction hypothesis using an integer witness, and the divisibility statement required for $k+1$. Do not complete the algebra.""",
        r"""For the claim that every amount $n\ge18$ can be made using 4-cent and 7-cent stamps, list sufficient base cases, state a strong induction hypothesis through $k$, and explain which earlier amount is used to construct $k+1$. Do not complete the proof.""",
        r"""For $2^n\ge n+1$ for every integer $n\ge0$, state $P(n)$, verify the base case, state the induction hypothesis, and write the first equality and inequality that should begin the $k+1$ step. Do not finish the proof.""",
    ]
    b = [
        r"""A student tries to prove $2^n\ge n+1$ for $n\ge0$ by assuming $2^{k+1}\ge k+2$ in the induction step. Identify the circularity, state the correct induction hypothesis, and give a valid chain of inequalities for the next case.""",
        r"""A recurrence proof uses both $P(k)$ and $P(k-1)$ to prove $P(k+1)$ but verifies only $P(0)$. Explain what is missing. State sufficient base cases and a valid strong induction hypothesis.""",
        r"""In the false proof that all positive integers in any finite list are equal, the step applies the hypothesis to the first $k$ and last $k$ entries and claims the groups overlap. Identify the first $k$ for which overlap is needed and explain precisely why the step fails.""",
        r"""A student proving $1+3+\cdots+(2n-1)=n^2$ writes $k^2+(2k-1)=(k+1)^2$. Identify the incorrect next term, repair the calculation, and state where the induction hypothesis is used.""",
        r"""A student proving $7\mid(8^n-1)$ says, “Assume $7\mid(8^{k+1}-1)$; therefore the next case holds.” Identify the error, replace it with the correct induction hypothesis, and show an algebraic decomposition that proves the $k+1$ case.""",
    ]
    c: list[str] = []
    for weight in range(1, 6):
        if weight == 1:
            lhs = r"\sum_{j=0}^{n}\binom{n}{j}"
            rhs = r"2^n"
        else:
            lhs = rf"\sum_{{j=0}}^{{n}} {weight}^{{n-j}}\binom{{n}}{{j}}"
            rhs = rf"{weight + 1}^n"
        c.append(
            rf"""You may use Pascal's identity
\[
\binom{{k+1}}{{j}}=\binom{{k}}{{j}}+\binom{{k}}{{j-1}}
\quad(1\le j\le k),\qquad
\binom{{n}}{{0}}=\binom{{n}}{{n}}=1.
\]
Prove by mathematical induction that
\[
{lhs}={rhs}\qquad\text{{for every integer }}n\ge0.
\]
State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof."""
        )
    return {
        section: [
            BankProblem(f"{section}.{number}", body)
            for number, body in enumerate(problems, start=1)
        ]
        for section, problems in {"A": a, "B": b, "C": c}.items()
    }


def write_induction_packet(form_count: int, seed: str) -> list[dict[str, str]]:
    banks = induction_banks()
    forms = balanced_random_forms(
        tuple("ABC"), len(banks["A"]), form_count, core_rng(seed, "induction")
    )
    lines = [tex_preamble()]
    manifest: list[dict[str, str]] = []
    for number, selection in enumerate(forms, start=1):
        width = max(2, len(str(form_count)))
        form_code = f"I{number:0{width}d}"
        lines.append(rf"\CoreHeader{{Induction}}{{{form_code}}}{{A--C}}{{\ThreePartScoring}}")
        # Balance the two short sections across the two columns so that the
        # full-width proof section can remain on the same page.
        lines.append(r"\begin{multicols}{2}")
        row = {"form": form_code}
        for section, title in (("A", "Proof setup"), ("B", "Diagnose and repair")):
            idx = selection[section]
            problem = banks[section][idx]
            row[section] = problem.source_id
            lines.append(
                rf"\begin{{CompactCoreProblem}}{{{problem.source_id}}}{{{title}}}"
            )
            lines.append(problem.body)
            lines.append(r"\end{CompactCoreProblem}")
        lines.append(r"\end{multicols}")
        idx = selection["C"]
        problem = banks["C"][idx]
        row["C"] = problem.source_id
        lines.append(
            rf"\begin{{CompactCoreProblem}}{{{problem.source_id}}}{{Complete inductive proof}}"
        )
        lines.append(problem.body)
        lines.append(r"\end{CompactCoreProblem}")
        lines.append(r"\CoreWorkArea")
        if number != len(forms):
            lines.append(r"\FormBreak")
        manifest.append(row)
    lines.append(r"\end{document}")
    (HERE / f"induction_core_{form_count}_forms.tex").write_text("\n".join(lines) + "\n")
    return manifest


def manifest_table(name: str, rows: list[dict[str, str]]) -> str:
    sections = [key for key in "ABCDE" if key in rows[0]]
    header = "| Form | " + " | ".join(sections) + " |"
    rule = "|---|" + "---|" * len(sections)
    body = ["| " + " | ".join([row["form"]] + [row[s] for s in sections]) + " |" for row in rows]
    return "\n".join([f"## {name}", "", header, rule, *body, ""])


def generate_packets(
    selected: Sequence[str], form_count: int, seed: str
) -> dict[str, list[dict[str, str]]]:
    """Generate TeX packets for the selected Core slugs."""
    manifests: dict[str, list[dict[str, str]]] = {}
    selected_set = set(selected)
    if "logic" in selected_set:
        logic_raw = extract_problem_markers(
            ASSESSMENTS / "logic_assessment.tex", r"\\problem\{([A-E]\.\d+)\}"
        )
        manifests["Logic"] = write_five_section_packet(
            "logic",
            "L",
            "Logic",
            organize_marked_bank(logic_raw),
            {
                "A": "Truth tables",
                "B": "Translation and meaning",
                "C": "Quantifier negation",
                "D": "Consistency and satisfiability",
                "E": "Logical equivalence",
            },
            {
                "A": "Construct the complete eight-row table; show useful intermediate columns and classify the result.",
                "B": "Define any predicates/domains requested; translate exactly and diagnose the proposed translation.",
                "C": "Symbolize and negate as directed; move every negation directly before a predicate.",
                "D": "Translate the conditions. Give a satisfying assignment or a short contradiction, then complete the final request.",
                "E": "Give an equivalence chain and cite one permitted rule at every step: implication, double negation, De Morgan, distributive, associative, commutative, or idempotent.",
            },
            split_after=3,
            form_count=form_count,
            seed=seed,
        )

    sets_extra = r"""
\newcommand{\vennworkspace}{%
\begin{tikzpicture}[scale=0.38]
  \draw[thick] (-2.2,-1.6) rectangle (4.0,3.3) node[above left]{$\mathfrak U$};
  \def\rad{1.3}\coordinate (A) at (0,0);\coordinate (B) at (1.8,0);\coordinate (C) at (0.9,1.4);
  \draw (A) circle (\rad);\draw (B) circle (\rad);\draw (C) circle (\rad);
  \node at ($(A)+(0,\rad+0.35)$) {$A$};\node at ($(B)+(0,\rad+0.35)$) {$B$};\node at ($(C)+(0,\rad+0.35)$) {$C$};
\end{tikzpicture}}
"""
    if "sets" in selected_set:
        sets_raw = extract_problem_markers(
            ASSESSMENTS / "sets_assessment.tex",
            r"\\subsection\*\{([A-E]\.\d+)(?:[^}]*)\}",
        )
        manifests["Sets"] = write_five_section_packet(
            "sets",
            "S",
            "Sets",
            organize_marked_bank(sets_raw),
            {
                "A": "Set language",
                "B": "Set operations",
                "C": "Relations",
                "D": "Functions, images, and preimages",
                "E": "Prove or refute",
            },
            {
                "A": "Complete every part.",
                "B": "Shade the formula's region, then name it using set operations.",
                "C": "List the relation, evaluate both quantified statements, and classify whether it is a function.",
                "D": "Compute the requested image/preimage and justify the function classification.",
                "E": "If true, prove by following an arbitrary element; if false, give and compute a finite counterexample.",
            },
            split_after=2,
            form_count=form_count,
            seed=seed,
            extra_preamble=sets_extra,
        )

    if "proofs" in selected_set:
        proofs_raw = extract_problem_markers(
            ASSESSMENTS / "proofs_assessment.tex",
            r"\\subsection\*\{([A-E]\.\d+)(?:[^}]*)\}",
        )
        manifests["Proofs"] = write_five_section_packet(
            "proofs",
            "P",
            "Proofs",
            organize_marked_bank(proofs_raw),
            {
                "A": "Inference and proof structure",
                "B": "Direct proof",
                "C": "Contraposition or contradiction",
                "D": "Cases, existence, or counterexample",
                "E": "Strategy choice and repair",
            },
            {},
            split_after=3,
            form_count=form_count,
            seed=seed,
            header_note="Use complete sentences, name the requested method or rule, and justify every inference.",
        )

    if "divisibility" in selected_set:
        divisibility_raw = extract_problem_markers(
            ASSESSMENTS / "divisibility_assessment.tex", r"\\problem\{([A-E]\.\d+)\}"
        )
        manifests["Divisibility"] = write_five_section_packet(
            "divisibility",
            "D",
            "Divisibility",
            organize_marked_bank(divisibility_raw),
            {
                "A": "Division and congruence",
                "B": "Integer representations",
                "C": "Modular arithmetic",
                "D": r"GCD and B\'ezout coefficients",
                "E": "Proof from definitions",
            },
            {
                "A": "Use the division algorithm and least nonnegative remainder; justify congruences from the definition.",
                "B": "Show place values, grouping, or repeated division, and check all digits.",
                "C": "Give least nonnegative residues and show efficient reductions.",
                "D": "Display the Euclidean algorithm and back-substitution.",
                "E": "State arbitrary integers and witnesses explicitly; end by matching the definition.",
            },
            split_after=3,
            form_count=form_count,
            seed=seed,
            extra_preamble=r"\newcommand{\equivmod}[1]{\mathrel{\equiv_{#1}}}",
        )

    if "induction" in selected_set:
        manifests["Induction"] = write_induction_packet(form_count, seed)

    if "counting" in selected_set:
        manifests["Counting"] = write_five_section_packet(
            "counting",
            "C",
            "Counting",
            extract_counting_sections(),
            {
                "A": "Fundamental counting rules",
                "B": "Arrangements and selections",
                "C": "Constrained counting",
                "D": "Probability models",
                "E": "Modeling and interpretation",
            },
            {
                section: "Name and justify the model; exact fractions and unsimplified products are acceptable."
                for section in "ABCDE"
            },
            split_after=3,
            form_count=form_count,
            seed=seed,
        )

    if "arguments" in selected_set:
        manifests["Arguments"] = write_arguments_packet(form_count, seed)

    return manifests


def validate_manifests(manifests: dict[str, list[dict[str, str]]], form_count: int) -> None:
    """Fail before compilation if forms are duplicated or problem use is skewed."""
    for name, rows in manifests.items():
        if len(rows) != form_count:
            raise RuntimeError(f"{name}: expected {form_count} forms, found {len(rows)}")
        sections = [section for section in "ABCDE" if section in rows[0]]
        form_codes = [row["form"] for row in rows]
        if len(set(form_codes)) != form_count:
            raise RuntimeError(f"{name}: duplicate form codes")
        tuples = [tuple(row[section] for section in sections) for row in rows]
        if len(set(tuples)) != form_count:
            raise RuntimeError(f"{name}: duplicate problem combinations")
        for section in sections:
            counts = Counter(row[section] for row in rows)
            if max(counts.values()) - min(counts.values()) > 1:
                raise RuntimeError(f"{name} section {section}: unbalanced problem use {counts}")


def write_manifest(
    manifests: dict[str, list[dict[str, str]]], form_count: int, seed: str
) -> Path:
    safe_seed = re.sub(r"[^A-Za-z0-9_-]+", "-", seed).strip("-") or "seed"
    if len(manifests) == 1:
        only_core = next(iter(manifests)).lower()
        path = HERE / (
            f"{only_core}_core_{form_count}_forms_manifest_seed_{safe_seed}.md"
        )
    else:
        path = HERE / f"core_attempt_form_manifest_{form_count}_seed_{safe_seed}.md"
    parts = [
        f"# COMP 2300 Core Attempt Form Manifest — {form_count} forms",
        "",
        "> Private instructor artifact. Do not publish or distribute with the student forms.",
        "",
        f"Reproducible random seed: `{seed}`.",
        "Each PDF contains one single-sided question sheet per form, with source-bank IDs printed in every problem heading.",
        "Forms are unique and problem use is balanced within each section.",
        "",
    ]
    for name in ("Logic", "Arguments", "Sets", "Proofs", "Divisibility", "Induction", "Counting"):
        if name in manifests:
            parts.append(manifest_table(name, manifests[name]))
    path.write_text("\n".join(parts).rstrip() + "\n")
    return path


def packet_path(slug: str, form_count: int, suffix: str) -> Path:
    return HERE / f"{slug}_core_{form_count}_forms.{suffix}"


def compile_packet(slug: str, form_count: int) -> Path:
    latexmk = shutil.which("latexmk")
    if not latexmk:
        raise RuntimeError("latexmk is required for --compile")
    tex = packet_path(slug, form_count, "tex")
    command = [
        latexmk,
        "-norc",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-synctex=1",
        tex.name,
    ]
    completed = subprocess.run(command, cwd=HERE, text=True, capture_output=True)
    if completed.returncode:
        tail = "\n".join((completed.stdout + completed.stderr).splitlines()[-50:])
        raise RuntimeError(f"Compilation failed for {tex.name}:\n{tail}")
    return packet_path(slug, form_count, "pdf")


def verify_pdf(slug: str, rows: list[dict[str, str]], form_count: int) -> None:
    pdfinfo = shutil.which("pdfinfo")
    pdftotext = shutil.which("pdftotext")
    if not pdfinfo or not pdftotext:
        raise RuntimeError("pdfinfo and pdftotext are required for --verify")
    pdf = packet_path(slug, form_count, "pdf")
    info = subprocess.run([pdfinfo, str(pdf)], text=True, capture_output=True, check=True).stdout
    pages_match = re.search(r"(?m)^Pages:\s+(\d+)$", info)
    size_match = re.search(r"(?m)^Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    if not pages_match or int(pages_match.group(1)) != form_count:
        raise RuntimeError(f"{pdf.name}: expected {form_count} pages")
    if not size_match or tuple(round(float(size_match.group(i))) for i in (1, 2)) != (612, 792):
        raise RuntimeError(f"{pdf.name}: pages are not US Letter")

    text = subprocess.run(
        [pdftotext, "-layout", str(pdf), "-"], text=True, capture_output=True, check=True
    ).stdout
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    if len(pages) != form_count:
        raise RuntimeError(f"{pdf.name}: text extraction found {len(pages)} pages")
    for page_number, (page, row) in enumerate(zip(pages, rows), start=1):
        if f"Form {row['form']}" not in page:
            raise RuntimeError(f"{pdf.name} page {page_number}: missing form code {row['form']}")
        for section in (key for key in "ABCDE" if key in row):
            if row[section] not in page:
                raise RuntimeError(
                    f"{pdf.name} page {page_number}: missing source ID {row[section]}"
                )
    log = packet_path(slug, form_count, "log")
    if log.exists():
        diagnostics = [
            line
            for line in log.read_text(errors="replace").splitlines()
            if "Overfull \\hbox" in line or "Underfull \\hbox" in line
        ]
        if diagnostics:
            raise RuntimeError(f"{pdf.name}: layout diagnostics:\n" + "\n".join(diagnostics))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate reproducibly randomized, balanced COMP 2300 Core attempt packets."
    )
    parser.add_argument(
        "cores",
        nargs="*",
        help="Core slugs to build; omit to build all seven.",
    )
    parser.add_argument("--forms", type=int, default=20, help="Number of one-page forms per Core.")
    parser.add_argument(
        "--seed",
        default="2300-core-forms",
        help="Reproducible random seed; change it to create a new packet ordering.",
    )
    parser.add_argument("--compile", action="store_true", help="Compile generated TeX with latexmk.")
    parser.add_argument("--verify", action="store_true", help="Verify page count, size, IDs, and layout.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help=f"Copy finished PDFs here (suggested: {DEFAULT_OUTPUT}).",
    )
    args = parser.parse_args(argv)
    invalid = sorted(set(args.cores) - set(CORE_ORDER))
    if invalid:
        parser.error(
            f"unsupported Core(s): {', '.join(invalid)}; choose from {', '.join(CORE_ORDER)}"
        )
    return args


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    selected = tuple(args.cores) if args.cores else CORE_ORDER
    manifests = generate_packets(selected, args.forms, args.seed)
    validate_manifests(manifests, args.forms)
    manifest = write_manifest(manifests, args.forms, args.seed)

    title_to_slug = {slug.title(): slug for slug in CORE_ORDER}
    built: list[Path] = []
    for title, rows in manifests.items():
        slug = title_to_slug[title]
        pdf = compile_packet(slug, args.forms) if args.compile else packet_path(slug, args.forms, "pdf")
        if args.verify:
            if not pdf.exists():
                raise RuntimeError(f"{pdf} does not exist; add --compile")
            verify_pdf(slug, rows, args.forms)
        if args.output_dir:
            if not pdf.exists():
                raise RuntimeError(f"{pdf} does not exist; add --compile")
            args.output_dir.mkdir(parents=True, exist_ok=True)
            destination = args.output_dir / pdf.name
            shutil.copy2(pdf, destination)
            built.append(destination)
        else:
            built.append(pdf)

    print(f"Manifest: {manifest}")
    for path in built:
        print(path)


if __name__ == "__main__":
    main()
