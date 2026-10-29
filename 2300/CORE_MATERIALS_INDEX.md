# COMP 2300 Core Materials Index

This file is the durable handoff map for the seven Autumn 2026 Core topics.
Student companions are study references, not permitted materials during a live
Core unless an accommodation explicitly says otherwise. Stable student-facing
PDFs live in `cheat_sheets/companion_pdfs/` and are committed as an explicit
exception to the normal generated-PDF ignore rule. Rebuild them from the TeX
sources with the repository's TeX Live 2025 workflow after source edits.

## Authoritative sources

| Order | Core | Student companion (flexible page count) | Assessment / practice bank | Complete solutions | Private instructor / grader guide | Preserved extended material |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Logic | `cheat_sheets/logic_core_companion.tex` | `core_assessments/logic_assessment.tex` | `obsidian_solutions/2300_Logic_Solutions.md` | `core_assessments/drafts/logic_core_instructor_notes.md` | `cheat_sheets/logic_cheat_sheet.tex`; `cheat_sheets/relevant_logic_definitions_reference.tex` |
| 2 | Arguments | `cheat_sheets/arguments_core_companion.tex` | `core_assessments/arguments_assessment.tex` (six-page selected bank) | `obsidian_solutions/2300_Arguments_Solutions.md` | `core_assessments/drafts/arguments_core_instructor_notes.md` | `core_assessments/arguments_extended_practice.tex` (all 210 items) |
| 3 | Sets | `cheat_sheets/sets_core_companion.tex` | `core_assessments/sets_assessment.tex` | `obsidian_solutions/2300_Sets_Solutions.md` | `core_assessments/drafts/sets_core_instructor_notes.md` | Chapter and quiz sources under `../course_highlights/` |
| 4 | Proofs | `cheat_sheets/proofs_core_companion.tex` | `core_assessments/proofs_assessment.tex` | `obsidian_solutions/2300_Proofs_Solutions.md` | `core_assessments/drafts/proofs_core_instructor_notes.md` | `cheat_sheets/proofs_cheat_sheet.tex` |
| 5 | Divisibility | `cheat_sheets/divisibility_reference_and_worked_examples.tex` | `core_assessments/divisibility_assessment.tex` | `obsidian_solutions/2300_Divisibility_Solutions.md` | `core_assessments/drafts/divisibility_core_instructor_notes.md` | `core_assessments/drafts/juan_divisibility_instruction_guide.tex` |
| 6 | Induction | `cheat_sheets/induction_core_companion.tex` | `core_assessments/induction_assessment.tex` (authoritative three-part exception) | `obsidian_solutions/2300_Induction_Solutions.md` | `core_assessments/drafts/induction_core_instructor_notes.md` | `core_assessments/drafts/induction_extended_problem_bank.tex`; `core_assessments/induction_assessment_long_proof.tex` |
| 7 | Counting | `cheat_sheets/counting_core_companion.tex` | `core_assessments/counting_assessment.tex` plus `counting_problem_sections/` | `obsidian_solutions/2300_Counting_Solutions.md` | `core_assessments/drafts/counting_core_instructor_notes.md` | Counting and probability chapters under `../course_highlights/` |

## Self-contained companion revision — 2026-10-29

The companion page budget is now flexible. Include a complete problem statement
before every existing worked example, followed by a worked solution and an answer
or conclusion. Retain the representative study-guide role, readable typography,
and original numbers only for exact assessment matches. Adapted examples must be
identified as similar examples. The earlier four-page build records below are
historical and no longer impose a page limit.

The local revision, page counts, example coverage, and verification record are
tracked in `cheat_sheets/COMPANION_SELF_CONTAINED_COVERAGE.md`. Alex approved
GitHub/Overleaf synchronization on 2026-10-29; remote delivery is verified
separately from the build record. Canvas uploads and Obsidian publication are
outside this companion revision.

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

Do not distribute the repository-root `output/pdf/arguments_core_practice_bank.pdf`: it is an
obsolete 30-page build dated September 6. The canonical Arguments assessment is
`core_assessments/arguments_assessment.tex` /
`core_assessments/pdfs/arguments_assessment.pdf` (6 pages); the preserved
`core_assessments/arguments_extended_practice.tex` builds to 29 pages
and contains all 210 practice items. Neither is the obsolete 30-page PDF.

