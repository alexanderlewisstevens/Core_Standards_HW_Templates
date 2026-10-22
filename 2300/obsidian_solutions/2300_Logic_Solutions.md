---
title: 2300 Logic Solutions
aliases:
  - 2300 Logic Solutions
  - Logic Solutions
linter-yaml-title-alias: 2300 Logic Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Wednesday, October 21st 2026
publish: true
permalink: core-assessment-solutions/2300-logic-solutions
---
# Logic Core Solutions

This page contains worked solutions for the complete Logic Core practice bank.
It is not a live assessment form. On a supervised attempt, course staff select
one problem from each section A--E, for five problems total. **Meets** means four
of the five selected problems are fully correct; **Exceeds** means all five are
fully correct. Every required subpart of a labeled problem must be complete for
that problem to count as correct.

> [!IMPORTANT] Full-credit and grader guidance
> The worked solution is one model, not the only acceptable wording. Equivalent
> notation, a different truth-table row order, a different satisfying assignment,
> or a different valid equivalence chain earns full credit when it satisfies every
> direction in the prompt. Each section below identifies a **minimum complete
> answer** and a **decisive check**. The decisive check helps a grader find the
> central idea quickly; it does not excuse a missing required subpart.

## A. Construct and interpret truth tables

> [!TIP]- Relevant materials
> - Rosen: [[Books/book_sections_md/1.1_Propositional_Logic|§1.1 — Propositional Logic]] and [[Books/book_sections_md/1.3_Propositional_Equivalences|§1.3 — Propositional Equivalences]]
> - [Truth Tables handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1dTruthTablesHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1dTruthTables.10.47.mp4)
> - [Logical Equivalence Using Truth Tables handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3bLogicalEquivalenceTruthTableHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3bLogicalEquivalenceTruthTable.9.07.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** all eight valuations, correct useful intermediate
> columns, the correct final column, and the classification. Any consistent row
> order is acceptable. **Decisive check:** inspect the final column first; it must
> have exactly the pattern shown below and support the stated classification.

#### A.1

> [!NOTE]- Solution
>
> | $p$ | $q$ | $r$ | $\neg q\lor r$ | $p\to(\neg q\lor r)$ |
> |:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T |
> | T | T | F | F | F |
> | T | F | T | T | T |
> | T | F | F | T | T |
> | F | T | T | T | T |
> | F | T | F | F | T |
> | F | F | T | T | T |
> | F | F | F | T | T |
>
> The final column contains both truth values, so this is a **contingency**.

#### A.2

> [!NOTE]- Solution
>
> | $p$ | $q$ | $r$ | $\neg p$ | $q\to r$ | $\neg p\to(q\to r)$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | T | T |
> | T | T | F | F | F | T |
> | T | F | T | F | T | T |
> | T | F | F | F | T | T |
> | F | T | T | T | T | T |
> | F | T | F | T | F | F |
> | F | F | T | T | T | T |
> | F | F | F | T | T | T |
>
> This is a **contingency**.

#### A.3

> [!NOTE]- Solution
>
> | $p$ | $q$ | $r$ | $p\to q$ | $\neg p\to r$ | Final |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T | T |
> | T | T | F | T | T | T |
> | T | F | T | F | T | T |
> | T | F | F | F | T | T |
> | F | T | T | T | T | T |
> | F | T | F | T | F | T |
> | F | F | T | T | T | T |
> | F | F | F | T | F | T |
>
> The final proposition $(p\to q)\lor(\neg p\to r)$ is always true, so it is a **tautology**.

#### A.4

> [!NOTE]- Solution
>
> | $p$ | $q$ | $r$ | $p\to q$ | $\neg p\to r$ | Final |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T | T |
> | T | T | F | T | T | T |
> | T | F | T | F | T | F |
> | T | F | F | F | T | F |
> | F | T | T | T | T | T |
> | F | T | F | T | F | F |
> | F | F | T | T | T | T |
> | F | F | F | T | F | F |
>
> The final proposition $(p\to q)\land(\neg p\to r)$ is a **contingency**.

#### A.5

> [!NOTE]- Solution
>
> | $p$ | $q$ | $r$ | $p\leftrightarrow q$ | $\neg q\leftrightarrow r$ | Final |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | F | T |
> | T | T | F | T | T | T |
> | T | F | T | F | T | T |
> | T | F | F | F | F | F |
> | F | T | T | F | F | F |
> | F | T | F | F | T | T |
> | F | F | T | T | T | T |
> | F | F | F | T | F | T |
>
> The final proposition $(p\leftrightarrow q)\lor(\neg q\leftrightarrow r)$ is a **contingency**.

## B. Translate meaning and diagnose translation errors

> [!TIP]- Relevant materials
> - Rosen: [[Books/book_sections_md/1.1_Propositional_Logic|§1.1 — Propositional Logic]], [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|§1.2 — Applications of Propositional Logic]], and [[Books/book_sections_md/1.5_Nested_Quantifiers|§1.5 — Nested Quantifiers]]
> - [Conditional Statements handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1cConditionalStatementsHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1cConditionalStatements.10.10.mp4)
> - [Logic and English handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisitedHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4bLogicAndEnglishRevisited.4.06.mp4)
> - [Nested Quantifiers handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.5NestedQuantifiersHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.5NestedQuantifiers.6.04.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** all three parts, with the conditional pointing in
> the correct direction, the quantified formula translated with its variable
> roles intact, and the proposed translation explicitly diagnosed. Logically
> equivalent formulas and ordinary-English paraphrases are acceptable.
> **Decisive check:** verify the order of the quantifiers and the order of the
> arguments in a two-place predicate; these are the errors most likely to reverse
> the meaning.

#### B.1

> [!NOTE]- Solution
> - **(a)** $e\to a$. Equivalently, $\neg a\to\neg e$.
> - **(b)** There is a student who sent a message to every student.
> - **(c)** The proposed reading is incorrect. “Every student sent a message to at least one student” is $\forall x\,\exists y\,Q(x,y)$; it reverses the quantifier order and meaning.

#### B.2

> [!NOTE]- Solution
> - **(a)** $m\to(e\lor p)$.
> - **(b)** Every student sent a message to at least one student.
> - **(c)** $\forall y\,\exists x\,Q(x,y)$ says every student received a message from at least one student. “One student sent a message to every student” is $\exists x\,\forall y\,Q(x,y)$.

#### B.3

> [!NOTE]- Solution
> - **(a)** $g\to(r\land\neg m\land\neg b)$.
> - **(b)** There is a computer-science course that every student has taken.
> - **(c)** $\forall x\,\exists y\,P(x,y)$ says every student has taken at least one computer-science course, possibly a different course for each student. It does not require one common course.

#### B.4

> [!NOTE]- Solution
> - **(a)** $w\to(d\lor s)$. Equivalently, $w\land\neg s\to d$.
> - **(b)** $\forall x\,\exists y\,L(x,y)$.
> - **(c)** $\exists y\,\forall x\,L(x,y)$ says there is one person whom everybody loves. In the correct translation, the loved person may differ with $x$.

#### B.5

> [!NOTE]- Solution
> - **(a)** $q\to p$.
> - **(b)** Over the domain of all people,
>   $$\exists x\bigl(S(x)\land\forall y(F(y)\to A(x,y))\bigr).$$
> - **(c)** Replacing $A(x,y)$ with $A(y,x)$ says that some student was asked a question by every faculty member:
>   $$\exists x\bigl(S(x)\land\forall y(F(y)\to A(y,x))\bigr).$$
>   Reversing the arguments reverses who asked whom.

## C. Negate quantified statements

> [!TIP]- Relevant materials
> - Rosen: [[Books/book_sections_md/1.4_Predicates_and_Quantifiers|§1.4 — Predicates and Quantifiers]] and [[Books/book_sections_md/1.5_Nested_Quantifiers|§1.5 — Nested Quantifiers]]
> - [Quantifiers handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4aQuantifiersHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4aQuantifiers.4.07.mp4)
> - [Negating Expressions handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4cNegatingExpressionsHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4cNegatingExpressions.7.38.mp4)
> - [Nested Quantifiers handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.5NestedQuantifiersHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.5NestedQuantifiers.6.04.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** for (a), definitions, a correct symbolic original,
> a negation with no negation immediately before a quantifier, and a matching
> English reading; for (b), the fully pushed-in negation. Equivalent De Morgan
> forms are acceptable. **Decisive check:** every crossed quantifier must flip
> ($\forall\leftrightarrow\exists$), and the innermost predicate or connective
> must be negated correctly.

#### C.1

> [!NOTE]- Solution
> - **(a)** Let $D(x)$ mean “$x$ is a dog” and $F(x)$ mean “$x$ has fleas.” The statement is $\forall x(D(x)\to F(x))$. Its negation is $\exists x(D(x)\land\neg F(x))$: some dog does not have fleas.
> - **(b)** $\neg\exists y\,\exists x\,P(x,y)\equiv\forall y\,\forall x\,\neg P(x,y)$.

#### C.2

> [!NOTE]- Solution
> - **(a)** Let $M(x)$ mean “$x$ is a monkey” and $F(x)$ mean “$x$ can speak French.” The statement is $\forall x(M(x)\to\neg F(x))$. Its negation is $\exists x(M(x)\land F(x))$: some monkey can speak French.
> - **(b)** $\neg\forall x\,\exists y\,P(x,y)\equiv\exists x\,\forall y\,\neg P(x,y)$.

#### C.3

> [!NOTE]- Solution
> - **(a)** Let $O(x)$ mean “$x$ is old,” $D(x)$ mean “$x$ is a dog,” and $T(x)$ mean “$x$ can learn new tricks.” The statement is $\exists x(O(x)\land D(x)\land T(x))$. Its negation is $\forall x(\neg O(x)\lor\neg D(x)\lor\neg T(x))$, equivalently $\forall x((O(x)\land D(x))\to\neg T(x))$: no old dog can learn new tricks.
> - **(b)** $\neg\forall x\,\forall y\,P(x,y)\equiv\exists x\,\exists y\,\neg P(x,y)$.

#### C.4

> [!NOTE]- Solution
> - **(a)** Let $C(x)$ mean “$x$ is in this class,” $F(x)$ mean “$x$ knows French,” and $R(x)$ mean “$x$ knows Russian.” The statement is $\forall x(C(x)\to\neg(F(x)\land R(x)))$. Its negation is $\exists x(C(x)\land F(x)\land R(x))$: someone in this class knows both French and Russian.
> - **(b)** $\neg\forall y\,\exists x\,P(x,y)\equiv\exists y\,\forall x\,\neg P(x,y)$.

#### C.5

> [!NOTE]- Solution
> - **(a)** Let $W(x)$ mean “$x$ is a Swedish movie” and $S(x)$ mean “$x$ is serious.” The statement is $\forall x(W(x)\to S(x))$. Its negation is $\exists x(W(x)\land\neg S(x))$: some Swedish movie is not serious.
> - **(b)**
>   $$\neg\forall y\,\forall x(P(x,y)\lor Q(x,y))
>   \equiv\exists y\,\exists x\,\neg(P(x,y)\lor Q(x,y))
>   \equiv\exists y\,\exists x(\neg P(x,y)\land\neg Q(x,y)).$$

## D. Determine consistency and satisfiability

> [!TIP]- Relevant materials
> - Rosen: [[Books/book_sections_md/1.2_Applications_of_Propositional_Logic|§1.2 — Applications of Propositional Logic]] and [[Books/book_sections_md/1.3_Propositional_Equivalences|§1.3 — Propositional Equivalences]]
> - [Logic and English handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntroHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.2LogicAndEnglishIntro.11.19.mp4)
> - [Tautologies, Contradictions, and Satisfiability handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3aTautologyContradictionContingencySatisfiableHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3aTautologyContradictionContingencySatisfiable.9.40.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** definitions and translations for all atomic claims,
> a correct consistency verdict, a complete satisfying assignment or explicit
> contradiction, and the final balancing request. A truth table, systematic case
> split, or shorter derivation is equally acceptable. **Decisive check:** a claimed
> satisfying assignment must make every condition true; an inconsistency proof
> must derive both a proposition and its negation from the listed conditions.

#### D.1

> [!NOTE]- Solution
> Let $M$ mean multiuser state, $N$ mean operating normally, $K$ mean the kernel is functioning, and $I$ mean interrupt mode. The conditions are
> $$M\leftrightarrow N,\quad N\to K,\quad \neg K\lor I,\quad \neg M\to I,\quad \neg I.$$
> From $\neg I$ and $\neg K\lor I$, infer $\neg K$. From $N\to K$, infer $\neg N$; the biconditional then gives $\neg M$. Finally $\neg M\to I$ gives $I$, contradicting $\neg I$. The conditions are **inconsistent**.
>
> All five conditions form a minimal inconsistent collection: removing any one allows a satisfying assignment. Listed in condition order, witnesses after removing conditions 1 through 5 are
> $$(M,N,K,I)=(T,F,F,F),(T,T,F,F),(T,T,T,F),(F,F,F,F),(F,F,F,T).$$

#### D.2

> [!NOTE]- Solution
> Let $G$ mean software is being upgraded, $A$ mean users can access the file system, and $S$ mean users can save new files. The conditions are
> $$G\to\neg A,\qquad A\to S,\qquad \neg S\to\neg G.$$
> They are **consistent**. All satisfying assignments $(G,A,S)$ are
> $$(T,F,T),\quad(F,F,F),\quad(F,F,T),\quad(F,T,T).$$
> If $G$ is true, the first and third conditions force $A=F$ and $S=T$; if $G$ is false, only $A=T,S=F$ is excluded.

#### D.3

> [!NOTE]- Solution
> Let $P$ mean the router can send packets, $A$ mean it supports the new address space, and $L$ mean the latest release is installed. The conditions are
> $$P\to A,\qquad A\to L,\qquad L\to P,\qquad \neg A.$$
> They are **consistent**, but every value is forced. From $\neg A$ and $P\to A$, infer $\neg P$; from $\neg P$ and $L\to P$, infer $\neg L$. The unique satisfying assignment is $(P,A,L)=(F,F,F)$.

#### D.4

> [!NOTE]- Solution
> Let $L$ mean the file system is not locked, $Q$ mean new messages are queued, $N$ mean the system is functioning normally, and $B$ mean messages are sent to the buffer. The conditions are
> $$L\to Q,\qquad L\leftrightarrow N,\qquad \neg Q\to B,\qquad L\to B,\qquad \neg B.$$
> From $\neg B$ and $L\to B$, infer $\neg L$. The biconditional gives $\neg N$. From $\neg B$ and $\neg Q\to B$, infer $Q$. The conditions are **consistent**, with forced assignment $(L,Q,N,B)=(F,T,F,F)$.

#### D.5

> [!NOTE]- Solution
> We model an invitation set as the set of people who attend. Let $J,S,K$ mean that Jasmine, Samir, and Kanti attend, and let $U$ mean Jasmine is unhappy. The conditions are
> $$(J\land S)\to U,\qquad S\to K,\qquad K\to J.$$
> Samir's attendance therefore requires Kanti and Jasmine, and Kanti's attendance requires Jasmine. The satisfying invitation/attendance sets are
> $$\varnothing,\qquad\{J\},\qquad\{J,K\},\qquad\{J,K,S\}.$$
> For each of the first three sets, $U$ may be either true or false; for $\{J,K,S\}$, $U$ must be true. Thus, for example, complete satisfying assignments are $(J,S,K,U)=(F,F,F,F),(T,F,F,F),(T,F,T,F),(T,T,T,T)$. The first condition does not forbid the last set. If avoiding Jasmine's unhappiness were an additional requirement, then $\{J,K,S\}$ would also be excluded.

## E. Derive logical equivalences with cited rules

> [!TIP]- Relevant materials
> - Rosen: [[Books/book_sections_md/1.3_Propositional_Equivalences|§1.3 — Propositional Equivalences]]
> - [Logical Equivalence Proofs handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3cLogicalEquivalenceLogicallyHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3cLogicalEquivalenceLogically.6.08.mp4)
>
> Each displayed step below uses one permitted rule. A rule may be used in either direction.

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** an equivalence chain beginning with the left-hand
> expression and ending with the right-hand expression, with exactly one permitted
> rule cited at each step. The chains below are not unique; shorter or longer valid
> chains earn full credit. **Decisive check:** after replacing implications, each
> expression should have the same disjunctive core as the target. Uncited changes
> of order or parentheses are not implicit: cite Commutative or Associative.

#### E.1

> [!NOTE]- Solution
> $$
> \begin{aligned}
> (p\to q)\land(p\to r)
> &\equiv(\neg p\lor q)\land(p\to r) &&\text{(Implication)}\\
> &\equiv(\neg p\lor q)\land(\neg p\lor r) &&\text{(Implication)}\\
> &\equiv\neg p\lor(q\land r) &&\text{(Distributive)}\\
> &\equiv p\to(q\land r) &&\text{(Implication).}
> \end{aligned}
> $$

#### E.2

> [!NOTE]- Solution
> $$
> \begin{aligned}
> (p\to r)\land(q\to r)
> &\equiv(\neg p\lor r)\land(q\to r) &&\text{(Implication)}\\
> &\equiv(\neg p\lor r)\land(\neg q\lor r) &&\text{(Implication)}\\
> &\equiv(r\lor\neg p)\land(\neg q\lor r) &&\text{(Commutative)}\\
> &\equiv(r\lor\neg p)\land(r\lor\neg q) &&\text{(Commutative)}\\
> &\equiv r\lor(\neg p\land\neg q) &&\text{(Distributive)}\\
> &\equiv(\neg p\land\neg q)\lor r &&\text{(Commutative)}\\
> &\equiv\neg(p\lor q)\lor r &&\text{(De Morgan)}\\
> &\equiv(p\lor q)\to r &&\text{(Implication).}
> \end{aligned}
> $$

#### E.3

> [!NOTE]- Solution
> $$
> \begin{aligned}
> (p\to q)\lor(p\to r)
> &\equiv(\neg p\lor q)\lor(p\to r) &&\text{(Implication)}\\
> &\equiv(\neg p\lor q)\lor(\neg p\lor r) &&\text{(Implication)}\\
> &\equiv((\neg p\lor q)\lor\neg p)\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor(q\lor\neg p))\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor(\neg p\lor q))\lor r &&\text{(Commutative)}\\
> &\equiv((\neg p\lor\neg p)\lor q)\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor q)\lor r &&\text{(Idempotent)}\\
> &\equiv\neg p\lor(q\lor r) &&\text{(Associative)}\\
> &\equiv p\to(q\lor r) &&\text{(Implication).}
> \end{aligned}
> $$

