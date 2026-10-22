---
title: Arguments Core Solutions
aliases: [2300 Arguments Solutions, Arguments Solutions, Arguments Core Solutions]
linter-yaml-title-alias: Arguments Core Solutions
date created: Saturday, September 5th 2026, 10:08:45 pm
date modified: Wednesday, October 21st 2026
publish: true
permalink: core-assessment-solutions/2300-arguments-solutions
---
# Arguments Core Solutions

These are complete worked solutions to the public **Arguments Core Extended Practice** bank.
They are not answer keys to a live form; supervised paper forms use new scenarios
from the same problem families.

A live attempt lasts 20 minutes and contains five scoring units, one from each
section A–E. Meets is four of five fully correct; Exceeds is five of five.
For a multiple-choice problem, the selected letter and its justification must
both be correct.

All passages, scenarios, choices, and explanations are original course material.
No official LSAC or LawHub question is reproduced.

## Full-credit and grader guidance

The worked responses below are models, not the only acceptable wording. A
different response earns full credit when it makes every requested judgment,
supports each judgment with the passage, and performs the reasoning named in
the prompt. For multiple-choice problems, the student must give both the
correct letter and a brief justification that distinguishes it from the most
plausible distractor. A correct letter alone is not a complete response.

The **decisive check** listed for each section is a fast way for a grader to
locate the central reasoning move. It does not waive any requested part of the
problem: under the course mastery rule, a response with a missing requested
part is not fully correct.

## A. Reconstruct and Challenge Natural-Language Arguments

> [!CHECK]- Minimum full-credit response and decisive checks
> - **A.1:** Identify the main conclusion, any intermediate conclusion, the stated premises, the support structure, and a plausible bridge premise. Equivalent argument maps are acceptable. **Decisive check:** the response distinguishes the claim being supported from a claim that merely supports it.
> - **A.2:** State the rules, translate each relevant rule in the correct direction, identify necessary and sufficient conditions, give a valid contrapositive when requested, and reject an unsupported converse. **Decisive check:** arrows point in the direction licensed by the text.
> - **A.3:** Give a numbered or equally clear formal reconstruction, judge validity, name the valid rule or provide a countermodel, and make the requested minimal repair. **Decisive check:** for an invalid argument, the countermodel makes every premise true and the conclusion false.

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.1_Propositional_Logic|Rosen §1.1 — Propositional Logic]]
> - [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|Rosen §1.2 — Applications of Propositional Logic]]
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen §1.6 — Rules of Inference]]
> - [1.2 Intro to Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntroHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntro.11.19.mp4)
> - [1.4b More on Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisitedHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisited.4.06.mp4)
> - [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)

### A.1 Argument Structure

Identify how the claims fit together rather than merely listing them.

#### A.1.01

> [!NOTE]- Solution
> **Main conclusion:** The team should archive a build log for every release.
>
> **Intermediate conclusion:** Archived build logs can be audited after a failure.
>
> **Stated premises:**
> 1. Archived build logs receive automatic timestamps.
> 2. Any record with a trustworthy timestamp can be audited after a failure.
> 3. An auditable release process makes debugging more reliable.
>
> Premises 1 and 2 form a short chain: archived log $\rightarrow$ trustworthy timestamp $\rightarrow$ auditable after a failure. That chain establishes the intermediate conclusion. The intermediate conclusion and premise 3 then support the recommendation, but they do not deductively entail it without a value or policy premise.
>
> One plausible bridge premise is: **If an affordable recordkeeping practice makes every release auditable and thereby makes debugging more reliable, the team should adopt that practice for every release.** With that bridge in place, the recommendation follows. Notice that premise 3 does not itself prove that the team should archive logs; it explains why auditability is valuable.

#### A.1.02

> [!NOTE]- Solution
> The main conclusion is that the city should place its next three docks beside rail stations. The intermediate conclusion is that placing docks near rail stations increases bike-share use. The stated premises concern where trips begin or end, the higher use of comparable station-area docks, and the city's goal of increasing bicycle-transit combinations. The first two premises support the intermediate causal claim; that claim and the stated goal support the recommendation. A bridge is that, other relevant costs being comparable, the city should choose dock locations that advance its stated transportation goal.

#### A.1.03

> [!NOTE]- Solution
> The main conclusion is that the course should add accurate captions before assigning the videos. The intermediate conclusion is that uncaptioned tutorial videos do not satisfy the accessibility rule. The premises are that such videos cannot be used fully by every student and that material some students cannot use fully violates the rule. Those premises jointly support the intermediate conclusion. A bridge to the recommendation is that a course should not assign material that violates the accessibility rule when adding accurate captions would make it compliant.

#### A.1.04

> [!NOTE]- Solution
> The main conclusion is that every nonemergency bug report should require repeatable steps. The intermediate conclusion is that reports containing such steps make causes easier to isolate. The first two statements form a chain from repeatable steps to reproduction to easier isolation. The statement that faster diagnosis shortens outages is an additional premise. A bridge is that easier isolation produces faster diagnosis and that requirements which reduce outages at reasonable cost should be adopted.

#### A.1.05

> [!NOTE]- Solution
> The main conclusion recommends planting canopy trees along the busiest walking routes. The intermediate conclusion is that increasing street shade can reduce pedestrian heat risk. The measurement about shaded blocks and the premise connecting lower temperatures to lower risk support that intermediate conclusion. The lack of existing shade is a further premise. A bridge is that canopy trees will materially increase shade on those routes and are an acceptable way to reduce a significant pedestrian risk.

#### A.1.06

> [!NOTE]- Solution
> **Main conclusion:** The development team should require each feature to be committed in focused steps.
>
> **Intermediate conclusion:** Small commits reduce recovery time after a defect.
>
> **Stated premises:**
> 1. Focused commits make it possible to reverse one change without discarding unrelated work.
> 2. Selective reversal shortens recovery after a defect.
>
> The support is serial rather than independent: focused commits enable selective reversal, and selective reversal shortens recovery. Together those claims support the intermediate conclusion. The intermediate conclusion then supports the policy recommendation.
>
> Two small bridges are implicit. First, committing a feature in focused steps produces the relevant kind of small commits. Second, **when a feasible development practice materially shortens recovery without a comparable cost, the team should require it.** Without that normative bridge, the passage establishes a benefit but not yet a requirement.

#### A.1.07

> [!NOTE]- Solution
> The main conclusion recommends delaying the northbound departure by five minutes. The intermediate conclusion is that the shift would make the connection reliable on most days. The premises describe the current missed connection, the effect of the proposed shift, and the travel-time benefit of reliable connections. A bridge is that the small schedule cost does not outweigh the substantial reduction in connection waits, so the agency should implement the change.

#### A.1.08

> [!NOTE]- Solution
> The main conclusion is that the clinic should keep one daily backup offline. The intermediate conclusion is that an offline backup protects restoration ability. The premises say the attack cannot encrypt the offline copy and an unencrypted copy can restore records. A bridge is that a daily offline copy will be recent enough to provide meaningful restoration and that the clinic should take a feasible step that protects essential records.

#### A.1.09

> [!NOTE]- Solution
> The main conclusion recommends extending finals-week hours. The intermediate conclusion is that the pilot addressed a demonstrated need. Heavy pilot use and the general statement about heavy use during peak demand support that intermediate conclusion. The claim that an extra hour would continue the service is another premise. A bridge is that, absent prohibitive cost or harm, a library should continue a service shown to meet a demonstrated finals-period need.

#### A.1.10

> [!NOTE]- Solution
> The main conclusion is that the utility should initially offer real-time meters in buildings with aging plumbing. The intermediate conclusion is that the meters can reduce water lost to leaks. The first two premises form a chain from real-time feedback through earlier detection to prevented loss. A bridge is that aging plumbing creates a comparatively high leak risk and that prioritizing a scarce intervention where expected benefit is greatest is justified.

### A.2 Hidden Conditionals

Translate each rule exactly. Do not assume its converse.

#### A.2.01

> [!NOTE]- Solution
> The rules are E → T, T → E, and E ↔ (T ∧ S). Training is necessary for entry in the first rule and sufficient in the second. In the third, both training and supervision are necessary for entry, while their conjunction is sufficient. The contrapositive of E → T is ¬T → ¬E. Its converse T → E does not follow from the first rule because another requirement could still block a trained student.

#### A.2.02

> [!NOTE]- Solution
> The rules are V → P, (P ∧ R) → V, and V → R. Patching is necessary for removal; patching together with restart is sufficient; restart is also necessary for removal. The contrapositive of V → P is ¬P → ¬V. The converse P → V is not licensed: the server may also need to restart.

#### A.2.03

> [!NOTE]- Solution
> Let $M$ mean “the member may vote,” $D$ mean “dues are current,” and $A$ mean “the member attended orientation.”
>
> 1. “Only members with current dues may vote” translates as $M \rightarrow D$. The word **only** introduces a necessary condition: voting permission requires current dues.
> 2. “Current dues are enough to vote unless orientation was missed,” under the problem’s instruction to treat this as requiring attendance, translates as $(D \land A) \rightarrow M$.
> 3. “A member may vote if and only if dues are current and orientation was attended” translates as $M \leftrightarrow (D \land A)$, which abbreviates both $M \rightarrow (D \land A)$ and $(D \land A) \rightarrow M$.
>
> Thus $D$ and $A$ are each **necessary** for $M$, while their conjunction $D \land A$ is **sufficient** for $M$. Neither $D$ nor $A$ alone is sufficient. The contrapositive of the first rule is $\neg D \rightarrow \neg M$: if dues are not current, the member may not vote. The common mistake is to reverse the first rule and claim $D \rightarrow M$; orientation is still required.

#### A.2.04

> [!NOTE]- Solution
> The rules are B ↔ (C ∨ L), C → B, and B → (C ∨ L). The first biconditional is exactly the conjunction of the latter direction B → (C ∨ L) with the sufficient directions C → B and L → B. The contrapositive of C → B is ¬B → ¬C. From B alone one cannot infer C, because L could be the copy that provides backup.

#### A.2.05

> [!NOTE]- Solution
> The rules are G → C, C ∧ ¬F → ¬G (equivalently, G → (C ∧ F) in this policy context), and (C ∧ F) → G. Thus C and F are individually necessary for graduation, and their conjunction is sufficient. The contrapositive of G → C is ¬C → ¬G. Neither C nor F alone is sufficient.

#### A.2.06

> [!NOTE]- Solution
> The rules are U → N, N → (H ∨ U), and H → N. U and H are each sufficient for N. Their disjunction is necessary for N. The contrapositive of N → (H ∨ U) is (¬H ∧ ¬U) → ¬N. N does not imply H by itself because urgent mode may be responsible.

#### A.2.07

> [!NOTE]- Solution
> The translations are A → I, (I ∧ R) → A, and (¬I ∨ ¬R) → ¬A. The last rule is equivalent by contraposition and De Morgan to A → (I ∧ R). Therefore I and R are each necessary for A, and their conjunction is sufficient. Neither is sufficient alone.

#### A.2.08