## Validation and delivery record — 2026-10-28

### Safe stopping point

The reviewed seven-Core solution set, companion PDFs, and published Canvas
resource entry point are delivered as recorded below. The final 420-question
quiz package is saved and audited, but its corrected live overwrite import is
not verified. The seven existing quizzes remain unpublished pending final
instructions, module placement, approved dates, and saved read-back.
Alex explicitly confirmed **Keep unpublished for scheduling**; do not publish
them as optional review. This decision does not resume the paused work.

Resume from `homework_templates/CORE_SYNTAX_CANVAS_IMPORT_CHECKLIST.md`, which
contains the final package checksum, seven existing quiz URLs, and exact next
steps. There were no open Canvas editing/import tabs at the stopping check.
Do not repeat completed Obsidian publication or rebuild reviewed companions
merely to resume the unfinished Canvas quiz rollout.

The latest quiz-generator fixes, regression tests, student instruction HTML,
resource-page source, and this handoff are saved in a local checkpoint; they
have not yet received their next GitHub push / Overleaf pull. This does not
undo the already verified delivery of the companion PDFs and solutions.

The seven companion PDFs were compiled with TeX Live 2025 and visually checked
as four US-letter pages each. The substantive second review is complete, and
the reviewed sources and rebuilt stable PDFs are committed. Rebuilt copies
must replace the stable PDFs whenever sources change.

Final checks passed after merging the existing Overleaf commits:

- Solution alignment: all 350 full question/solution records, including all
  210 extended Arguments items; Divisibility C.5 ends before the next page's
  shared definitions, and all five Sets relation images are included.
- QTI: seven single-Core packages plus the combined package; 420 keyed items,
  60 items and 3 points per quiz, with the original Canvas identities retained.
- QTI regression tests: all 12 pass, including reproducibility, saved identity
  reuse, clean-course identifiers, invalid identity/options detection, and
  notation/feedback conversion. Final combined and individual package audits
  also pass; these are local package checks, not Canvas import verification.
- Arguments packets: reproducible 20-form and both 60-form seed manifests,
  with current packet TeX verified where applicable.
- Git whitespace checks: passed. No student records or bulk `output/` artifacts
  were committed.

### Verified GitHub delivery

Reviewed content commit: `048180e`. Both existing Overleaf commits were merged
without conflicts. The latest verified pushed revision is
`45acbbbe98b6b23ab55c9569dc8ba955bbb055e8`. The earlier material revision
`827c011a4dab41294c18903de9dd120af043a181` was also verified against the live
remote `main` reference and fetched file blobs. GitHub delivery alone does not
establish delivery on the other platforms; their separate read-back evidence
is recorded below.

All seven public raw PDF URLs below returned valid PDFs byte-for-byte identical
to the reviewed local copies. Each is four US-letter pages, with readable text
on every page and no replacement characters in text extraction.

| Companion | Verified public PDF | Bytes | Page/text check |
| --- | --- | ---: | --- |
| Logic | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/logic_core_companion.pdf) | 208208 | 4 pages; passed |
| Arguments | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/arguments_core_companion.pdf) | 236308 | 4 pages; passed |
| Sets | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/sets_core_companion.pdf) | 202015 | 4 pages; passed |
| Proofs | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/proofs_core_companion.pdf) | 192978 | 4 pages; passed |
| Divisibility | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/divisibility_core_companion.pdf) | 232337 | 4 pages; passed |
| Induction | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/induction_core_companion.pdf) | 197108 | 4 pages; passed |
| Counting | [PDF](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/counting_core_companion.pdf) | 246627 | 4 pages; passed |

### Verified Overleaf synchronization

The live project `68cc44fe290b01ea1636acd8` pulled all three available GitHub
commits. Its GitHub integration then reported no new commits to pull. The
Logic companion compiled live to four pages with zero errors and one harmless
`showhyphens`-changed warning. This verifies the project synchronization and
that live Logic compile, not a live compile of every other document.

