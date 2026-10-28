#!/usr/bin/env python3
"""Offline regressions for safe, repeatable Core practice quiz imports."""

from pathlib import Path
from tempfile import TemporaryDirectory
from html.parser import HTMLParser
import re
import unittest
import zipfile
from xml.etree import ElementTree as ET

from audit_core_syntax_qti import audit_archive, audit_combined, audit_documents
from generate_core_syntax_bank import CORES, CORE_NOTATION_GUIDES, form_items
from generate_core_syntax_qti import (
    build, deterministic_identifiers, reused_identifiers, saved_identifiers,
    feedback_html, math_to_html, math_to_unicode, tex_fragment_to_html,
)


class SafeMathHTML(HTMLParser):
    """Reject broken nesting or accidental HTML produced from a math token."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"p", "strong", "em", "sub", "sup"} or attrs:
            raise AssertionError(f"Unexpected HTML tag/attributes: {tag}, {attrs}")
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise AssertionError(f"Unbalanced HTML tag: {tag}")

    def finish(self):
        self.close()
        if self.stack:
            raise AssertionError(f"Unclosed HTML tags: {self.stack}")


class CoreSyntaxRendering(unittest.TestCase):
    def test_unbraced_and_grouped_command_arguments(self):
        cases = {
            r"\frac12": "(1)/(2)",
            r"\frac13": "(1)/(3)",
            r"\frac16": "(1)/(6)",
            r"\frac23": "(2)/(3)",
            r"\frac{3}{4}": "(3)/(4)",
            r"\frac{3}{0}": "(3)/(0)",
            r"\frac{n(n+1)}2": "(n(n+1))/(2)",
            r"\frac{n(n-1)}2": "(n(n-1))/(2)",
            r"\frac{5!}{2!\,2!}": "(5!)/(2! 2!)",
            r"\frac{5!}{2!\,}": "(5!)/(2!)",
            r"\binom52": "C(5, 2)",
            r"\binom53": "C(5, 3)",
            r"\binom54": "C(5, 4)",
            r"\binom nr": "C(n, r)",
            r"\binom5X": "C(5, X)",
            r"\binom{\,}{2}": "C(, 2)",
            r"\sqrt2": "√(2)",
            r"\sqrt{n+1}": "√(n+1)",
            r"\mathbb Z": "ℤ",
            r"\mathbb{Z}": "ℤ",
            r"\mathbb E[Z]": "𝔼[Z]",
            r"\mathcal P(A)": "𝒫(A)",
            r"\mathcal{P}(A)": "𝒫(A)",
            r"a\equiv b\pmod m": "a≡ b (mod m)",
            r"a\equiv b\pmod{m+1}": "a≡ b (mod m+1)",
            r"\operatorname{cause}(p,q)": "cause(p,q)",
            r"\frac{1}{\frac23}": "(1)/((2)/(3))",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(math_to_unicode(source), expected)
                self.assertEqual(math_to_html(source), expected)

    def test_command_tokens_cannot_erase_negation_or_prefixes(self):
        cases = {
            r"1\not\equiv_4 3": "1≢_4 3",
            r"x\not\in A": "x∉ A",
            r"x\not \in A": "x∉ A",
            r"1+\cdots+n": "1+…+n",
            r"d_k\cdots d_0": "d_k… d_0",
            r"\cdot\cdots\ldots": "·……",
            r"a\bmod m": "a mod m",
            r"p\iff q": "p iff q",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(math_to_unicode(source), expected)
        for source in (r"\unknown{x}", r"\cdotsx", r"\mathbb A", r"\not\to"):
            with self.subTest(unsupported=source), self.assertRaises(ValueError):
                math_to_unicode(source)

    def test_grouped_subscripts_and_exponents_are_not_flattened(self):
        cases = {
            r"a_{n+1}=a_n+3": ("a_(n+1)=a_n+3", "a<sub>n+1</sub>=a<sub>n</sub>+3"),
            r"a_{4}+": ("a_4+", "a<sub>4</sub>+"),
            r"a\equiv_m b": ("a≡_m b", "a≡<sub>m</sub> b"),
            r"2^{\Box}=32": ("2^□=32", "2<sup>□</sup>=32"),
            r"2^{k+1}": ("2^(k+1)", "2<sup>k+1</sup>"),
            r"2^{2^2}": ("2^(2^2)", "2<sup>2<sup>2</sup></sup>"),
            r"A^c": ("A^c", "A<sup>c</sup>"),
            r"(d_k\cdots d_0)_b": ("(d_k… d_0)_b", "(d<sub>k</sub>… d<sub>0</sub>)<sub>b</sub>"),
        }
        for source, (plain, markup) in cases.items():
            with self.subTest(source=source):
                self.assertEqual(math_to_unicode(source), plain)
                self.assertEqual(math_to_html(source), markup)

    def test_intentionally_invalid_statements_are_not_repaired(self):
        cases = {
            r"$a_{n+1}=a_n+$.": "a<sub>n+1</sub>=a<sub>n</sub>+.",
            r"$P(1)\land\cdots\land P(k)\to$.": "P(1)∧…∧ P(k)→.",
            r"$\Pr({}^c)=1$.": "Pr(<sup>c</sup>)=1.",
            r"$\{1,2$.": "{1,2.",
            r"$\binom{\,}{2}=10$.": "C(, 2)=10.",
            r"$\Pr(\{2\})=\frac16$.": "Pr({2})=(1)/(6).",
            r"$n<0$ and \emph{not} $n>1$.": "n&lt;0 and <em>not</em> n&gt;1.",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(tex_fragment_to_html(source), expected)
        with self.assertRaises(ValueError):
            tex_fragment_to_html("$p")
        with self.assertRaises(ValueError):
            tex_fragment_to_html(r"\unknown{p}")

    def test_all_420_prompts_feedback_and_14_description_fragments_are_safe(self):
        count = 0
        for core in CORES:
            fragments = [core.context, CORE_NOTATION_GUIDES[core.name]]
            for form_index in range(3):
                for _, _, version in form_items(core, form_index):
                    count += 1
                    fragments.extend((version.body, version.explanation, version.repair))
                    fragments.append(feedback_html(version.answer, version.explanation, version.repair))
            for source in fragments:
                # Complete feedback is already HTML; source fragments still
                # need the converter. Check every source field, not just body.
                rendered = source if source.startswith("<p>") else tex_fragment_to_html(source)
                with self.subTest(core=core.name, source=source):
                    self.assertNotRegex(rendered, r"\\[A-Za-z]+|\$|·s|�|\x00")
                    checker = SafeMathHTML()
                    checker.feed(rendered)
                    checker.finish()
        self.assertEqual(count, 420)

    def test_counting_term_feedback_and_minimal_repair_keep_n_key(self):
        counting = next(core for core in CORES if core.name == "Counting")
        matching = [version for form_index in range(3)
                    for _, _, version in form_items(counting, form_index)
                    if version.body == r"$\frac{5!}{2!\,}$."]
        self.assertEqual(len(matching), 1)
        version = matching[0]
        self.assertEqual(version.answer, "N")
        self.assertIn("complete arithmetic term", version.explanation)
        self.assertNotIn("denominator is incomplete", version.explanation)
        self.assertEqual(tex_fragment_to_html(version.repair), "(5!)/(2!)=60.")

    def test_reviewed_minimal_repairs_are_complete_propositions(self):
        expected = {
            ("Divisibility", 0, 9): r"$23\bmod 5=3$.",
            ("Divisibility", 2, 6): r"$\gcd(12,18)=6$.",
            ("Induction", 0, 20): r"$P(2)$.",
            ("Induction", 1, 19): r"$4\ge4$.",
            ("Induction", 0, 6): r"An ordinary induction step treats $k\ge1$ as fixed but arbitrary.",
            ("Induction", 1, 2): r"In ordinary induction, $P(k)$ is the induction hypothesis.",
            ("Induction", 1, 7): r"A strong-induction step may assume $P(1),\ldots,P(k)$.",
            ("Induction", 1, 18): r"In ordinary induction, $P(k)$ is the induction hypothesis.",
            ("Induction", 1, 16): r"$\forall n\ge1,\ 2^n\ge n+1$.",
            ("Induction", 0, 10): r"$\forall n\ge1,\ a_{n+1}=a_n+3$.",
            ("Induction", 0, 17): r"The inference $P(k),\ P(k)\to P(k+1)\ \therefore P(k+1)$ is valid.",
            ("Induction", 2, 5): r"The inference $P(1),P(2),P(3)\therefore P(1)\land P(2)\land P(3)$ is valid.",
            ("Induction", 2, 9): r"The two base-case propositions are $P(1)$ and $P(2)$.",
            ("Counting", 0, 4): r"Placing $7$ objects into $6$ boxes forces some box to receive at least two objects.",
            ("Counting", 0, 16): r"$\Pr(E\cup F)=\frac23$.",
            ("Counting", 0, 19): r"$\Pr(E\mid F)=\frac23$.",
            ("Counting", 1, 10): r"Five choices made twice with repetition produce $5^2=25$ sequences.",
            ("Counting", 1, 20): r"$\mathbb E[Z]=3.5$.",
            ("Counting", 2, 12): r"Selecting a two-person committee from five people gives $\binom52=10$ possible committees.",
        }
        by_name = {core.name: core for core in CORES}
        for (name, form, item), repair in expected.items():
            with self.subTest(core=name, form=form, item=item):
                _, _, version = form_items(by_name[name], form)[item - 1]
                self.assertEqual(version.answer, "N")
                self.assertEqual(version.repair, repair)

    def test_packages_match_every_source_statement_key_and_feedback(self):
        namespace = {"q": "http://www.imsglobal.org/xsd/ims_qtiasiv1p2"}
        with TemporaryDirectory(prefix="comp2300-render-test-") as directory:
            paths = build(Path(directory))
            for core, path in zip(CORES, paths):
                with self.subTest(core=core.name), zipfile.ZipFile(path) as bundle:
                    root = ET.fromstring(bundle.read("assessment.xml"))
                    items = root.findall(".//q:item", namespace)
                    source_items = [version for form_index in range(3)
                                    for _, _, version in form_items(core, form_index)]
                    self.assertEqual(len(items), 60)
                    for item, version in zip(items, source_items):
                        prompt = item.find("./q:presentation/q:material/q:mattext", namespace).text
                        feedback = item.find("./q:itemfeedback/q:flow_mat/q:material/q:mattext", namespace).text
                        key = item.find("./q:resprocessing/q:respcondition/q:conditionvar/q:varequal", namespace).text
                        self.assertIn(f"<p>{tex_fragment_to_html(version.body)}</p>", prompt)
                        self.assertEqual(feedback, feedback_html(version.answer, version.explanation, version.repair))
                        self.assertEqual(key, version.answer)
                    description = root.find(".//q:assessment/q:rubric/q:material/q:mattext", namespace).text
                    self.assertIn(tex_fragment_to_html(core.context), description)
                    self.assertIn(tex_fragment_to_html(CORE_NOTATION_GUIDES[core.name]), description)


class CoreSyntaxImports(unittest.TestCase):
    def test_saved_identity_default_and_repeatability(self):
        with TemporaryDirectory(prefix="comp2300-qti-test-") as directory:
            root = Path(directory)
            first = build(root / "first")
            again = build(root / "again")
            self.assertEqual(reused_identifiers(root / "first"), saved_identifiers())
            self.assertEqual([path.read_bytes() for path in first],
                             [path.read_bytes() for path in again])
            reused = build(root / "reused", root / "first")
            self.assertEqual([path.read_bytes() for path in first],
                             [path.read_bytes() for path in reused])
            for core, path in zip(CORES, first):
                with self.subTest(core=core.name):
                    self.assertEqual(audit_archive(path, core.name), [])
            self.assertEqual(audit_combined(first[-1]), [])

    def test_clean_course_identifiers_are_stable_and_explicit(self):
        with TemporaryDirectory(prefix="comp2300-qti-test-") as directory:
            root = Path(directory)
            first = build(root / "clean", new_identifiers=True)
            again = build(root / "again", new_identifiers=True)
            self.assertEqual([path.read_bytes() for path in first],
                             [path.read_bytes() for path in again])
            expected = {core.name: deterministic_identifiers(core.name) for core in CORES}
            self.assertEqual(reused_identifiers(root / "clean"), expected)
            for core, path in zip(CORES, first):
                with self.subTest(core=core.name):
                    self.assertNotEqual(expected[core.name].assessment,
                                        saved_identifiers()[core.name].assessment)
                    self.assertEqual(audit_archive(path, core.name, expected[core.name]), [])
            self.assertEqual(audit_combined(first[-1], expected), [])

    def test_audit_rejects_accidental_identity_change(self):
        with TemporaryDirectory(prefix="comp2300-qti-test-") as directory:
            first = build(Path(directory))[0]
            with zipfile.ZipFile(first) as bundle:
                assessment = bundle.read("assessment.xml").replace(
                    saved_identifiers()["Logic"].assessment.encode(), b"assessment_wrong",
                )
                errors = audit_documents(assessment, bundle.read("imsmanifest.xml"), "Logic")
            self.assertTrue(any("assessment identifier differs" in error for error in errors))

    def test_conflicting_identity_options_are_rejected(self):
        with TemporaryDirectory(prefix="comp2300-qti-test-") as directory:
            with self.assertRaises(ValueError):
                build(Path(directory), Path(directory), new_identifiers=True)


if __name__ == "__main__":
    unittest.main()
