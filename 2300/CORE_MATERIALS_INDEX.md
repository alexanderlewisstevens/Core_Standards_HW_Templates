# COMP 2300 Core Materials Index

This file is the durable handoff map for the seven Autumn 2026 Core topics.
Student companions are study references, not permitted materials during a live
Core unless an accommodation explicitly says otherwise. Stable student-facing
PDFs live in `cheat_sheets/companion_pdfs/` and are committed as an explicit
exception to the normal generated-PDF ignore rule. Rebuild them from the TeX
sources with the repository's TeX Live 2025 workflow after source edits.

## Authoritative sources

| Order | Core | Student companion (exactly 4 pages) | Assessment / practice bank | Complete solutions | Private instructor / grader guide | Preserved extended material |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Logic | `cheat_sheets/logic_core_companion.tex` | `core_assessments/logic_assessment.tex` | `obsidian_solutions/2300_Logic_Solutions.md` | `core_assessments/drafts/logic_core_instructor_notes.md` | `cheat_sheets/logic_cheat_sheet.tex`; `cheat_sheets/relevant_logic_definitions_reference.tex` |
| 2 | Arguments | `cheat_sheets/arguments_core_companion.tex` | `core_assessments/arguments_assessment.tex` (six-page selected bank) | `obsidian_solutions/2300_Arguments_Solutions.md` | `core_assessments/drafts/arguments_core_instructor_notes.md` | `core_assessments/arguments_extended_practice.tex` (all 210 items) |
| 3 | Sets | `cheat_sheets/sets_core_companion.tex` | `core_assessments/sets_assessment.tex` | `obsidian_solutions/2300_Sets_Solutions.md` | `core_assessments/drafts/sets_core_instructor_notes.md` | Chapter and quiz sources under `../course_highlights/` |
| 4 | Proofs | `cheat_sheets/proofs_core_companion.tex` | `core_assessments/proofs_assessment.tex` | `obsidian_solutions/2300_Proofs_Solutions.md` | `core_assessments/drafts/proofs_core_instructor_notes.md` | `cheat_sheets/proofs_cheat_sheet.tex` |
| 5 | Divisibility | `cheat_sheets/divisibility_reference_and_worked_examples.tex` | `core_assessments/divisibility_assessment.tex` | `obsidian_solutions/2300_Divisibility_Solutions.md` | `core_assessments/drafts/divisibility_core_instructor_notes.md` | `core_assessments/drafts/juan_divisibility_instruction_guide.tex` |
| 6 | Induction | `cheat_sheets/induction_core_companion.tex` | `core_assessments/induction_assessment.tex` (authoritative three-part exception) | `obsidian_solutions/2300_Induction_Solutions.md` | `core_assessments/drafts/induction_core_instructor_notes.md` | `core_assessments/drafts/induction_extended_problem_bank.tex`; `core_assessments/induction_assessment_long_proof.tex` |
| 7 | Counting | `cheat_sheets/counting_core_companion.tex` | `core_assessments/counting_assessment.tex` plus `counting_problem_sections/` | `obsidian_solutions/2300_Counting_Solutions.md` | `core_assessments/drafts/counting_core_instructor_notes.md` | Counting and probability chapters under `../course_highlights/` |

## Live-form and grade-entry rules

- Logic, Arguments, Sets, Proofs, Divisibility, and Counting use one selected
  problem from each section A--E. The supervised form lasts 20 minutes; four
  fully correct problems earn Meets and all five earn Exceeds.
- Induction is the deliberate exception: A.1 and B.1 are short, C.1 is the only
  long proof and is essential. C.1 plus exactly one correct short problem earns
  Meets; all three earn Exceeds.
- Canvas records only `0 = Not Yet`, `4 = Meets`, or `5 = Exceeds` on the single
  Core assignment. Do not convert the result to a percentage or create separate
  retake assignments.
- Every retake replaces the entire Core. A student may attempt a given Core once
  per day and may attempt a second, different Core that day only after passing
  the first Core attempted.
- Arguments response rule: B, C, and D require answer selection only and no
  justification. A and E allow at most one or two explanatory sentences.

## Generated attempt packets

`core_attempt_packets/` contains the reusable generator, 20-form and 60-form
TeX packets, and seed manifests. The generated Arguments packets and their
core-specific manifests incorporate the no-justification B--D rule:

- `arguments_core_20_forms_manifest_seed_2300-core-forms.md`
- `arguments_core_60_forms_manifest_seed_autumn-2026-core-attempts.md`

Regenerate packets only through the script so item IDs, original numbering,
seeds, and answer-key alignment remain reproducible. A single-Core run writes
a Core-specific manifest and cannot overwrite a shared all-Core manifest.

## Validation and delivery record — 2026-10-28

The seven companion PDFs were compiled with TeX Live 2025 and visually checked
as four US-letter pages each. A second substantive review is correcting stale
explanations and explicit-assumption gaps. Rebuilt copies must replace the
stable PDFs whenever sources change. The alignment audit checks 350 full
question/solution records (including all 210 extended Arguments items).

### Syntax and definitions practice

`homework_templates/generate_core_syntax_bank.py` is the content source;
`generate_core_syntax_qti.py` builds seven Canvas packages under `output/qti/`.
Each has 60 autograded items, 20 each of True/False/Not a truth-evaluable
proposition as written, answer feedback, and minimal repairs for malformed
items. Intended total: 3 Participation and Practice points, unlimited attempts,
highest score retained. Run `audit_core_syntax_qti.py` before import.

Live Chrome audit on October 28 found two prior sets of seven imports:
unpublished raw-notation archives, and unpublished Unicode practice quizzes
still displaying 60 points. Download the later source ZIPs through Canvas and
reuse their identifiers with the overwrite option; do not create another set
of active quizzes. Publication, module placement, grading category, and dates
must be read back after the corrected import. No Student View or Canvas API.

### Required student entry points

For each Core, the Canvas module where it is introduced should contain the
student companion PDF, the practice quiz, and a direct link to its public
Obsidian solution page. The Core assignment should link to the same practice
bank and solutions. The book home is
`https://publish.obsidian.md/alexstevens/books/book-sections-md/rosen-abridged`.
Keep grader guides, answer keys, attempt manifests, and intentionally unused
material unpublished. Do not expose a private instructor key with a companion.

### Live rollout status

| Destination | Verified state | Remaining work |
| --- | --- | --- |
| Local source | Saved; substantive second review in progress | Finish audit; rebuild changed PDFs; commit only reviewed materials |
| GitHub | Fetched; local branch behind two commits; remote changes inspected | Incorporate existing Overleaf edits without losing local work, push and verify |
| Overleaf | Project identified, not yet verified against this revision | Pull synchronized GitHub commit and verify files/compile |
| Active Obsidian vault | Earlier staged full-question revision exists | Resync final audited solutions/assets; batch publish; verify public pages |
| Canvas 213452 | Existing syntax imports verified unpublished | Overwrite matching quiz IDs, verify settings, attach resources in correct modules |

The current user-authorized goal includes these in-scope synchronization,
publication, and Canvas delivery actions. Do not publish unrelated material or
send messages. A local edit, open editor, or staged Publish dialog is not proof
of a completed live delivery step. Update this table only with read-back evidence.
