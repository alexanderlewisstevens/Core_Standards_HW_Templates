# Core syntax practice: import and verification

Local audit: **2026-10-28 — passed.** This records package readiness, not proof of a successful live Canvas import or student access.

Combined upload: `output/qti/Core_All_Syntax_Practice_Canvas_QTI.zip` (repository root).

SHA-256: `6409390dcca0cb93cbf351ce0bcd67bffadecc810aba83b4cbb6d2f7e99325da`

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

Normal builds use the saved course-213452 identities without Downloads. The audit checks all seven single packages plus the combined ZIP; four regression tests check reproducibility, saved-ID reuse, explicit clean-course IDs, corruption detection, and conflicting identity options. **Do not use `--new-identifiers` to update this course**: that option intentionally produces a separate stable identity set for clean-course imports. Retest and refresh the checksum after changing content.