> [!NOTE]- Solution
> Let $O$ mean “the event is held outdoors,” $W$ mean “the forecast is dry,” and $P$ mean “a permit is approved.”
>
> 1. “Outdoor events require an approved permit” is $O \rightarrow P$.
> 2. “A dry forecast does not by itself guarantee an outdoor event” says that $W \rightarrow O$ is **not** an accepted rule; write $W \nrightarrow O$.
> 3. “The event is held outdoors exactly when both the forecast is dry and the permit is approved” is $O \leftrightarrow (W \land P)$.
>
> The biconditional yields $O \rightarrow W$, $O \rightarrow P$, and $(W \land P) \rightarrow O$. Therefore, $W$ and $P$ are individually necessary for $O$, while $W \land P$ is sufficient. Neither condition alone is sufficient. The contrapositive of the permit requirement is $\neg P \rightarrow \neg O$. A dry forecast by itself leaves open the possibility that the permit was denied, so it cannot establish $O$.

#### A.2.09

> [!NOTE]- Solution
> The rules can be written (X ∧ K) → D, (X ∧ D) → K, and, restricted to encrypted messages, X → (D ↔ K). D alone does not imply X because an unencrypted message can also be decoded. From (X ∧ K) → D, a useful contrapositive is ¬D → (¬X ∨ ¬K); with X assumed, this reduces to (X ∧ ¬D) → ¬K.

#### A.2.10

> [!NOTE]- Solution
> The translations are R → E, E ↛ R, and R ↔ (E ∧ F). The biconditional makes E and F individually necessary and E ∧ F sufficient. It also explains why eligibility alone is not sufficient. The contrapositive of R → E is ¬E → ¬R.

### A.3 Validity, Countermodels, and Repair

Rewrite each argument in numbered premise/conclusion form. If valid, name the rule; if invalid, give a true-premise/false-conclusion countermodel and a minimal repair.

#### A.3.01

> [!NOTE]- Solution
> Let P mean the patch is installed, R the server restarts, V the vulnerability is removed, and A the audit passes. Numbered form: (1) (P ∧ R) → V; (2) V → A; (3) P; (4) R; conclusion: A. Conjoin (3) and (4), use modus ponens with (1) to derive V, and use modus ponens with (2) to derive A. The argument is valid.

#### A.3.02

> [!NOTE]- Solution
> Let B mean the badge is active, U the door unlocks, and D the desk receives an alert. Numbered form: (1) B → (U ∨ D); (2) ¬U; (3) ¬D; conclusion: ¬B. Premises (2) and (3) imply ¬(U ∨ D) by De Morgan's law. Modus tollens with (1) then yields ¬B. The argument is valid.

#### A.3.03

> [!NOTE]- Solution
> Let P mean the parser rejects the file, A the compiler accepts it, and S the schema is valid. Numbered form: (1) (P ∨ A) ∧ ¬(P ∧ A); (2) A → S; (3) ¬S; conclusion: P. From (2) and (3), modus tollens gives ¬A. The first conjunct of (1) gives P ∨ A, and disjunctive syllogism yields P. The exclusivity conjunct is accurate but not needed. The argument is valid.

#### A.3.04

> [!NOTE]- Solution
> Let C mean calibrated, S stable readings, A an active scheduler, R regular samples, and U usable readings. Numbered form: (1) C → S; (2) A → R; (3) (S ∧ R) → U; (4) C; (5) A; conclusion: U. Modus ponens gives S and R from the first two rules; conjunction gives S ∧ R; a final modus ponens gives U. The argument is valid.

#### A.3.05

> [!NOTE]- Solution
> Let $C$ mean “the cache is stale,” $F$ mean “the integration test fails,” and $M$ mean “the warning log records a mismatch.” The argument is:
>
> 1. $C \rightarrow (F \land M)$
> 2. $F$
> 3. $M$
> 4. Therefore, $C$.
>
> This is **invalid**. Premises 2 and 3 allow us to infer $F \land M$, but premise 1 says only that a stale cache is one sufficient cause of those observations. It does not say that a stale cache is their only possible cause. The inference affirms the consequent.
>
> A countermodel sets $C$ false, $F$ true, and $M$ true. Then $C \rightarrow (F \land M)$ is true because its antecedent is false, both observational premises are true, and the conclusion is false. A different defect could have caused both observations.
>
> A minimal repair is to add $(F \land M) \rightarrow C$, or equivalently replace premise 1 with $C \leftrightarrow (F \land M)$. With that additional direction, conjunction gives $F \land M$ and modus ponens gives $C$.

#### A.3.06

> [!NOTE]- Solution
> Let R mean reserved, C shown on the calendar, and N that the coordinator receives a notice. Numbered form: (1) R → C; (2) C → N; (3) ¬R; conclusion: ¬N. It is invalid by denying the antecedent of the chain. A countermodel is R=false, C=true, N=true. Replacing (2) with N → R is a minimal repair, since ¬R and N → R yield ¬N by modus tollens; alternatively, adding N → R repairs the original set.

#### A.3.07

> [!NOTE]- Solution
> Let C(x) mean certified, S(x) passed the safety test, P(x) prototype, and k denote Unit K. Numbered form: (1) ∀x(C(x) → S(x)); (2) ∀x(P(x) → ¬S(x)); (3) P(k); (4) some nonprototype is not S; conclusion: ¬C(k). From (2) and (3), derive ¬S(k); with the instance C(k) → S(k) of (1), modus tollens yields ¬C(k). The existential aside is irrelevant. The argument is valid.

#### A.3.08

> [!NOTE]- Solution
> Let L mean the lab is open, T a technician is present, S a supervisor is present, and D the incident desk is staffed. Numbered form: (1) L → (T ∨ S); (2) S → D; (3) L; (4) ¬T; conclusion: D. From (1) and (3), derive T ∨ S; with (4), disjunctive syllogism gives S; modus ponens with (2) gives D. The argument is valid.

#### A.3.09

