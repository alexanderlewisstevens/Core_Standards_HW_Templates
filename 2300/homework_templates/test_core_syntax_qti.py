#!/usr/bin/env python3
"""Offline regressions for safe, repeatable Core practice quiz imports."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import zipfile

from audit_core_syntax_qti import audit_archive, audit_combined, audit_documents
from generate_core_syntax_bank import CORES
from generate_core_syntax_qti import (
    build, deterministic_identifiers, reused_identifiers, saved_identifiers,
)


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
