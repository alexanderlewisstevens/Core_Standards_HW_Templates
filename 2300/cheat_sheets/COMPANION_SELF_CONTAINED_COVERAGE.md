# Self-contained Core companion coverage

Local review completed October 29, 2026. All seven revised TeX sources and their
stable companion PDFs are saved in this repository. These are representative
study guides, not exhaustive solutions to every problem in the assessment banks.

Every row below has been checked for a complete **Problem**, a matching **Worked
solution**, and an explicit **Answer or conclusion**. Checks include the stated
domain, necessary assumptions, intermediate steps, and final result. Existing
definitions, methods, common mistakes, and readiness checks remain.

An **Exact** mapping preserves the assessment's problem number and mathematical
task; explanatory wording may be expanded. A **Similar** mapping is explicitly
labeled as a similar example in the companion and is not presented as an exact
assessment question. Section letters without an exact problem number identify
the skill being practiced.

## Delivery and build checks

| Core | Example groups | Pages | TeX source in this directory | Stable PDF in `companion_pdfs/` |
|---|---:|---:|---|---|
| Logic | 12 | 5 | `logic_core_companion.tex` | `logic_core_companion.pdf` |
| Arguments | 21 | 8 | `arguments_core_companion.tex` | `arguments_core_companion.pdf` |
| Sets | 15 | 5 | `sets_core_companion.tex` | `sets_core_companion.pdf` |
| Proofs | 17 | 4 | `proofs_core_companion.tex` | `proofs_core_companion.pdf` |
| Divisibility | 22 | 6 | `divisibility_reference_and_worked_examples.tex` | `divisibility_core_companion.pdf` |
| Induction | 9 | 4 | `induction_core_companion.tex` | `induction_core_companion.pdf` |
| Counting | 24 | 5 | `counting_core_companion.tex` | `counting_core_companion.pdf` |
| **Total** | **120** | **37** | | |

Example groups count a multi-part problem once. Induction C.1 is one problem
whose solution spans two explicitly labeled boxes. Inline solved examples in
definition/method boxes are included in the inventory.

- [x] Compared examples with the current assessment sources in
  `../core_assessments/`; used the selected Arguments assessment and compact
  three-part Induction assessment.
- [x] Preserved the existing examples. Previously combined tasks have separate
  complete prompts where needed; no fixed four-page limit remains in current
  companion instructions.
- [x] Compiled all seven with TeX Live 2025, pdfTeX
  `3.141592653-2.6-1.40.27`, and `latexmk` 4.86a.
- [x] Final TeX logs contain no warnings, errors, overfull boxes, or underfull
  boxes.
- [x] Inspected every rendered page: 37 US-letter pages total. Checked columns,
  table/diagram readability, continuation labels, page boundaries, and clipping.
- [x] Replaced all seven stable PDF copies and verified their bytes match the
  final builds. Filenames are unchanged.
- [x] Saved source/PDF SHA-256 identities in
  `companion_pdfs/BUILD_MANIFEST.json`.

Build scratch files, logs, and page renders are under
`../../output/self-contained-companions/` relative to this directory (repository-root
`output/self-contained-companions/`). They are not student deliverables.

## Logic — 12 example groups

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Complete truth table | Exact A.3 | Explicit task; all eight truth assignments and intermediate columns; tautology conclusion |
| 2 | Interpreting one row | Similar, A skills | Assigned truth values, requested formulas, row calculation, result |
| 3 | Conditional translation | Similar, B skills | Full natural-language condition and requested symbolic statement |
| 4 | Quantifiers and argument order | Similar, B skills | Predicate meanings, variable domains, quantifier order, interpretation |
| 5 | Complete negation | Exact C.1(a) | Original quantified statement, domain, requested negation, equivalent final form |
| 6 | Nested negation | Exact C.2(b) | Full nested statement, domain, quantifier reversal and predicate negation |
| 7 | Inconsistency and minimality | Exact D.1 | All premises, contradiction, and witnesses after removing each premise |
| 8 | One satisfying witness | Similar, D.2 conditions | Requests one model rather than all models; values and premise checks |
| 9 | Minimal contradiction | Similar, D skills | Entire formula set, contradiction, proper-subset witnesses |
| 10 | Factor a common term | Exact E.1 | Starting/target expressions, named equivalence steps, conclusion |
| 11 | De Morgan structure | Exact E.2 | Starting/target expressions, named equivalence steps, conclusion |
| 12 | Nested implication | Exact E.5 | Complete equivalence task, legal transformation steps, final expression |

## Arguments — 21 example groups

All examples are **Similar** examples of types in the current selected assessment,
not verbatim assessment items. Every B–D example contains its complete passage
and five answer choices. Its required assessment response is the selection only;
the longer explanation is labeled as teaching material. A/E specify brief
responses and show a short acceptable answer separately from explanation.