> [!NOTE]- Solution
> Let G mean the grant is renewed, H an assistant is hired, R weekend hours are reduced, and W weekday service is preserved. Numbered form: (1) G → H; (2) ¬G → R; (3) H → W; (4) R → W; (5) G ∨ ¬G; conclusion: W. In the G case, H and then W follow; in the ¬G case, R and then W follow. The cases are exhaustive, so the argument is valid by proof by cases (a constructive dilemma followed by either branch's implication to W).

#### A.3.10

> [!NOTE]- Solution
> Let $R$ mean “the report is accurate,” $A$ mean “the sensors agree,” $C$ mean “their calibration is current,” and $K$ mean “an automatic check completed.” The argument is:
>
> 1. $R \leftrightarrow (A \land C)$
> 2. $A$
> 3. $K$
> 4. Therefore, $R$.
>
> The biconditional gives $(A \land C) \rightarrow R$, but the premises establish only $A$. Nothing connects $K$ to $C$. The word “check” may suggest current calibration in ordinary conversation, but formal evaluation may use only stated relationships.
>
> The argument is invalid. A countermodel is $R=false$, $A=true$, $C=false$, and $K=true$. In that model, $A \land C$ is false, so the biconditional $R \leftrightarrow (A \land C)$ is true; premises 2 and 3 are also true, while the conclusion is false.
>
> Add $C$ as a premise, or add $K \rightarrow C$. In the second repair, $K$ and $K \rightarrow C$ yield $C$; conjunction yields $A \land C$; then the sufficient direction of the biconditional yields $R$.

## B. Logical Reasoning I: Anatomy and Inference

> [!CHECK]- Minimum full-credit response and decisive checks
> - **B.1 Main conclusion:** Give the correct letter and explain which claim the other claims support. **Decisive check:** the chosen statement is the author's ultimate point, not evidence or a concession.
> - **B.2 Role in argument:** Give the correct letter and accurately describe how the cited claim supports, qualifies, or opposes another claim.
> - **B.3 Point at issue:** State the exact proposition one speaker accepts and the other rejects; do not merely name the topic.
> - **B.4 Must follow:** Give the correct letter and show that it is forced by the stated facts without adding an assumption.
> - **B.5 Parallel reasoning:** Give the correct letter and match the logical structure, including polarity and quantifier strength. An equivalent symbolization is acceptable.

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.1_Propositional_Logic|Rosen §1.1 — Propositional Logic]]
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen §1.6 — Rules of Inference]]
> - [1.1c Conditional Statements (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1cConditionalStatementsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1cConditionalStatements.10.10.mp4)
> - [1.2 Intro to Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntroHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntro.11.19.mp4)
> - [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)

### B.1 Main Conclusion

Select the claim the author is ultimately trying to establish, then justify your choice by describing the role of the other claims.

#### B.1.01

> [!NOTE]- Answer: C
> The author uses the time pressure on field teams, the trial result, and the purpose-sensitive principle to support the recommendation that response maps omit evacuation-irrelevant details. Choices A and D are evidence, B is a concession, and E explains the recommendation without replacing it as the passage's main conclusion.

#### B.1.02

> [!NOTE]- Answer: A
> **Why A is correct:** The passage is organized to establish a recommendation: the clinic should begin Saturday appointments next month. The remaining claims answer the two natural questions about that recommendation—whether Saturday service is needed and whether it is feasible.
>
> **Argument map:** inconvenient weekday openings plus rapidly filled evening clinics support unmet demand outside ordinary work hours. The newly hired nurse and available budget remove the two obstacles that previously defeated weekend service. Those two lines of support converge on A.
>
> **Why the others are not the main conclusion:** B and C describe evidence of need. E is one fact establishing feasibility. D is a useful intermediate conclusion synthesized from the nurse and budget facts, but the author uses that conclusion to support the further recommendation in A.

#### B.1.03

> [!NOTE]- Answer: E
> The evidence and general standard first support the intermediate judgment in D; that judgment is then used to support the specific extension recommendation in E. A is a concession, B summarizes mitigating evidence, and C is the governing principle.

#### B.1.04

> [!NOTE]- Answer: B
> The break-even and expected-use premises support B, the decision-relevant cost conclusion. A is a criticism of the vendor's framing, C and D are supporting facts, and E limits the scope of the conclusion.

#### B.1.05

> [!NOTE]- Answer: D
> D is the policy recommendation the passage is organized to defend. C is the principal intermediate conclusion; A and E concede a benefit of the proposal, while B states the mechanism used with the support-record evidence.

#### B.1.06

> [!NOTE]- Answer: C
> The author answers the critic and uses the different sensing mechanisms to support the limited reliability claim in C. A and D are evidence, B is a concession, and E overstates the final qualification.

#### B.1.07

> [!NOTE]- Answer: A
> **Why A is correct:** The author’s ultimate aim is the case-specific recommendation that Mira’s fee be waived.
>
> **Argument map:** the general waiver policy supplies the rule. The saved form supports B, that Mira took reasonable steps, while the server logs support C, that an outside circumstance prevented timely completion. Those facts together support D, the intermediate conclusion that the policy applies to Mira. D then supports A. The last sentence, represented by E, answers a slippery-slope objection: granting this waiver need not excuse students who simply waited too long.
>
> B, C, D, and E may all be claims the author accepts, but the main-conclusion question asks which claim the others are ultimately used to establish. That is A.

#### B.1.08

> [!NOTE]- Answer: E
> The passage's evidence and intermediate comparative judgment in D are offered to support the opening recommendation in E. A is a concession, while B and C are parts of the response to it.

#### B.1.09

> [!NOTE]- Answer: B
> D is an intermediate evaluation derived from the platform's features and the role of diagnostic information. Together with the department's commitment, it supports the qualified recommendation in B. A, C, and E contribute premises rather than the ultimate conclusion.

#### B.1.10

> [!NOTE]- Answer: D
> The demand evidence supports the intermediate conclusion in B, while the parcel comparison supports E. Together they support the site-specific recommendation in D. C is a qualification about what the first evidence can establish.

### B.2 Role of a Statement

Identify the argumentative function of the specified statement, not merely whether it is true.

#### B.2.01

> [!NOTE]- Answer: C
> The statement makes reduced irrigation a requirement for the decision. Combined with thyme's lower water use and adequate durability, it supports the recommendation. It is neither inferred from the plant comparison nor offered as a concession.

#### B.2.02

> [!NOTE]- Answer: D
> The several-week requirement identifies a disruption created by scanning. The author grants that cost, explains how to reduce it, and contrasts it with irreversible loss. It is a concession rather than the conclusion or support for fading.

#### B.2.03

> [!NOTE]- Answer: A
> The audit establishes that the repetitions existed at the relevant time, satisfying the condition explicitly built into the first statement. That fact strengthens the inference from the committee's silence to its likely failure to inspect the raw file.

#### B.2.04

> [!NOTE]- Answer: E
> **Why E is correct:** The expense claim is introduced as a reason offered by engineers who favor closure. The author concedes that point—“the inspection report agrees about the cost”—but argues that it is outweighed by the absence of structural instability, the adequacy of targeted repairs, and the danger of redirecting pedestrians to a road without a sidewalk.
>
> Thus the claim is a **conceded consideration for the opposing position**, not part of the author’s positive case by itself. A contradicts the report, which finds no instability. B reverses the author’s position. C invents a support relation. D is wrong because cost does not qualify whether the safety margin can be restored; it is a separate consideration weighed against keeping the bridge open.

#### B.2.05

> [!NOTE]- Answer: B
> The claim follows from the general encryption premise and the fact about Drive K. It is then shown to address only disclosure, not deletion, which helps support the broader conclusion that encryption alone is inadequate.

#### B.2.06

> [!NOTE]- Answer: C
> The final sentence connects inexpensive, repeatable verification to effective oversight. Applied to the preceding consequences of machine-readable data, it supports the opening policy recommendation without itself stating that policy.

#### B.2.07

> [!NOTE]- Answer: A
> The time-of-day mismatch supports the judgment that the estimate is inadequate for the proposed decision. That judgment then supports the final recommendation to gather broader evidence before changing staffing.

#### B.2.08

> [!NOTE]- Answer: E
> The sale date establishes that the university will own the building for far less than the estimated payback period. Together with the no-resale-premium fact, it supports the owner-specific conclusion while allowing the final qualification about another owner.

#### B.2.09

> [!NOTE]- Answer: B
> **Why B is correct:** The draft’s undefined abbreviations and map labels are evidence for the prediction that many residents will not understand the alert quickly enough. That prediction is not yet the final recommendation. Combined with the opening standard—an alert is useful only if residents can understand it without another source—it supports rewriting and testing the alert.
>
> The structure is: draft features $\rightarrow$ comprehension problem; comprehension problem plus usefulness condition $\rightarrow$ revision recommendation. A reverses the role of the claim, C confuses an effect with an explanation of the abbreviations, D names the opening general standard rather than the specified sentence, and E ignores the sentence’s central inferential role.

#### B.2.10

> [!NOTE]- Answer: D
> The author allows that the reported difference may be real but distinguishes that association from the claimed causal effect. Selection, prior grades, and work hours are offered as reasons the causal interpretation is not yet established.

### B.3 Point at Issue

Select the proposition one speaker accepts and the other rejects. Both positions must be textually supported.

#### B.3.01

> [!NOTE]- Answer: B
> **Why B is correct:** Nara explicitly says the city **should permit** up to four carts; Ivo explicitly says the proposed permit **should be denied**. One accepts the proposition in B and the other rejects it.
>
> For a point-at-issue answer, both attitudes must be textually supported. A may be accepted by Nara, but Ivo never denies that carts offer cheaper food. C is asserted by Ivo, but Nara does not deny it. Both speakers can accept D. E is too broad: Nara cites evidence that a four-cart limit caused only a slight increase in traffic elsewhere, not that numerical limits always prevent crowding.

#### B.3.02

> [!NOTE]- Answer: A
> Leah affirms that the survey is adequate for the majority question; Omar denies exactly that. Both treat random selection as useful, and Omar's objection is compatible with all twelve selected students having replied.

#### B.3.03

> [!NOTE]- Answer: E
> Priya says catalogue status and preserved originals are enough to permit uninspected disposal; Tomas explicitly says inspection is required first. Priya need not deny that copies can contain notes, and Tomas need not deny that their printed text is duplicated.

#### B.3.04

> [!NOTE]- Answer: B
> Mei says the existing model is suitable for the decision; Arturo says it is not suitable without adjustment. Both can accept its past performance and that the policy change could affect demand.

#### B.3.05

> [!NOTE]- Answer: D
> Dana favors reopening now and monitoring later; Sol requires a slope assessment before reopening. Sol explicitly accepts the completed repairs, and Dana does not claim the inspectors evaluated the latest soil reading.

#### B.3.06

> [!NOTE]- Answer: A
> **Why A is correct:** Amina claims that once speech is available as text, **each video will be fully accessible**; she therefore treats accurate captions as sufficient. Joel agrees that captions are necessary but denies that they are sufficient, because visually communicated information may also need description.
>
> The speakers agree on B and C. Joel asserts D and E, but Amina never explicitly denies either proposition; she may simply have overlooked them. A is the only statement for which the passage supplies opposite positions from both speakers.

#### B.3.07

> [!NOTE]- Answer: C
> Ruth's recommendation commits her to treating the replacement as an effective local response; Ken explicitly denies that. He need not reject the outside association, and Ruth does not address where the recent local thefts occurred.

#### B.3.08

> [!NOTE]- Answer: E
> Hana says the results favor authenticity over a later imitation; Luis explicitly says they do not. Both can agree that the results are consistent with authenticity and that the materials date from the claimed period.

#### B.3.09

> [!NOTE]- Answer: C
> Cam supports ending disposable service next month; Noor calls that timing premature. Noor can accept that the deposit improved returns, and Cam does not state that the current return rate is already above half.

#### B.3.10

> [!NOTE]- Answer: D
> Sera's inference rules out the possibility in D; Ben explicitly says that possibility remains open. They agree that approval requires privacy review and that Project L was not approved. Ben's additional requirements do not imply that privacy failure is the only route to nonapproval.

### B.4 Must Follow

Choose the statement that is logically guaranteed by the facts. Do not assume a converse, exclusivity, or an unstated relationship.

#### B.4.01

> [!NOTE]- Answer: B
> Meadow House satisfies both conditions in the first rule, so it employs an avian-certified veterinarian. The second rule then guarantees its quarantine room. River Yard's room does not license either converse inference.

#### B.4.02

> [!NOTE]- Answer: D
> Because the laboratory is closed, any opening this week would occur outside it. Q is archive-key encrypted, so the approval rule applies conditionally. Nothing establishes that Q will be opened or that approval has already been granted.

#### B.4.03

> [!NOTE]- Answer: A
> **Why A must follow:** Let $r$ be one of the people guaranteed by “some robotics-club members are first-year students assigned to fabrication.” Because $r$ is a first-year fabrication member, the universal rule says $r$ completed the supervised demonstration. Anyone who completed it may reserve the beginner workbench. Therefore $r$ is both a club member and eligible to reserve, proving A.
>
> B and E overgeneralize from first-year fabrication members to much larger groups. C reverses the last conditional: demonstration permits reservation, but the passage does not say that only first-year students can complete it. D invents a nonmember witness; the warning that a demonstration does not guarantee membership says only that the implication is unavailable, not that a nonmember demonstrator must exist.

#### B.4.04

> [!NOTE]- Answer: E
> The exclusive Tuesday-or-Thursday choice plus not-Thursday forces Tuesday. The stated exception to Mira's attendance is absent because the inspection is Friday, so Mira attends. Nothing establishes the biconditional or the broader claim about Luis.

#### B.4.05

> [!NOTE]- Answer: C
> K's kiosk status places its issuance before the audit. If K were temporary, the first rule would make it invalid after midnight, contrary to the stated fact. Thus K is not temporary. The facts about some permanent credentials do not support universal claims.

#### B.4.06

> [!NOTE]- Answer: B
> L's unanimous approval and absence of a legal hold guarantee agenda placement; agenda placement guarantees a docket number. The existential postponement fact does not identify L, and no converse from docketing is licensed.

#### B.4.07

> [!NOTE]- Answer: D
> Arming guarantees blue or amber. Since blue is expressly not lit, amber must be lit; combining that conclusion with the stated blue fact yields D. The diagnostic information blocks converses about armed status but does not affect this inference.

#### B.4.08

> [!NOTE]- Answer: A
> **Why A must follow:** The rule is $P(x) \rightarrow C(x)$: every peer-reviewed article has a citation list. The collection contains at least one article $a$ with $\neg C(a)$. By the contrapositive $\neg C(x) \rightarrow \neg P(x)$, $a$ was not peer reviewed. Hence at least one article in the collection was not peer reviewed.
>
> B conflicts with the statement that peer-reviewed articles have author identifiers. C affirms the consequent; editorials with citations are explicit possible counterexamples. D changes “at least one” to “exactly one.” E is unsupported because every article, including editorials, is said to have an author identifier.

#### B.4.09

> [!NOTE]- Answer: E
> No notice and a functioning notification service imply that the backup did not run. From the biconditional, failure to run means the conjunction of idle server and connected archive was false, which is equivalent to E. Neither disjunct alone is forced.

#### B.4.10

> [!NOTE]- Answer: C
> The existential witness is a laboratory course requiring goggles. It therefore provides in-person training and, by the final rule, assigns an acknowledgement. The optional-video fact does not amount to in-person training, and none of the universal rules may be reversed.

### B.5 Parallel Reasoning

Choose the argument with the same valid logical structure, ignoring subject matter.

#### B.5.01

> [!NOTE]- Answer: E
> The stimulus and E both chain P -> Q -> R and reason backward from not-R to not-P. A and D affirm a consequent, while B and C deny an antecedent.

#### B.5.02

> [!NOTE]- Answer: C
> Both arguments have the form all A are B; no B are C; x is A; therefore x is not C. A reaches a similar conclusion from a different premise order and category relation; the remaining choices reverse rules or change the quantifier.

#### B.5.03

> [!NOTE]- Answer: B
> Both arguments start with P or Q, use P -> R and Q -> S, obtain not-P from not-R, and then infer Q and S. A and D treat an inclusive disjunction as exclusive; C omits the disjunction; E negates the wrong alternative.

#### B.5.04

> [!NOTE]- Answer: A
> Both arguments use P -> Q -> R, P or S, and not-S to obtain P and then R. The other choices affirm a consequent, introduce a contradiction, change the disjunction, or derive from the eliminated branch.

#### B.5.05

> [!NOTE]- Answer: D
> **Why D is correct:** The stimulus has the valid chain
> $$\exists x(Ax \land Bx),\quad \forall x(Bx\rightarrow Cx),\quad \forall x(Cx\rightarrow Dx)\quad\therefore\quad \exists x(Ax\land Dx).$$
> The existential premise supplies one object that is both archived and a budget memo; the two universal rules carry that same witness through “indexed” to “searchable.” D repeats exactly this pattern with a marked wetland trail carried through “mapped” to “inspected.”
>
> A and E illicitly strengthen an existential fact into a universal conclusion. B combines two existential statements that may concern different people. C begins similarly but concludes that **no** fragile parcel is anonymous; from “some fragile parcels are insured” one can establish only that **some** fragile parcel is not anonymous.

#### B.5.06

> [!NOTE]- Answer: E
> Both use P exactly when Q, Q -> R, and not-R to infer not-Q and therefore not-P. A and C affirm the consequent, B uses the other direction without the same chain, and D reaches a conclusion weaker than the premises support.

#### B.5.07

> [!NOTE]- Answer: C
> The stimulus and C combine no B is D, some A is B, and every A is C to conclude some C is not D. A illegitimately universalizes, while B, D, and E disconnect the existential witness from a needed category.

#### B.5.08

> [!NOTE]- Answer: B
> Both arguments have (P or Q) -> R, R -> S, and Q, therefore S. A confuses a conjunctive antecedent with a disjunctive one; C affirms a consequent; D and E deny antecedents.

#### B.5.09

> [!NOTE]- Answer: A
> Both use P exactly when (Q and R), plus P, to conclude Q. B affirms the consequent of a one-way rule, C changes the condition, D establishes only half of a conjunctive necessary condition, and E changes conjunction to disjunction.

#### B.5.10

> [!NOTE]- Answer: D
> **Why D is correct:** The stimulus has the form
> $$P\rightarrow Q,\quad P\lor R,\quad \neg Q\quad\therefore\quad R.$$
> From $P\rightarrow Q$ and $\neg Q$, modus tollens gives $\neg P$. From $P\lor R$ and $\neg P$, disjunctive syllogism gives $R$. Choice D preserves this exact sequence: pump runs $\rightarrow$ water flows; pump runs or valve closed; water did not flow; therefore valve closed.
>
> A has “travel is slow or the path is closed,” not “icy or closed,” so its disjunction does not contain the antecedent. B affirms the consequent and then draws an unsupported conclusion about the alarm. C’s disjunction contains “lamp off,” the negation of the antecedent, rather than the antecedent itself. E again uses a differently structured disjunction and affirms the consequent.

## C. Logical Reasoning II: Assumptions and Evidence

> [!CHECK]- Minimum full-credit response and decisive checks
> - **C.1 Necessary assumption:** Give the correct letter and use the negation test: negating the choice must break the stated reasoning.
> - **C.2 Sufficient assumption:** Give the correct letter and show that adding it makes the conclusion follow. It need not be necessary.
> - **C.3 Flaw:** Identify the precise inferential gap and connect it to this passage; a vague label alone is insufficient.
> - **C.4 Strengthen / C.5 Weaken:** Give the correct letter and explain how the new fact improves or damages the argument's actual support link. **Decisive check:** the response discusses the inference, not merely whether the new fact sounds favorable or unfavorable.

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|Rosen §1.2 — Applications of Propositional Logic]]
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen §1.6 — Rules of Inference]]
> - [1.3a Tautologies, Contradictions, and Satisfiability (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3aTautologyContradictionContingencySatisfiableHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3aTautologyContradictionContingencySatisfiable.9.40.mp4)
> - [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)

### C.1 Necessary Assumption

Select the assumption the argument requires. If it were false, the stated reasoning would fail.

#### C.1.01

> [!NOTE]- Answer: A
> The restoration guarantee reaches only files in the most recently completed backup. Because the conclusion covers every file now in use and concerns a loss tonight, the reasoning requires each current file to be in that backup. Negating A leaves at least one current file outside the only stated restoration guarantee.

#### C.1.02

> [!NOTE]- Answer: B
> **Why B is required:** The conclusion is contrastive: the signs, **rather than some unrelated change**, produced most of the decline. Negate B: suppose an unrelated change did account for most of the decline. The director’s conclusion would then be false even though every stated premise could remain true. B therefore passes the negation test for a necessary assumption.
>
> A may help explain a mechanism but is not required; visitors could use signs even if they do not prefer them. C adds an irrelevant design detail. D is stronger than necessary: the signs need to affect enough of the people who would otherwise ask for directions, not necessarily a majority of all visitors. E is a possible consequence, not a required link in the causal inference.

#### C.1.03

> [!NOTE]- Answer: C
> The stated rule makes a valid signature necessary for approval, but the argument treats the signature as sufficient. It therefore requires the converse exclusion: an unapproved request cannot have such a signature. Without that assumption, Rowan's signed request could remain unapproved.

#### C.1.04

> [!NOTE]- Answer: D
> The argument treats K's unique satisfaction of the budget and deadline as decisive against both postponement and the alternatives. If either postponement or knowingly violating a constraint were preferable to adopting the sole feasible plan, the stated comparison would not justify K. D rules out that defeat without requiring K to have every imaginable advantage.

#### C.1.05

> [!NOTE]- Answer: E
> The absence of a flag establishes permission only if every disqualifying failure relevant to Build 18 would produce a flag. If an unflagged build could still violate another release requirement, the conclusion could be false.

#### C.1.06

> [!NOTE]- Answer: A
> The prediction transfers a result from one course to another. It requires that there be no relevant difference—such as class structure or implementation—that defeats the transfer. Exact enrollment and identical preferences are stronger than the argument needs.

#### C.1.07

> [!NOTE]- Answer: B
> **Why B is required:** The evidence concerns 186 volunteers at a cycling workshop; the conclusion concerns Lakeview residents as a whole. The argument requires the sample to be sufficiently representative on the very attitude being estimated. Negate B: if workshop volunteers are strongly more favorable toward bicycle lanes than the wider neighborhood, then even participation from every precinct does not justify the population conclusion.
>
> A is irrelevant to the survey inference. C demands residence along the proposed route, which is unnecessary for a neighborhood-wide opinion estimate. D speculates about opponents’ knowledge. E concerns expected turnout, not representativeness. Geographic coverage alone does not eliminate self-selection bias.

#### C.1.08

> [!NOTE]- Answer: C
> Eliminating the desk and hook establishes the drawer only if those two locations plus the drawer exhaust the current possibilities. If the key could be in a pocket or another room, the elimination is incomplete.

#### C.1.09

> [!NOTE]- Answer: D
> A lower average is compatible with some individuals receiving no benefit or even having longer commutes. The universal conclusion requires ruling out every such case. Sample size does not turn an average improvement into an improvement for each rider.

#### C.1.10

> [!NOTE]- Answer: E
> A single advantage justifies replacement only if relevant disadvantages do not outweigh it. The argument does not require identical completion speeds or fewer questions; it requires the net case for replacement not to be defeated by, for example, missing information or excessive transition costs.

### C.2 Sufficient Assumption

Select the statement that, if added to the stated premises, makes the conclusion follow logically.

#### C.2.01

> [!NOTE]- Answer: A
> The stimulus already supplies the load result and current calibration. Adding A supplies the remaining test result, completing every condition in the stated sufficient rule. The other choices describe necessary conditions, comparisons, or a negated combination that does not establish R's heat-test result.

#### C.2.02

> [!NOTE]- Answer: B
> The stated disjunction and the added denial of its network alternative yield the database alternative by disjunctive syllogism. The other statements do not eliminate the network service as the cause.

#### C.2.03

> [!NOTE]- Answer: C
> The added 'only' statement supplies the converse conditional: if a manuscript receives a permanent archive number, then it was accepted. Applying that conditional to M's archive number entails acceptance.

#### C.2.04

> [!NOTE]- Answer: D
> **Why D is sufficient:** The town can select exactly one project. The footbridge uniquely provides a safe spring crossing, while the fountain offers a lower-cost improvement to the square. D supplies the missing priority rule: in precisely that conflict, the safety benefit outranks the fountain’s advantages. Applying the rule to the stated facts deductively yields the recommendation to fund the footbridge.
>
> A supports the fountain. B and E do not rank the projects. C gives a fact about summer travel but does not establish how to decide the spring-safety tradeoff. A sufficient-assumption answer must close the whole logical gap, not merely make the preferred conclusion somewhat more attractive.

#### C.2.05

> [!NOTE]- Answer: E
> The added universal statement directly places every accessibility-working-group member on the council. Since Niko serves on that group, council membership follows. The original premise alone runs in the opposite direction.

#### C.2.06

> [!NOTE]- Answer: A
> If the checklist was the only change capable of affecting the error count, the observed decline cannot be attributed to a rival change during the period. Given the decline after introduction, that premise is sufficient for the stated causal comparison in this argument.

#### C.2.07

> [!NOTE]- Answer: B
> The existing chain yields that P appears on Friday's agenda. The added agenda-to-discussion conditional extends that chain to the conclusion. The converse in choice A would not guarantee discussion.

#### C.2.08

> [!NOTE]- Answer: C
> The premises make the maker of the blue bowl a local artist who made a displayed ceramic piece. The added universal statement puts every such artist in the cooperative, so the bowl's maker is a cooperative member.

#### C.2.09

> [!NOTE]- Answer: D
> **Why D is sufficient:** We know $N$ is shorter than $P$, but length alone does not generally determine walking time because surface and crossings may matter. D adds a rule tailored to the present comparison: for these two routes under current conditions, the shorter route is also the faster route. Since $N$ is shorter, it follows that $N$ takes less time.
>
> A merely restates that the endpoints are comparable. B does not measure the delay caused by the crossings. C concerns preference rather than travel time. E gives only an upper bound—both routes could take under an hour while $P$ remains faster. D is sufficient even if it is not independently established by the original passage.

#### C.2.10

> [!NOTE]- Answer: E
> The original rule makes a token necessary, not sufficient, while the stimulus separately establishes Q's completed duplicate check. E combines those established conditions into a rule sufficient for immediate admission. Choice D supplies another exclusion but never states that passing the check is enough.

### C.3 Diagnose the Flaw

Select the choice that most precisely describes the error in the argument's reasoning.

#### C.3.01

> [!NOTE]- Answer: A
> **Why A is correct:** The argument observes a before/after association and attributes the entire change to the benches. Holding ticket price and number of performances fixed removes two alternatives, and the survey provides a plausible mechanism, but other simultaneous changes—performers, publicity, weather, scheduling, or population—could still explain the attendance increase. The design lacks a comparison group or adequate control for confounders.
>
> B is unnecessarily strong; benches could increase attendance even if not every new attendee sits. C is compatible with a causal effect. D describes a shift the passage does not make. E misstates the inference: the organizers need not assume patrons value nothing else. A identifies the exact causal gap without exaggerating it.

#### C.3.02

> [!NOTE]- Answer: B
> The premise gives inspection → green seal, while the reasoning uses green seal → inspection. A seal might have another source, so affirming the consequent is invalid unless the converse rule is supplied.

#### C.3.03

> [!NOTE]- Answer: C
> People who choose to attend a baking workshop are unusually likely to value access to a shared kitchen. The sample is therefore not shown to represent the town. The conclusion concerns public support, not whether the proposal will succeed.

#### C.3.04

> [!NOTE]- Answer: D
> The argument constructs a false dilemma. Caring about students is compatible with many schedules and forms of support other than daily midnight hours, so rejecting those hours does not entail indifference.

#### C.3.05

> [!NOTE]- Answer: E
> A twenty-percent rise in complaints can accompany a fall in the rate per user when the user population doubles. The conclusion concerns how often an individual encounters a delay, so totals with different exposure bases do not establish it. Choice D concerns representativeness, but even perfectly representative complainants would not repair the missing rate comparison.

#### C.3.06

> [!NOTE]- Answer: A
> **Why A is correct:** The rule says approval requires both training and managing-editor authorization:
> $$P \rightarrow (T \land A).$$
> Dev is an editor and satisfies $T$, but nothing establishes $A$. Completing one necessary condition does not establish the sufficient conjunction. The list’s not being public is an absence of evidence about authorization, not evidence that Dev is authorized.
>
> B invents a comparison about timing. C concerns a different class of reports. D describes an inference from a single person to everyone that the argument never makes. E is a related possible error, but the conclusion does not require believing that no list exists; the central flaw is treating partial satisfaction of the stated requirements as enough.

#### C.3.07

> [!NOTE]- Answer: B
> Even when every part weighs less than one kilogram, their combined weight can exceed one kilogram. The argument commits a composition error by applying a distributive fact about individual parts to their aggregate.

#### C.3.08

> [!NOTE]- Answer: C
> 'Reliable' and 'trustworthy' do no independent work here: each is offered as the sole support for the other. The final recommendation therefore rests on circular reasoning rather than evidence of catalog accuracy.

#### C.3.09

> [!NOTE]- Answer: D
> Unreported failures may still have occurred, especially if users did not notice them or had no convenient reporting channel. The conclusion requires a detection-and-reporting link that the premises never establish.

#### C.3.10

> [!NOTE]- Answer: E
> A shared grid layout is irrelevant to power requirements. The application's being electronic is precisely the kind of difference that undermines the analogy, so the paper calendar's independence from power does not transfer.

### C.4 Strengthen

Select the statement that, if true, provides the strongest additional support for the argument's conclusion.

#### C.4.01

> [!NOTE]- Answer: A
> The comparison park supplies a control exposed to the same general period but not the signs. Its unchanged litter level makes a broad seasonal explanation less plausible and thereby supports the signs as the relevant cause.

#### C.4.02

> [!NOTE]- Answer: B
> The chief concern is nonresponse bias. A random check showing that nonrespondents have nearly the same view as respondents directly supports treating the returned questionnaires as representative of the whole neighborhood.

#### C.4.03

> [!NOTE]- Answer: C
> **Why C most strengthens:** The recommendation rests on two important claims: shelters would make summer travel more usable, and installing them would not divert funds from essential service. C directly reinforces both. It says lack of shade is a chief reason riders avoid the stops, making shade a well-targeted remedy, and it confirms that four shelters fit the existing improvement budget.
>
> A concerns delays, not shade or feasibility. B shows that some shelters have another benefit but does not show that these shelters solve the stated problem. D is a seasonal scheduling fact. E shows benches can be used in varied weather but provides little evidence about shaded shelters at these stops. C supplies the strongest new link to both premises behind the recommendation.

#### C.4.04

> [!NOTE]- Answer: D
> The intervention changes humidity while holding the major competing factors fixed, and the predicted effect follows. That controlled change provides much stronger causal evidence than the original correlation alone.

#### C.4.05

> [!NOTE]- Answer: E
> The prediction is analogical, so similarities relevant to tutoring's effect matter. Common materials, tutors, student profiles, and starting rates make the evening result much more likely to transfer to the morning section.

#### C.4.06

> [!NOTE]- Answer: A
> The scheduled expansion creates a concrete continuing source of new borrowing over the exact forecast period. It makes simple continuation of the recent pattern more plausible instead of relying only on the past trend.

#### C.4.07

> [!NOTE]- Answer: B
> The statement supplies the decision rule connecting Mei's evidence to qualification and explicitly rules out the exception built into that rule. The conclusion then follows rather than resting on an incomplete list of favorable credentials.

#### C.4.08

> [!NOTE]- Answer: C
> **Why C most strengthens:** The manager’s causal inference is threatened by differences in workers, workload, case mix, and procedures. C holds all four roughly constant across the before/after periods. Because the visual update did not change the displayed rules, removing these additional rivals leaves the training as a much more plausible explanation of the decline.
>
> A describes the training’s format but not its effect. B reports where the decrease was largest without ruling out a change in cases. D weakens a simple dose-response story but does not establish an alternative cause. E concerns how the dates were selected; independent scheduling does not show which change caused the improvement. C most directly improves causal identification.

#### C.4.09

> [!NOTE]- Answer: D
> Random selection from the full catalog makes the checked entries more likely to represent the population about which the conclusion generalizes. The sample size is modest, but representative selection substantially strengthens the inference.

#### C.4.10

> [!NOTE]- Answer: E
> The trial tests the proposed policy under representative operating conditions and observes the predicted benefit without an obvious productivity cost. It therefore supports both effectiveness and adoption.

### C.5 Weaken

Select the statement that, if true, most undermines the support offered for the argument's conclusion.

#### C.5.01

> [!NOTE]- Answer: A
> The added employees are a powerful simultaneous alternative cause of shorter waits. Because the original before-and-after comparison cannot separate staffing from check-in method, its causal conclusion is substantially weakened.

#### C.5.02

> [!NOTE]- Answer: B
> The survey systematically misses a sizeable group whose views differ from those reached. That selection bias directly undermines the inference from respondents to all residents.

#### C.5.03

> [!NOTE]- Answer: C
> The proposal may improve one form of access while eliminating another important form of access. That countervailing consequence weakens the recommendation even if free printing itself is convenient.

#### C.5.04

> [!NOTE]- Answer: D
> The proposed analogy depends on the policy functioning similarly in both workplaces. A major difference in the need for conversation makes a quiet policy potentially harmful at headquarters and therefore undermines transfer of the branch result.

#### C.5.05

> [!NOTE]- Answer: E
> **Why E most weakens:** The original rule is review $\rightarrow$ dated blue stamp. The conclusion reverses it: dated blue stamp $\rightarrow$ review. E provides a concrete alternative cause of the observed stamp—the portal applies it automatically before review—so T could have exactly the observed features without ever being reviewed.
>
> A concerns length, B concerns review order, and C concerns what happens after a completed review; none breaks the stamp-review connection as strongly. D merely aligns two dates and is fully compatible with review. E attacks the argument’s only evidence for its conclusion.

#### C.5.06

> [!NOTE]- Answer: A
> The unusual competing event supplies a concrete reason the recent trend may not continue in the predicted period. The forecast relies on continuity, and the festival disrupts that continuity for the relevant audience.

#### C.5.07

> [!NOTE]- Answer: B
> A surviving nonmetal device is a direct counterexample to the claimed necessity of metal. Scratched metal devices do not matter because the conclusion concerns survival, not absence of cosmetic damage.

#### C.5.08

> [!NOTE]- Answer: C
> The groups differed on the outcome before the supposed cause was introduced. Their later difference may therefore reflect selection or a preexisting condition rather than an effect of night-display mode.

#### C.5.09

> [!NOTE]- Answer: D
> The admission rule selects precisely for the skill being generalized. Club volunteers are therefore predictably much faster than typical city adults, making them a biased sample for the conclusion.

#### C.5.10

> [!NOTE]- Answer: E
> **Why E most weakens:** The agency moves from “the tutorial is accurate” and “applicants must open it” to “applicants will complete the form correctly.” E breaks the behavioral link: opening need not involve reading, understanding, or following the tutorial. If applicants can close it immediately, the requirement may change nothing relevant to their answers.
>
> A and D improve the tutorial and therefore tend to strengthen the plan. B describes device flexibility without undermining learning. C concerns correction after submission and does not show that the requirement fails to improve initial accuracy. E directly shows why the proposed mechanism does not ensure the promised result.

## D. Logical Reasoning III: Principles and Explanations

> [!CHECK]- Minimum full-credit response and decisive checks
> - **D.1 Principle support:** Give the correct letter and map every operative condition of the principle to a stated fact.
> - **D.2 Resolve discrepancy:** Give the correct letter and explain how it permits both apparently conflicting observations to be true.
> - **D.3 Parallel flaw:** Give the correct letter and identify the same invalid move in both arguments.
> - **D.4 Method of reasoning:** Give the correct letter and describe what the author actually does, not a method the author could have used.
> - **D.5 Complete the argument:** Give the correct letter and show how it closes the exact gap without adding an unnecessarily stronger claim. **Decisive check:** the added statement connects the established facts to the stated conclusion.

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|Rosen §1.2 — Applications of Propositional Logic]]
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen §1.6 — Rules of Inference]]
> - [1.4b More on Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisitedHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisited.4.06.mp4)
> - [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)

