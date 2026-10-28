# Core syntax practice: import and verification

Local audit: **2026-10-28 — passed.** This records package readiness, not proof of a successful live Canvas import or student access.

Combined upload: `output/qti/Core_All_Syntax_Practice_Canvas_QTI.zip` (repository root).

SHA-256: `7aec132e14c38ee97b2e8f288c7b8732f711b3eef5e42c916c1044daf51e5022`

## Saved stopping point — 2026-10-28

Alex explicitly chose **Keep unpublished for scheduling** for all seven new
practice quizzes. Do not release them as optional review or publish them without
subsequent direction. Final release and deadline dates remain undecided.

All seven final local packages and the combined package pass the offline audit;
all 12 regression tests pass. The final review covered all 420 keys, notation,
feedback, and minimal repairs. The original Canvas identities remain intact.
Seven ready-to-paste student instruction blocks are saved in
`canvas_instructions/`; QTI import does not reliably preserve those descriptions.

The earlier combined import completed at 12:43 PM, before the final notation
and feedback repairs. **The final corrected overwrite import is not verified.**
Do not infer success from a prepared import form or a mouse click. Browser focus
changed during the attempted final import. Before retrying, check Import Course
Content for a later completed job to avoid a duplicate import.

The last saved quiz read-back showed the following existing records, each
unpublished, with 60 questions, 3 points, unlimited attempts/highest score,
Participation and Practice assignment group, and no assigned dates. These are
the targets to update, not a reason to create new copies.

| Core | Existing Canvas quiz | Description / module / schedule |
| --- | --- | --- |
| Logic | https://canvas.du.edu/courses/213452/quizzes/277965 | Final instructions, placement, and dates pending |
| Arguments | https://canvas.du.edu/courses/213452/quizzes/277966 | Final instructions, placement, and dates pending |
| Sets | https://canvas.du.edu/courses/213452/quizzes/277960 | Final instructions, placement, and dates pending |
| Proofs | https://canvas.du.edu/courses/213452/quizzes/277968 | Final instructions, placement, and dates pending |
| Divisibility | https://canvas.du.edu/courses/213452/quizzes/277962 | Final instructions, placement, and dates pending |
| Induction | https://canvas.du.edu/courses/213452/quizzes/277970 | Final instructions, placement, and dates pending |
| Counting | https://canvas.du.edu/courses/213452/quizzes/277964 | Final instructions, placement, and dates pending |

At the stopping check, no open Chrome tab was a Canvas editing page or import
form. There are no known unsaved Canvas content edits. Local sources and the
generated ZIP are saved; the final generator/HTML/checklist changes are a local
checkpoint and still need their next GitHub push and Overleaf synchronization.

Resume in this order: verify/import the final ZIP once; paste and save the seven
instruction blocks; inspect True/False/third-choice samples and complex notation
in instructor editing mode; place quizzes beside the relevant Core materials;
obtain an approved release/due-date plan; read back and publish only when ready.
Do not use Student View, change course publication, invent dates, or publish
private keys. This is a safe pause, not a completed live quiz rollout.

## Expected quizzes

| Core | Exact Canvas title |
| --- | --- |
| Logic | Core Practice — Logic Syntax and Definitions |
| Arguments | Core Practice — Arguments Syntax and Definitions |
| Sets | Core Practice — Sets Syntax and Definitions |
| Proofs | Core Practice — Proofs Syntax and Definitions |
| Divisibility | Core Practice — Divisibility Syntax and Definitions |
| Induction | Core Practice — Induction Syntax and Definitions |
| Counting | Core Practice — Counting Syntax and Definitions |

Each quiz has **60 multiple-choice questions, 0.05 point each, 3 points total**, with unlimited attempts encoded as `cc_maxattempts=-1`. The fixed choices are **True**, **False**, and **Not a truth-evaluable proposition as written**. Each quiz has 20 correct answers of each kind. Choice shuffling is disabled. Every question includes its key and explanation as feedback for both correct and incorrect responses; every third-choice answer also includes a minimal repair. Prompts use portable Unicode rather than raw TeX.

The combined ZIP contains seven independent QTI resources under `CoreName/assessment.xml`. Its assessment XML is byte-identical to the corresponding single-Core package and current generator output. All **182 assessment/resource/question/response/feedback identifiers per Core** match the original imports. The durable map is `core_syntax_canvas_identifiers.json`, explicitly tied to course **213452**; it contains no student records.

## Chrome import

- [ ] Confirm the destination is **COMP 2300, course 213452**. Check existing quiz/submission state before overwriting an item that students may have attempted.
- [ ] In course Settings → Import Course Content, choose **QTI .zip file** and the combined ZIP above.
- [ ] Enable **Overwrite assessment content with matching IDs**. Leave **Convert content to New Quizzes** off so the existing Classic Quiz records can be updated.
- [ ] Start the import once. Wait for its completed status; inspect any warnings before retrying. A completed import alone does not prove every setting survived.
- [ ] Confirm there is one intended active quiz for each title above, with no duplicate active copy. Preserve unused/legacy records unpublished; do not delete them.

## Read back each saved quiz

- [ ] Title matches; Questions shows **60 questions / 3 points**, with **0.05** on individual questions.
- [ ] It is a graded, autograded quiz in **Participation and Practice**, not an ungraded survey or a Core mastery-score assignment. Keep the highest attempt. Unlimited attempts is enabled in the live settings.
- [ ] Inspect Questions in instructor editing mode: three correctly rendered choices; answer selection and explanatory feedback present; include at least one True, False, and third-choice item. Do not enter Student View or create/use a Test Student.
- [ ] Enable the intended post-submission response/feedback visibility so students can learn from the explanations. Check that answer-choice shuffling remains off.
- [ ] Apply the approved due/available-from dates and section assignments. Dates, section overrides, highest-attempt policy, assignment group, feedback visibility, module placement, and publication state are **not guaranteed by this QTI package**. Do not guess when course sources disagree. Use an available-until date only where the approved policy requires it.
- [ ] Put the quiz beside the relevant Core materials in the correct published module. Publish scheduled student practice only after settings are verified; retain intentional banks/instructor material unpublished. Do not change the course's publication state or add module prerequisites.
- [ ] Save, reopen, and read back the settings immediately. Record the live quiz URL, module, dates, and publication status in the course audit. Close obsolete editing tabs only after confirming the save.

## Rebuild and offline checks

Run from the repository root:

```sh
python3 2300/homework_templates/generate_core_syntax_qti.py
python3 2300/homework_templates/audit_core_syntax_qti.py
python3 2300/homework_templates/test_core_syntax_qti.py
```

Normal builds use the saved course-213452 identities without Downloads. The audit checks all seven single packages plus the combined ZIP; 12 regression tests check reproducibility, saved-ID reuse, explicit clean-course IDs, corruption detection, conflicting identity options, and notation/feedback conversion. **Do not use `--new-identifiers` to update this course**: that option intentionally produces a separate stable identity set for clean-course imports. Retest and refresh the checksum after changing content.