### Verified Obsidian Publish delivery

All eight solution Markdown pages and five Sets relation JPG assets were
published. Public GETs of the actual served Markdown were byte-for-byte
identical to the reviewed sources, with 350 full-question callouts across the
solution pages. All seven companion PDF links and all five JPG assets were
also fetched as genuine file bytes, rather than just successful landing-page
responses. The companion PDF byte checks are listed above.

### Syntax and definitions practice

`homework_templates/generate_core_syntax_bank.py` is the content source;
`generate_core_syntax_qti.py` builds seven Canvas packages under `output/qti/`.
Each has 60 autograded items, 20 each of True/False/Not a truth-evaluable
proposition as written, answer feedback, and minimal repairs for malformed
items. Intended total: 3 Participation and Practice points, unlimited attempts,
highest score retained. Run `audit_core_syntax_qti.py` before import.

An earlier Chrome audit on October 28 found two prior sets of seven imports:
unpublished raw-notation archives, and unpublished Unicode practice quizzes
still displaying 60 points. The corrected packages now reuse the downloaded
Unicode import identities through the committed course-213452 identifier map.
Use the overwrite option; do not create another set of active quizzes. Live
import of the final corrected packages remains in progress. Import completion,
publication, module placement, grading category, and dates remain pending
read-back verification in the course audit; local package tests do not
establish these. No availability/due-date matrix for these seven new quizzes
has been approved; do not invent retrospective dates. See
`homework_templates/CORE_SYNTAX_CANVAS_IMPORT_CHECKLIST.md`.
No Student View or Canvas API.

### Required student entry points

For each Core, the Canvas module where it is introduced should contain the
student companion PDF, the practice quiz, and a direct link to its public
Obsidian solution page. The Core assignment should link to the same practice
bank and solutions. The book home is
`https://publish.obsidian.md/alexstevens/books/book-sections-md/rosen-abridged`.
Keep grader guides, answer keys, attempt manifests, and intentionally unused
material unpublished. Do not expose a private instructor key with a companion.

The published [Core Study Resources](https://canvas.du.edu/courses/213452/pages/core-study-resources)
page is verified as the first item in the published **Core Assessments** module
(`831530`). It links all seven public companions and exact Obsidian solution
permalinks, the book home, and the read-only Overleaf project. It excludes
private grading guides and explicitly identifies the companions as study
references, not permitted live-Core materials absent an accommodation.
The source is `canvas_resources/core_study_resources.html`. This completed
shared entry point does not establish the unfinished quiz rollout or every
individual weekly-module/Core-assignment link.

### Live rollout status

| Destination | Verified state | Remaining work |
| --- | --- | --- |
| Local source | Final substantive review, 350-record alignment, QTI audits/regressions, packet reproducibility, and stable PDF checks passed | Rebuild and re-audit after any later source changes |
| GitHub | Latest verified pushed revision `45acbbbe98b6b23ab55c9569dc8ba955bbb055e8`; seven public companion PDFs byte-verified | Push the later local quiz-generator/HTML/handoff checkpoint; bulk `output/` stays local |
| Overleaf | Material commits pulled into project `68cc44fe290b01ea1636acd8`; Logic companion live compile: 4 pages, 0 errors, 1 harmless warning | Pull the later checkpoint after its GitHub push; other live document compiles not claimed |
| Active Obsidian vault / Publish | Eight Markdown pages and five Sets JPGs published; actual served Markdown byte-identical; 350 question callouts, seven companion PDFs, and five genuine JPGs verified | Re-publish and recheck if reviewed content changes |
| Canvas 213452 | Core Study Resources page published and first in published Core Assessments module `831530`; companion, solution, book, and read-only Overleaf links verified | Final corrected quiz import/settings/publication/module read-back still pending; obtain approved availability/due dates; verify remaining per-Core entry points |

The current user-authorized goal includes these in-scope synchronization,
publication, and Canvas delivery actions. Do not publish unrelated material or
send messages. A local edit, open editor, or staged Publish dialog is not proof
of a completed live delivery step. Update this table only with read-back evidence.