### D.1 Principle Support

Select the principle that most strongly supports the stated judgment, and briefly justify the application.

#### D.1.01

> [!NOTE]- Answer: A
> Choice A supplies the needed priority rule: scarcity favors the unique recordings because the novels can be replaced from other sources. B requires equal treatment rather than a choice, C points toward the novels, and D and E introduce criteria the director did not use.

#### D.1.02

> [!NOTE]- Answer: B
> **Why B is correct:** The relevant facts match B condition by condition: the cooperative publicly promised prompt disclosure; the discovered defect could seriously compromise user data; and immediate disclosure carries a foreseeable reputational cost because of the demonstration. B says that such a cost does not cancel the obligation to honor the commitment, so it directly supports disclosure now.
>
> A and C introduce delay conditions absent from the promise. D makes sales rather than the commitment decisive. E would permit breaking a promise whenever compliance is inconvenient—the exact reasoning the manager rejects. B is neither broader nor narrower than the judgment it is meant to justify.

#### D.1.03

> [!NOTE]- Answer: C
> C connects the committee's own website failure to a justified exception from its deadline. The recommendation does not depend on the applicant's qualifications or on opposition to deadlines generally, so B and D do not support it; A and E are much broader than the facts warrant.

#### D.1.04

> [!NOTE]- Answer: D
> D links priority for a scarce cooperative benefit to performance of the duties that maintain the garden, matching both relevant facts. A and B prescribe unrelated allocation rules, while C is a permanent and disproportionate penalty and E rests on status rather than contribution.