| # | Example | Skill/type | Complete content checked |
|---:|---|---|---|
| 1 | Archive recovery | A.1 conclusion structure | Full passage; main/intermediate conclusions; brief response |
| 2 | Access, training, and supervision | A.2 formalization | Complete conditions, symbol meanings, biconditional formulation |
| 3 | Stale cache | A.3 countermodel | Entire argument, valuation, premises true/conclusion false |
| 4 | Clinic | B.1 main conclusion | Passage, five choices, selection, teaching explanation |
| 5 | Digitization | B.2 concession role | Passage, five choices, selection, teaching explanation |
| 6 | Random sample | B.3 disagreement | Both speakers, five choices, selection, teaching explanation |
| 7 | Certified, inspected, and sealed | B.4 must follow | All conditions, five choices, selection, teaching explanation |
| 8 | Pump and valve | B.5 parallel reasoning | Original argument, five candidate arguments, selection, explanation |
| 9 | Latest backup | C.1 necessary assumption | Passage, five choices, negation test, selection |
| 10 | Unique feasible plan | C.2 sufficient principle | Passage, five principles, sufficiency reasoning, selection |
| 11 | Benches and attendance | C.3 causal flaw | Passage, five choices, selection, teaching explanation |
| 12 | High-contrast labels | C.4 strengthen | Passage, five choices, selection, teaching explanation |
| 13 | Tutorial | C.5 weaken | Passage, five choices, selection, teaching explanation |
| 14 | Fee waiver | D.1 principle application | Full case, five principles, selection, teaching explanation |
| 15 | Registrations and no-shows | D.2 discrepancy | Both observations, five explanations, selection, explanation |
| 16 | Certified device and oak | D.3 parallel flaw | Full original argument and five candidate arguments; selection and explanation |
| 17 | Deadline counterexample | D.4 method | Entire exchange, five choices, selection, teaching explanation |
| 18 | Early riders | D.5 completion | Passage and blank, five completions, selection, explanation |
| 19 | Reminders | E.1 causal test | Complete claim/evidence, requested test, short acceptable response |
| 20 | Screen and independent corroboration | E.2 principle | Full situation and requested distinction, short acceptable response |
| 21 | Bus lane | E.3 conclusion and revision | Complete passage, requested conclusion/revision, short acceptable response |

## Sets — 15 example groups

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Finite construction | Similar; uses A.5 sets | All sets and membership task; explicitly differs from the assessment task |
| 2 | Union and difference Venn region | Exact B.1 | Universe, sets, expression, actual shaded solution |
| 3 | Conditional Venn region | Exact B.3 | Universe, sets, logical condition, actual shaded solution |
| 4 | Biconditional Venn region | Exact B.5 | Universe, sets, logical condition, actual shaded solution |
| 5 | Reading a relation plot | Similar, C skills | Actual labeled plot, axes, domain/codomain, full reading task |
| 6 | Quantified relation statements | Similar, C skills | Relation definition, domains, complete quantified statements |
| 7 | Diagnosing a nonfunction | Similar, C skills | Entire relation and domain/codomain; failed uniqueness condition |
| 8 | Finite images, preimages, and classification | Exact D.1 | Mapping, sets, requested images/preimages and classification |
| 9 | Integer formula | Exact D.2 | Formula, integer domain/codomain, requested classifications and witnesses |
| 10 | Domain and codomain matter | Similar, D skills | Both functions' domains/codomains and comparison task; not full D.3/D.5 |
| 11 | Image of a union | Exact E.1 | Full theorem, function/set assumptions, element proof |
| 12 | Image of an intersection | Exact E.2 | Claimed relation, hypotheses, inclusion and strictness example |
| 13 | Preimage preserves intersection | Exact E.3 | Full identity, function/set assumptions, membership equivalences |
| 14 | Product distributes over union | Exact E.4 | Full identity, arbitrary sets, ordered-pair membership argument |
| 15 | False cancellation claim | Exact E.5 | Complete implication, counterexample sets, verification |

## Proofs — 17 example groups