#### E.4

> [!NOTE]- Solution
> $$
> \begin{aligned}
> (p\to r)\lor(q\to r)
> &\equiv(\neg p\lor r)\lor(q\to r) &&\text{(Implication)}\\
> &\equiv(\neg p\lor r)\lor(\neg q\lor r) &&\text{(Implication)}\\
> &\equiv((\neg p\lor r)\lor\neg q)\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor(r\lor\neg q))\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor(\neg q\lor r))\lor r &&\text{(Commutative)}\\
> &\equiv((\neg p\lor\neg q)\lor r)\lor r &&\text{(Associative)}\\
> &\equiv(\neg p\lor\neg q)\lor(r\lor r) &&\text{(Associative)}\\
> &\equiv(\neg p\lor\neg q)\lor r &&\text{(Idempotent)}\\
> &\equiv\neg(p\land q)\lor r &&\text{(De Morgan)}\\
> &\equiv(p\land q)\to r &&\text{(Implication).}
> \end{aligned}
> $$

#### E.5

> [!NOTE]- Solution
> $$
> \begin{aligned}
> \neg p\to(q\to r)
> &\equiv\neg\neg p\lor(q\to r) &&\text{(Implication)}\\
> &\equiv p\lor(q\to r) &&\text{(Double Negation)}\\
> &\equiv p\lor(\neg q\lor r) &&\text{(Implication)}\\
> &\equiv(p\lor\neg q)\lor r &&\text{(Associative)}\\
> &\equiv(\neg q\lor p)\lor r &&\text{(Commutative)}\\
> &\equiv\neg q\lor(p\lor r) &&\text{(Associative)}\\
> &\equiv q\to(p\lor r) &&\text{(Implication).}
> \end{aligned}
> $$