#### D.1.05

> [!NOTE]- Answer: E
> E narrowly covers the case: the ambiguity was the instructor's, it was material, and the students' interpretation was reasonable. The other choices either require indiscriminate changes, remove the task entirely, substitute effort for correctness, or forbid justified correction.

#### D.1.06

> [!NOTE]- Answer: A
> A explains why low ridership does not settle the decision: the route provides essential transportation with no reasonable substitute. Seeking a smaller vehicle is consistent with preserving access. B and C concern resource levels, D forbids even sensible modifications, and E supports cancellation.

#### D.1.07

> [!NOTE]- Answer: B
> **Why B is correct:** The technician designed a calibration procedure necessary to the reliability of the reported measurements. That is a substantive intellectual contribution to the result. B makes substantive contribution—not faculty/student status—the basis for credit and therefore directly supports adding the technician as an author.
>
> A is overinclusive because employment alone is not authorship. C is too narrow because authorship can reflect design, analysis, or methodology as well as drafting. D substitutes hours worked for intellectual contribution, and E substitutes hierarchy for contribution. Only B connects the stated fact to the director’s judgment.

#### D.1.08

> [!NOTE]- Answer: C
> C establishes that the charter's binding equal-eligibility guarantee limits what a majority may enact, which justifies ruling the proposal out of order. A ignores that limit; B and E introduce unsupported allocation rules; D concerns amendment rather than compliance with the current charter.