All theorems are stated before proof. Faulty arguments are reproduced before
diagnosis and repair. Inference rules distinguish universal instantiation from
existential instantiation, including the fresh-witness restriction.

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Propositional derivation | Exact A.4 | All premises, target conclusion, named inference steps |
| 2 | Quantifier derivation | Exact A.5 | Full quantified premises/target; arbitrary element, UI/MP/UG |
| 3 | Reused-witness countermodel | Exact A.3 | Faulty inference, quantified premises, countermodel and explanation |
| 4 | Even square | Exact B.1 | Theorem, integer domain, definition of even, witness |
| 5 | Odd plus odd | Exact B.3 | Theorem, integer domain, both odd witnesses, even witness |
| 6 | Rational sum | Exact B.2 | Theorem, rational representations, nonzero denominator |
| 7 | Subset intersection | Exact B.5 | Complete set theorem, hypotheses, element proof |
| 8 | Odd product | Exact C.1 | Theorem and contrapositive, parity witness, conclusion |
| 9 | No largest integer | Exact C.3 | Theorem, contradiction assumption, larger integer |
| 10 | Rational plus irrational | Exact C.4 | Theorem, contradiction assumption, rational closure steps |
| 11 | Parity cases | Exact D.1 | Integer theorem, exhaustive parity cases, conclusion |
| 12 | Four consecutive composites | Exact D.3 | Existence claim, four consecutive integers, factor witnesses |
| 13 | Two counterexamples | Exact D.4, both parts | Irrational-sum claim and prime-polynomial claim, complete counterexamples |
| 14 | Witness repair | Exact E.2 | Original faulty argument, illegal witness reuse, corrected result |
| 15 | Division by zero | Exact E.3 | Entire faulty calculation, invalid division, repair/conclusion |
| 16 | Circular proof | Exact E.4 | Original argument, circular step, independent repair |
| 17 | Bad starting element | Exact E.5 | Original proof, invalid chosen element, arbitrary-element repair |

## Divisibility — 22 example groups

All computations identify their integer inputs, positive divisors/moduli, and
requested residue conventions. Base-conversion examples state the base and digit
meaning. Proofs state integer domains and exhibit integer witnesses.

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Positive dividend: 263 divided by 17 | Similar, A skills | Quotient, canonical remainder, div/mod/congruence, justification |
| 2 | Negative dividend: -52 divided by 9 | Similar, A skills | Canonical quotient/remainder, legal bound, div/mod/congruence |
| 3 | Recover a number | Exact A.4 | Given div/mod values and divisor, reconstruction and remainder bound |
| 4 | Test a congruence | Exact A.5 | Both integers and modulus, definition check, least nonnegative residue |
| 5 | Decimal 1000 to hexadecimal | Exact B.4 | Repeated division, digit values, place-value verification |
| 6 | Decimal 202 to binary | Similar, B skills | Quotients/remainders, reverse digit order, powers-of-two check |
| 7 | Base-five 2301 | Similar, supplemental | Base/digits, expansion, decimal result, legality check |
| 8 | Octal 725 to binary and decimal | Exact B.3 | Input base, all digit groups, decimal verification |
| 9 | Binary 101101011 to octal and hexadecimal | Exact B.5 | Input base, requested outputs, grouping rule, answers |
| 10 | Hexadecimal 2D7 to binary and octal | Similar, B skills | D = 13, grouping/padding instructions, decimal check |
| 11 | Last two base-seven digits of 25314 | Similar, supplemental | Modulus 7 squared, no full decimal conversion, residue interpretation |
| 12 | Reduce (-47 times 38 + 19) modulo 12 | Similar, C skills | Entire expression, modulus, least nonnegative residue |
| 13 | 3 to the 47th power modulo 10 | Exact C.1(b) | Requested residue and cycle method, exponent reduction |
| 14 | 5 to the 117th power modulo 13 | Exact C.4 | Repeated-squaring task, displayed powers, product and residue |
| 15 | Euclidean algorithm and Bezout for 246 and 102 | Similar, D skills | Inputs, gcd task, coefficient identity, back-substitution and verification |
| 16 | Relative primality of 16 and 45 | Similar, supplemental | Prime-factorization task, gcd calculation and conclusion |
| 17 | Divisibility and linear combinations | Exact E.1 | All integer variables and hypotheses, definition-driven proof |
| 18 | A modulus that factors | Similar, supplemental | Positive factors and integer domain, both requested congruences; primality question |
| 19 | Products preserve congruence | Exact C.5 | Both congruence hypotheses, integer modulus, full witness proof |
| 20 | Odd squares modulo 8 | Exact E.2 | Odd-integer hypothesis, target congruence, extra factor of two |
| 21 | Transitivity of divisibility | Exact E.3 | All integer variables, distinct witnesses, conclusion |
| 22 | Three consecutive integers | Exact E.5 | Arbitrary starting integer, divisibility by 6, factors 2 and 3 combined |

The relative-primality example is supplemental; it is not mislabeled as exact
D.4 or D.5 (which use different integer inputs).

## Induction — 9 example groups