#### D.1.09

> [!NOTE]- Answer: D
> D ties the visibility of the remedy to the audience and consequence of the publication's own error, supporting comparable prominence. A makes correction depend on a request, B and E impose unrelated categorical rules, and C ignores whether the correction can repair the impression.

#### D.1.10

> [!NOTE]- Answer: E
> E makes consistent administration, not the moderator's personal priorities, the controlling consideration. The equal announced limits therefore support denial. A is unnecessary, B and C undermine neutrality, and D would make the procedure depend on requests rather than consistent treatment.

### D.2 Resolve the Discrepancy

Select the fact that best allows both reported observations to be true, and explain how it resolves the apparent conflict.

#### D.2.01

> [!NOTE]- Answer: A
> Transactions count purchases, whereas revenue reflects how much is sold in them. If many more transactions contained multi-item bundles, average revenue per transaction could rise enough for total revenue to increase despite fewer transactions. The other facts do not connect transaction count to revenue per transaction.

#### D.2.02

> [!NOTE]- Answer: B
> Distance and travel time need not move together. The bus-only lane can eliminate long intersection delays, more than offsetting the added distance. D merely repeats the discrepancy, while the remaining facts offer no mechanism affecting travel time.

#### D.2.03

> [!NOTE]- Answer: C
> More demanding content can coexist with higher completion when an independent obstacle is removed. Automatic saving prevents interrupted students from losing work and can raise completion enough to outweigh increased difficulty. The other choices do not explain the changed completion rate.

#### D.2.04

> [!NOTE]- Answer: D
> **Why D resolves the discrepancy:** Gate counts measure entries into the building, while the catalog measures new physical-book loans. Outdoor lockers uncouple those measures: a patron can initiate a loan and collect the book without passing through the gate. If enough patrons use the lockers, building entries can fall while loans rise, with all of the stated counting rules unchanged.
>
> A concerns nonpatron deliveries. B explains why some entrants do not borrow but gives no reason for more loans with fewer entrants. C does not distinguish the two winters. E changes book weight, which is irrelevant when each loan counts once. D alone supplies a mechanism that pushes the measures in the reported directions.

#### D.2.05

> [!NOTE]- Answer: E
> Drip lines can make water delivery more efficient: more of a smaller total reaches the roots, so growth can increase while water use decreases. The other choices neither improve effective water delivery nor otherwise reconcile the two measurements.

#### D.2.06

> [!NOTE]- Answer: A
> Fewer agents can still produce shorter waits if demand falls even more sharply. Eliminating a problem responsible for nearly half of prior calls reduces the queue enough to explain the result. The other facts have no relevant effect on call volume or service capacity.

#### D.2.07

> [!NOTE]- Answer: B
> Registrations are not the same as attendance. A much lower no-show rate can yield more occupied seats from fewer registrants. The remaining details do not explain why a larger share of registered people appeared.

#### D.2.08

> [!NOTE]- Answer: C
> Storage time is only one determinant of retained charge. If cooler storage greatly slows discharge, its effect can more than compensate for the longer period. The other choices make the comparison orderly but supply no factor that reverses the expected loss.

#### D.2.09

> [!NOTE]- Answer: D
> **Why D resolves the discrepancy:** An acceptance rate is $\text{accepted}/\text{submitted}$. Both reports can be true when the denominator grows sufficiently. For example, accepting 40% of 100 submissions gives 40 articles, while accepting 30% of 200 gives 60 articles: the percentage falls even as the number rises. D states exactly this denominator change.
>
> B might explain capacity to publish more articles but does not by itself explain the lower rate. A, C, and E are compatible background facts that do not mathematically connect the proportion and count. D makes the two observations jointly unsurprising.

#### D.2.10

> [!NOTE]- Answer: E
> Total injuries equal a rate multiplied by the number of participants. If participation grew enough, the total can rise despite a lower rate per participant. The other facts do not supply the needed change in the population to which the rate applies.

### D.3 Parallel Flaw

Select the argument whose reasoning contains the same flaw as the stimulus, and identify the shared invalid pattern.

#### D.3.01

> [!NOTE]- Answer: A
> **Why A is correct:** The stimulus has the invalid form
> $$(P \land Q)\rightarrow R,\quad R\quad\therefore\quad P\land Q.$$
> It affirms the consequent: public searchability may result from some condition other than both cataloging and a refreshed index. Choice A repeats the form exactly: occupied-and-projector-active $\rightarrow$ glowing panel; glowing panel; therefore both antecedent conditions.
>
> B and E validly apply modus ponens. C validly reasons by contraposition from $(W\lor S)\rightarrow A$ and $\neg A$ to $\neg(W\lor S)$, hence neither condition. D validly uses disjunctive syllogism with an exclusive disjunction. The shared flaw is not merely “assuming too much”; it is reversing a conditional with a conjunctive antecedent.

#### D.3.02

> [!NOTE]- Answer: B
> The stated sufficient condition has two alternative ways to trigger hiring. Rejecting grant renewal leaves reserve funding open, so the conclusion denies the consequence after eliminating only one disjunct. B repeats that error because overnight resting remains an open route to rising. A and E use contraposition; C and D validly apply their premises.

#### D.3.03

> [!NOTE]- Answer: C
> The stimulus wrongly concludes that two groups are identical merely because both lie within a third group: novels and manuals may both have complex plots without being the same objects. C matches with violins and pencils sharing the property of being wooden. A, B, D, and E follow validly from their premises.

#### D.3.04

> [!NOTE]- Answer: D
> The prototype argument transfers a property established for isolated parts to the interacting whole, overlooking failures that can arise from assembly or load. D makes the same composition error: individual ability under solo conditions does not guarantee the ensemble result. A and C reason from whole to parts, while B and E are supported by their premises.

#### D.3.05

> [!NOTE]- Answer: E
> The stimulus infers causation from an association between a self-selected choice and an outcome, ignoring possible prior differences such as health habits. E has the same flaw because motivation or preparation may influence both seat choice and scores. A applies a stated conditional, while B through D make appropriately qualified claims.

#### D.3.06

> [!NOTE]- Answer: A
> **Why A is correct:** The stadium argument uses a voluntary poll posted by opponents, so participation is self-selected and the sampling venue is associated with one side. It nevertheless treats the respondents’ percentage as the percentage among all residents. A has the same selection-bias flaw: buyers with strong opinions choose whether to review, but the store generalizes their responses to all buyers.
>
> B uses random, stratified sampling and is designed for population inference. C surveys every member of the limited target group and reports only that group. D explicitly acknowledges uncertainty rather than claiming exact representativeness. E polls the entire relevant membership and restricts the conclusion to it. A alone matches both the biased selection and overgeneralization.

#### D.3.07

> [!NOTE]- Answer: B
> The stimulus is circular: reliability is supported by trustworthiness, but trustworthiness is then supported only by the asserted reliability. B duplicates that loop with map accuracy and correct markings. The other arguments appeal to checks or evidence independent of the conclusion.

#### D.3.08

> [!NOTE]- Answer: C
> The stimulus attacks the author's unrelated past conduct instead of assessing the loading-zone proposal. C similarly treats the presenter's past littering as a refutation of the recycling plan. A, B, D, and E identify considerations directly relevant to the claims or proposals being evaluated.

#### D.3.09

> [!NOTE]- Answer: D
> The stimulus moves from a lower group average to improvement for every individual, although an average can fall because some commutes disappear or become much shorter while others remain unchanged or grow. D makes the same distribution error with class scores. A concerns changing membership of the average, while B, C, and E are supported by their premises.

#### D.3.10

> [!NOTE]- Answer: E
> The inspections were not capable of establishing calibration, so their failure to reveal inaccuracy is not proof of accuracy. E likewise converts the failure of a damage-only survey to demonstrate danger into complete safety. A, B, and D offer affirmative evidence, while C properly leaves an untested question open.

### D.4 Method of Reasoning

Select the most accurate description of how the argument proceeds, and point to the feature that establishes that description.

#### D.4.01

> [!NOTE]- Answer: A
> The memo makes a universal claim about every meeting, and the argument cites one morning meeting within that domain. A single genuine counterexample is enough to refute a universal statement, exactly as A describes. The argument does not sample, discuss motives, invoke causation, or infer correlation.

#### D.4.02

> [!NOTE]- Answer: B
> The argument compares food and repair carts on features relevant to the inspection rule—size, curb use, and pedestrian clearance—and recommends similar treatment. That is the analogical reasoning described by B. It neither identifies the two cart types nor attacks the rule or the city's authority.

#### D.4.03

> [!NOTE]- Answer: C
> **Why C is correct:** The student treats possession of a card as sufficient for entry: $C\rightarrow E$. The archivist says the card is required, so $E\rightarrow C$, but adds another necessary condition, a confirmed appointment: $E\rightarrow A$. Thus having $C$ alone does not establish $E$. The response distinguishes necessary from sufficient conditions and identifies the missing requirement.
>
> A contradicts the archivist’s concession that the card is required. B invents an exception. D says appointments alone guarantee entry, which the archivist never claims. E would attack a factual premise about the student, but the archivist instead corrects the logical rule.

#### D.4.04

> [!NOTE]- Answer: D
> The author grants the critics' factual point about first-summer watering, then argues that it is temporary and already addressed by stored rainwater. This concession-and-response structure is D. The author does not deny the objection, state a universal principle, attack anyone, or eliminate all alternatives.

#### D.4.05

> [!NOTE]- Answer: E
> The first sentence supplies three exhaustive locations. The search rules out the conference room, and the access evidence rules out the cabinet for a binder used today, leaving the records office. That elimination process is exactly E.

#### D.4.06

> [!NOTE]- Answer: A
> The argument gives a rule and establishes both of its case-specific conditions: readiness and delay caused by the committee's system. It then draws the judgment prescribed by the rule. That is direct principle application, not a generalization, analogy, causal reversal, or attack on all deadlines.

#### D.4.07

> [!NOTE]- Answer: B
> The argument temporarily assumes the consultant's universal claim, applies it to Report 17, and contrasts the resulting error-free prediction with incompatible totals. The contradiction refutes the assumption, which is the reductio method in B. It does not generalize the two errors or rely on authority.

#### D.4.08

> [!NOTE]- Answer: C
> **Why C is correct:** The premises describe a random sample whose class-year proportions mirror the population. The researcher then makes a qualified population inference—“probably”—from the 64% sample result. That is an inductive, probabilistic generalization from a deliberately representative sample.
>
> A is wrong because no rule guarantees every student’s preference. B describes a counterexample, not a sample. D would be circular reasoning, which is absent. E is normative, while the argument is empirical. The sampling design and probabilistic wording are the decisive features.

#### D.4.09

> [!NOTE]- Answer: D
> The speakers use 'efficient' relative to different resources. The chair exposes that ambiguity and replaces the verbal dispute with two explicit dimensions for comparison, exactly as D states. The chair does not decide either factual measurement or declare one definition exclusive.

#### D.4.10

> [!NOTE]- Answer: E
> The dean accepts the decline but points to a simultaneous fall in attendance that could independently produce it. By supplying an alternative cause, the dean weakens the inference that the signs caused the decline. The response does not deny the facts or assert that co-occurring events are never causal.

### D.5 Complete the Argument

Select the claim that most logically completes the argument, and explain how the stated premises support it.

#### D.5.01

> [!NOTE]- Answer: A
> External review imposes a minimum three-week approval time on Orion, while only two weeks remain. Thus Orion cannot be approved for this launch, as A states. The premises do not evaluate external review, guarantee a postponed launch, predict the review result, or establish anything about other proposals.

#### D.5.02

> [!NOTE]- Answer: B
> The rule has the form required attendance implies a remote option. Given no remote option and compliance with the rule, contraposition yields that attendance cannot be required, which is B. Nothing requires cancellation, predicts student behavior, or limits the rule to Fridays.

#### D.5.03

> [!NOTE]- Answer: C
> The premises require at least one of the two roads for emergency access and remove the north road from consideration. Therefore maintaining that access requires the south road to remain open. The other choices add claims about inspections, timing, past closure, or need that the premises do not establish.

#### D.5.04

> [!NOTE]- Answer: D
> The selection rule produces a sample predisposed toward dissatisfaction, so its majority cannot by itself support a conclusion about all students. D states that appropriately limited conclusion. The premises do not establish how many complaints each respondent filed, the views of all nonrecipients, or what another biased survey would find.

#### D.5.05

> [!NOTE]- Answer: E
> **Why E completes the argument:** The archive’s first priority is preventing permanent loss of unique records. Among this year’s proposals, only digitizing the deteriorating notebooks serves that first priority; the others serve the explicitly secondary goal of access. Therefore the notebooks project should rank first among the proposals, exactly as E states.
>
> A expands a comparative decision about this year’s projects into an unlimited rule about every undigitized record. B concerns new acquisitions. C confuses preservation priority with frequency of use. D says preservation has value only when it also produces public access, contrary to the stated ordering of priorities.

#### D.5.06

> [!NOTE]- Answer: A
> A written permit is a necessary condition for this trip, and the condition is unmet with no waiver available. Therefore the trip cannot proceed as planned. The remaining choices make broad predictions or recommendations and evaluations absent from the premises.

#### D.5.07

> [!NOTE]- Answer: B
> The premise says award recipient implies present at the final session. Since Maya was not present, contraposition entails that she was not an award recipient, which is B. The premise does not state who presented, whether presence was sufficient, or anything about other sessions or award timing.

#### D.5.08

> [!NOTE]- Answer: C
> Eligibility requires both conditions. X fails the budget condition, while Y meets both, and the two exhaust the available options. Therefore Y alone is eligible, as C states. The premises neither compare Y with every room nor deny X's accessibility.

#### D.5.09

> [!NOTE]- Answer: D
> The test set differs systematically from the intended use, so performance measured on it may not generalize to independent inputs. D expresses that cautious conclusion. The premises establish neither misconduct nor universal failure, and they do not justify condemning all internal tests or restricting users.

#### D.5.10

> [!NOTE]- Answer: E
> **Why E completes the argument:** The committee adopted an advance decision rule:
> $$(R \land \neg I)\rightarrow A,$$
> where $R$ is reduced average delay, $I$ is an increased error rate, and $A$ is adoption. The representative pilot reduced delays by 18% and left the error rate unchanged, so both antecedent conditions are satisfied. Because no other condition was specified, applying the agreed rule yields adoption.
>
> A and B overstate what one pilot shows. C predicts a decline even though the observed rate was merely unchanged. D asks the committee to add a condition after the agreed trigger has been satisfied. E is the appropriately limited conclusion.

## E. Integrated Evaluation and Revision