The compact A/B/C assessment is the reference. A.1 remains a setup task, not a
request to finish the proof. C.1 reproduces the full binomial-sum statement and
the supplied Pascal/endpoint identities. Its continued solution is explicitly
labeled and addresses the empty interior sums when k = 0.

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Prime-factorization induction setup | Exact A.1 | Full statement, domain, all four setup tasks, instruction not to complete proof |
| 2 | Odd-sum induction plan | Similar, A skills | Full sum identity, starting index, base/hypothesis/target |
| 3 | Circular exponential argument | Exact B.1 | Entire faulty proof, diagnosis, legal replacement argument |
| 4 | Wrong next term in an odd sum | Similar, B skills | Full claim and faulty step, corrected new term and step |
| 5 | Two-base recurrence | Similar, supplemental | a0/a1, recurrence for n at least 2, full target, two bases and step |
| 6 | Binomial sum | Exact C.1 | Full identity/domain and supplied identities; base, hypothesis, reindexing, endpoints, conclusion; labeled continuation |
| 7 | 3 divides 4 to the nth power minus 1 | Similar | n at least 0, divisibility statement, base, integer witness and step |
| 8 | Finite arithmetic sum | Similar | Full sum formula, n at least 1, base, hypothesis, algebra and conclusion |
| 9 | Factorial inequality | Similar | Full inequality, n at least 1, base and justified multiplicative step |

## Counting — 24 example groups

Every entry is an **Exact** task from the current Counting assessment. Ordered
versus unordered models, replacement, uniform selection, independence, and all
probability givens are explicit wherever needed.

| # | Example | Assessment mapping | Complete content checked |
|---:|---|---|---|
| 1 | Disjoint alternatives | Exact A.1 | Soup/salad counts, exactly one choice, requested rule and count |
| 2 | Successive positions | Exact A.2 | Letter/digit counts, length, repetition allowed, product |
| 3 | Functions | Exact A.3 | Full finite domain/codomain, arbitrary functions, requested count |
| 4 | Overlap | Exact A.4 | Both cardinalities/intersection, union task and identity |
| 5 | Hash buckets | Exact A.5 | 40 keys/20 values, guaranteed occupancy, optimality explanation |
| 6 | Committees | Exact B.1 | Pool and committee sizes, unordered selection, expression and reason |
| 7 | Labeled offices | Exact B.2 | Two distinct offices, ten candidates, no double office, expression |
| 8 | Repeated letters | Exact B.3 | Complete word BANANA, indistinguishable repeats, expression and result |
| 9 | Choosing positions | Exact B.4 | Eight bits/exactly three ones, selection model and result |
| 10 | Binomial coefficient | Exact B.5 | Full polynomial, requested power, determining term and coefficient |
| 11 | Exact hearts | Exact C.1 | Standard deck composition, unordered hand, no replacement, exact event |
| 12 | Count by complement | Exact C.2 | Length eight/at least two ones, forbidden cases and count |
| 13 | Mixed committee | Exact C.3 | Disjoint major pools, group size, exact composition, product |
| 14 | Injective functions | Exact C.4 | Domain/codomain cardinalities, injectivity restriction, ordered count |
| 15 | First-position code rule | Exact C.5 | Six letters, uppercase alphabet, specified vowels, no repetition |
| 16 | Coin and die | Exact D.1 | Fair independent devices, inclusive-or event, favorable count |
| 17 | Probability identities | Exact D.2 | All three givens, both requested events, union/complement calculations |
| 18 | Uniform bit strings | Exact D.3 | Uniform sample from all 256 strings, exactly three ones, exact probability |
| 19 | Without replacement | Exact D.4 | Four red/six blue, two sequential uniform draws, ordered event |
| 20 | Two different conditionals | Exact D.5 | Both usage counts and overlap, uniform student, both conditional events |
| 21 | Numerical independence test | Exact E.1 | All probabilities, equality test, requested conditional probability |
| 22 | Screening and base rates | Exact E.2 | Prevalence, both test-positive rates, both requested probabilities and interpretation |
| 23 | Factory Bayes model | Exact E.3 | Both supply shares/defect rates, uniform stocked battery, observed defect |
| 24 | Expected net value | Exact E.4 | Fair die, complete payout schedule, entry cost, net expectation and sign |

Aggregation reversal remains a definition/method box, as before; it did not
contain a numerical worked example. No claim is made that E.5 has a worked
companion example.

## Build-review boundary

This build review is complete. It covers the seven companion sources and stable
PDFs, not assessment banks, Canvas records/settings, practice-quiz publication,
Obsidian pages, or announcements. All seven practice quizzes were left untouched
and unpublished; their live status was not re-audited in this document pass.

Alex approved GitHub/Overleaf synchronization on 2026-10-29. Remote delivery is
verified separately from this build record; Canvas uploads and Obsidian
publication remain outside this revision.