> [!CHECK]- Minimum full-credit response and decisive checks
> - **E.1 Causal evaluation:** Identify the causal conclusion and evidence, give a genuine alternative explanation or confound, and state one result that would strengthen and one that would weaken the causal claim. Equivalent well-supported study designs are acceptable. **Decisive check:** the response explains why association alone does not establish causation.
> - **E.2 Principle application:** Select or state the principle and explicitly map the scenario's facts to its conditions.
> - **E.3 Integrated reconstruction:** Identify the conclusion and strongest support, diagnose the requested ambiguity or gap, consider a relevant alternative, and write a qualified revision. Different revisions earn full credit if they are supported by the evidence and actually repair the diagnosed problem.

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|Rosen §1.2 — Applications of Propositional Logic]]
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen §1.6 — Rules of Inference]]
> - [1.2 Intro to Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntroHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntro.11.19.mp4)
> - [1.4b More on Logic and English (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisitedHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisited.4.06.mp4)
> - [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)

### E.1 Causal Evaluation

Separate association from causation and say what additional evidence would matter.

#### E.1.01

> [!NOTE]- Solution
> The conclusion is that enabling reminders causes more timely submission; the evidence is an observed difference between students who chose to enable them and those who did not. Selection prevents a causal inference: students who are already organized may be more likely both to enable reminders and to submit on time. A randomized study assigning otherwise comparable students to reminder and no-reminder conditions, followed by a meaningful difference in on-time submission, would strengthen the claim. Finding the same preexisting submission gap before reminders were available, or finding no change when reminders are randomly enabled, would weaken it.

#### E.1.02

> [!NOTE]- Solution
> **Causal conclusion:** Using a standing desk causes an employee to complete more support tickets per week.
>
> **Evidence offered:** In an observational comparison, employees who chose the optional standing desks completed more weekly tickets than employees using ordinary desks. This establishes an association, not yet a causal effect.
>
> **Why causation does not follow:** Desk choice was not randomly assigned. The two groups may differ before desk use, and ticket count may not measure comparable work. For example, employees with stronger prior performance or greater energy may be more likely to request standing desks. Alternatively, standing-desk users may receive a larger number of easy tickets. Either explanation can produce the observed association even if the desks have no effect.
>
> **Evidence that would strengthen:** Randomly assign otherwise comparable employees to desk types, keep work volume and case difficulty similar, measure baseline and later performance, and find a sustained increase only after assignment to standing desks. A crossover design, in which the same employees use both arrangements in randomized periods, would also reduce person-level confounding.
>
> **Evidence that would weaken:** The standing-desk group already completed more tickets before receiving the desks; the difference disappears after controlling for case difficulty and hours worked; or randomized desk assignment produces no meaningful difference. Any of these findings breaks or seriously weakens the proposed causal explanation.

#### E.1.03

> [!NOTE]- Solution
> The conclusion attributes the fall in reported theft to the lamps; the evidence is a before-after change in one park. Other changes at the same time—additional patrols, seasonal attendance, construction, or changed reporting—could explain the reduction. A staggered or randomized lighting change across comparable parks, with theft declining specifically when each park receives brighter lamps, would strengthen the claim. A similar decline in unmodified parks, or records showing patrols increased at Riverside when the lamps changed, would weaken it.

#### E.1.04

> [!NOTE]- Solution
> The conclusion says workshop attendance lowers blood pressure; the evidence is the later difference between voluntary attendees and nonattendees. Attendees may have been more motivated, taken medication more consistently, exercised more, or begun with different blood pressure. Random assignment to an invitation with high compliance, or a matched study showing comparable baselines and no other treatment difference, would strengthen the claim. A large baseline difference or evidence that medication changes fully explain the later gap would weaken it.

#### E.1.05

> [!NOTE]- Solution
> The conclusion is that weekly practice quizzes improve performance; the evidence compares different classes. The classes may differ in instructor, student preparation, time on task, grading incentives, or curriculum. Randomly assigning comparable course sections to otherwise identical quiz and no-quiz designs would strengthen causation, especially if the improvement tracks quiz exposure. Evidence that quiz sections had stronger incoming students or additional review time that explains the score difference would weaken the claim.

#### E.1.06

> [!NOTE]- Solution
> The conclusion says planting trees reduces electricity use; the evidence is a cross-neighborhood correlation. Tree-rich neighborhoods may also have newer buildings, different household incomes, smaller homes, cooler locations, or residents with different energy habits. Comparing randomly or quasi-randomly selected blocks before and after a tree-planting program against similar untreated blocks would strengthen the claim. If the association disappears after building age and home size are controlled, or if new trees produce no later change, the claim is weakened.

#### E.1.07

> [!NOTE]- Solution
> **Causal conclusion:** Turning off social-media notifications causes a reduction in stress.
>
> **Evidence offered:** One month later, users who chose to turn notifications off reported less stress than users who left them on. This is an association between a self-selected behavior and a later self-reported outcome.
>
> **Why causation does not follow:** Users chose their settings. People actively trying to reduce stress may simultaneously improve sleep, reduce workload, leave stressful platforms, or limit total screen time. Baseline stress or notification volume may also differ between groups. In addition, reported stress can be influenced by expectations about the intervention.
>
> **Evidence that would strengthen:** Measure baseline stress, randomly assign users to notification-on and notification-off conditions, verify compliance, hold other social-media access comparable, and find a larger reduction in the off group. Replication with both self-report and a well-chosen behavioral or physiological measure would further strengthen the case.
>
> **Evidence that would weaken:** The off group already reported less stress at baseline; most members also sharply reduced total social-media use while the on group did not; the association vanishes after those differences are controlled; or a randomized study finds no difference. Those results suggest selection or another behavioral change, rather than notification status itself, explains the outcome.

#### E.1.08

> [!NOTE]- Solution
> The conclusion is that the fertilizer causes greater height; the evidence is a difference between treated and untreated plants. The inference remains uncertain unless assignment and other conditions were controlled: the treated plants might have received more light, water, or started larger. Randomly assigning similar seedlings to fertilizer and control groups while holding soil, light, and water constant would strengthen the claim. A baseline height imbalance, unequal light, or a blinded replication showing no height difference would weaken it.

#### E.1.09

> [!NOTE]- Solution
> The conclusion credits stand-ups for faster resolution; the evidence is a short before-after sequence. April defects may have been easier, the team may have gained staff, a new diagnostic tool may have arrived, or the March backlog may have cleared. Comparing similar teams with staggered adoption, or tracking the same team over a longer stable period while other changes are documented, would strengthen the claim. Evidence that defect complexity fell sharply or that comparable teams improved without stand-ups would weaken it.

#### E.1.10

> [!NOTE]- Solution
> The conclusion is that filter use prevents illness; the evidence is a self-selected user comparison based on reports. Filter users may have different water sources, hygiene practices, income, travel, or willingness to report illness. A randomized filter trial with the same water source and prespecified illness measurement would strengthen the causal claim. Tests showing both groups received equally clean water while reporting habits differed, or adjustment for water source eliminating the association, would weaken it.

### E.2 Apply a Principle

Choose the judgment that satisfies every condition in the principle. Then map each condition to a stated fact.

#### E.2.01

> [!NOTE]- Answer: B
> Choice B supplies every condition: the purchase is costly and unavoidable, its benefit is only administrative convenience, and existing cards are a less burdensome practical alternative. Choice A concerns a serious safety benefit and offers loaners; D is avoidable; C and E treat burden or dislike as decisive without the principle's other conditions.

#### E.2.02

> [!NOTE]- Answer: A
> Choice A concerns an eligible, safe, lawful submission, the publicly promised merit criterion, and an attempted substitution based only on unpopularity. Choice B applies an announced safety limit, while C and E endorse unrelated substitutions and D wrongly extends one promise to future decisions.

#### E.2.03

> [!NOTE]- Answer: D
> Choice D maps each element: removing the panel creates a foreseeable risk, visitors cannot readily detect it, and a visible barrier is a reasonable precaution with no comparable danger. The other choices omit creation, an exposed person, hiddenness, or the exception.

#### E.2.04

> [!NOTE]- Answer: C
> **Why C is correct:** Map every condition in the principle:
> - **Same important benefit:** controlled pilots show equal pollution reduction.
> - **Both feasible:** the choice explicitly says both policies are feasible.
> - **Less restrictive:** a voluntary rebate restricts individual choice less than a mandate.
> - **No substantial-cost exception:** they are similarly priced.
> - **No distinct-risk exception:** neither creates an additional safety risk.
>
> With every condition satisfied and neither exception triggered, the principle directs officials to choose the rebate. A fails the equal-benefit condition. B supplies no comparison of effectiveness, cost, or risk. D triggers the substantially-higher-cost exception. E triggers the distinct-serious-risk exception. The principle is conditional, so “less restrictive” does not automatically control in those cases.

#### E.2.05

> [!NOTE]- Answer: E
> Choice E distinguishes the prohibited serious penalty based solely on a false-positive-prone result from the permitted proportionate investigation. A wrongly bars investigation, B and C treat labels or repeated dependent alerts as corroboration, and D ignores the independent-evidence qualification.

#### E.2.06

> [!NOTE]- Answer: A
> Choice A supplies a personal financial relationship tied to the pending decision, reasonable grounds for doubt, and disclosure before participation. B fits the general-public exception, C is late, D is not financial, and E treats claimed objectivity as eliminating the duty.

#### E.2.07

> [!NOTE]- Answer: D
> Choice D identifies the restriction's sole emergency basis, reliable evidence that the specific risk has ceased, and no independent justification. A lacks cessation, B and C invent no qualifying basis, and E ignores the independent bridge-safety justification.

#### E.2.08

> [!NOTE]- Answer: B
> Choice B includes knowing acceptance of a divisible voluntary benefit, deliberate refusal of a fair ordinary cost, and a practical contribute-or-forgo remedy. A and E lack accepted benefit, C lacks divisibility and a practical exit, and D lacks refusal to contribute.

#### E.2.09

> [!NOTE]- Answer: C
> **Why C is correct:** The rule’s specified purpose is preventing soil damage. Field tests show that lightweight tripods do not increase that harm. Their resemblance to harmful heavy rigs—three legs and a camera mount—is irrelevant to soil damage. Prohibiting them merely because of that resemblance would therefore violate the principle, so the rule should permit them.
>
> A substitutes an owner’s promise for evidence and would permit equipment known to increase erosion. B rejects the rule based on a different value judgment rather than applying its stated purpose. D permits a ban for expense, which is unrelated to the specified harm and therefore contradicts the principle. E focuses on superficial difference while ignoring evidence that the heavy rig creates the same harm.

#### E.2.10

> [!NOTE]- Answer: E
> Choice E supplies a prediction used to recommend costly action and assumptions that are both material and uncertain. A demands immaterial details, B and D conceal material uncertainty, and C concerns a measured fact rather than the kind of assumption covered.

### E.3 Integrated Op-Ed Analysis and Revision

Reconstruct and improve the argument while preserving what its evidence can genuinely support.

#### E.3.01

> [!NOTE]- Solution
> **Main conclusion:** The university should keep one computer lab open overnight during the final two weeks.
>
> **Strongest stated support:** Some students lack dependable computing space at home; students steadily used a late-hours pilot; and pilot users submitted more assignments on time than nonusers. The first two facts support the existence of an access problem and demand for later hours. The submission data give a reason to study a possible academic benefit.
>
> **Ambiguity:** “Academic performance” might mean on-time submission, completion, grades, learning, retention, or something else. The evidence measures only on-time submission. “Worth its cost” is also underspecified: steady use alone does not show how large the benefit is or whether it justifies staffing, security, and facility costs.
>
> **Inferential gaps:** A lab kept open “late” does not establish demand for **overnight** access. The correlation between using the lab and timely submission does not prove that access caused the difference. The argument also applies the rule “any steadily used resource is worth its cost” without evidence that this very broad rule is reliable.
>
> **Alternative explanation:** More organized or motivated students may be more likely both to use the pilot and to submit work on time. Pilot users may also differ in course load, deadlines, housing, or prior achievement.
>
> **Supported revision:** *The pilot demonstrates demand for later lab access among students who lack dependable computing space. The university should therefore run a finals-period extended-hours trial and measure hourly use, staffing and security costs, and outcomes for comparable students before deciding whether overnight operation is warranted.*
>
> This conclusion preserves the genuine access evidence, avoids equating association with causation, and recommends a next step proportionate to what the pilot established.

#### E.3.02

> [!NOTE]- Solution
> The main conclusion is that every downtown parking fee should be removed permanently. Its strongest support is the simultaneous weekend increase in sales and temporary free parking. 'Good for the whole community' is ambiguous, and one weekend neither isolates parking's effect nor establishes that permanent removal has net benefits after congestion and lost revenue. A festival, favorable weather, or seasonal shopping could explain sales. A careful revision is: 'Because sales rose during the free-parking weekend, the city should compare several limited free-parking trials with similar paid-parking periods while measuring sales, traffic, access, and revenue before changing permanent policy.'

#### E.3.03

> [!NOTE]- Solution
> The main conclusion mandates six workshops as a registration condition. The support is workshop popularity and higher essay grades among voluntary attendees. 'Every skill' and 'effective' lack standards; popularity does not establish learning, the grade comparison is self-selected, and no evidence fixes six as the right number or justifies a registration hold. More motivated or better-prepared writers may attend. A qualified revision is: 'The attendance and grade pattern justifies offering and rigorously evaluating the workshops; before imposing a requirement, the university should compare similar students, identify which skills improve, and assess how many sessions are beneficial.'

#### E.3.04

> [!NOTE]- Solution
> The main conclusion is to replace half the town's trash cans with recycling-only bins next month. The support is reduced litter complaints after mixed public recycling bins appeared in two parks. 'Environmentally responsible' and 'recycle everything' are vague or unrealistic. Fewer complaints do not show why litter changed, do not measure sorting accuracy, and do not support removing general-waste capacity townwide. Increased cleanup or fewer park visitors could explain the decline. A careful revision is: 'The park results support testing paired trash and recycling bins at additional sites while measuring litter, contamination, use, and servicing needs before changing townwide bin capacity.'

#### E.3.05

> [!NOTE]- Solution
> The main conclusion is to close the office and require permanent remote work. The support is a higher message count among remote employees plus asserted links from messages to collaboration and quality. 'Collaboration' and 'better work' are not operationalized; message volume may reflect coordination difficulty rather than productive collaboration, and no quality outcome or cost comparison is provided. Remote employees may have different roles requiring more written communication. A revision is: 'The message difference warrants studying how work location affects communication, quality, employee needs, and costs; it does not yet justify eliminating the office or requiring one arrangement.'

#### E.3.06

> [!NOTE]- Solution
> **Main conclusion:** The department should require the new textbook in every introductory section.
>
> **Strongest stated support:** The new book has shorter chapters, and students in the first section using it completed more assigned reading. This provides preliminary evidence that the book may make completion easier in at least one setting.
>
> **Ambiguity:** “Shorter books” could mean a lower total page count, shorter individual chapters, less content, or more concise presentation. Only shorter chapters were established. “Deeper learning” is also undefined and was not measured; reading completion is not the same as comprehension, transfer, or long-term retention.
>
> **Inferential gaps:** The argument moves from one section to every section and from correlation to causation. It also moves from increased completion to deeper learning without evidence connecting the two. The statement that no instructor wants students to fall behind expresses a shared goal, but it does not show that this book best achieves it.
>
> **Alternative explanation:** The instructor may have changed reminders, quizzes, pacing, workload, or grading incentives. The first class may also differ from earlier classes in preparation or motivation. Any of those differences could increase completion without the textbook causing it.
>
> **Supported revision:** *Because reading completion was higher in the first section using the new textbook, the department should pilot it in additional comparable sections and measure completion, comprehension, cost, accessibility, and instructor practices before deciding whether to adopt it coursewide.*
>
> The revision treats the observed result as promising evidence, not proof of deeper learning or a sufficient basis for an immediate universal requirement.

#### E.3.07

> [!NOTE]- Solution
> The conclusion calls for immediate cameras on every residential block. The support is plate recording and reported feelings after a one-week pilot. 'Safer' may mean perceived or actual safety; recording plates and increasing perceived safety do not establish crime prevention, comparative effectiveness, or that benefits outweigh privacy and cost. Saying opponents care more about privacy than safety attacks or oversimplifies their motives rather than answering their concerns. A careful revision is: 'The pilot shows that cameras can record traffic and may affect perceived safety; the city should evaluate crime outcomes, accuracy, privacy safeguards, costs, and less intrusive alternatives before considering broader use.'

#### E.3.08

> [!NOTE]- Solution
> The main conclusion is to disable lecture-hall wireless access to prevent laptop use. The support is a one-lecture association between handwriting and next-day factual recall. 'Best way to learn' ignores other outcomes and subjects; the evidence does not establish general causation, and disabling wireless is a much broader intervention than encouraging handwritten notes. Students may have chosen methods based on preparation or engagement. A careful revision is: 'The recall difference supports a controlled study of note-taking methods across subjects and outcomes, and instructors may share the result while preserving necessary device access; it does not justify a campus network ban.'

#### E.3.09

> [!NOTE]- Solution
> The main conclusion is to eliminate charges for lost books. The evidence is increased returns after overdue fines ended. That before-after result does not isolate the cause, and overdue fines differ from replacement charges because returning a late book and losing it impose different costs. The claim that every supporter of access must oppose every fee is a false dilemma or purity test that substitutes a label for analysis. A justified revision is: 'The increase after eliminating overdue fines supports continued evaluation of that policy; before changing lost-book charges, the library should examine whether they deter access, recover replacement costs, and can be adjusted through waivers or alternatives.'

#### E.3.10

> [!NOTE]- Solution
> The main conclusion is a citywide conversion of one lane on every major road this year. Its support is shorter bus times and higher ridership on one pilot avenue. 'Solved congestion' is undefined and much stronger than the evidence; results from one avenue do not show effects on other roads or all travelers. A fare change, service increase, road construction, or seasonal demand could also affect ridership. A careful revision is: 'The pilot's travel-time and ridership results justify evaluating additional corridors whose traffic and transit conditions are comparable, while measuring total person travel, reliability, safety, and spillover congestion before a citywide conversion.'
