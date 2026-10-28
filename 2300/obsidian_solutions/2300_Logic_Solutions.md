---
title: 2300 Logic Solutions
aliases:
  - 2300 Logic Solutions
  - Logic Solutions
linter-yaml-title-alias: 2300 Logic Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Thursday, October 22nd 2026
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

> [!TIP] How to study from these solutions
> First cover the displayed answer and try the problem yourself. Then compare
> your work one step at a time: **translate or define**, **apply one rule**, and
> **check the result**. The explanatory steps below are intentionally more
> detailed than a timed Core response needs to be.

## A. Construct and interpret truth tables

> [!TIP]- Relevant materials
> - [Logic companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/logic_core_companion.pdf)
> - Rosen: [[Books/book_sections_md/1.1_Propositional_Logic|§1.1 — Propositional Logic]] and [[Books/book_sections_md/1.3_Propositional_Equivalences|§1.3 — Propositional Equivalences]]
> - [Truth Tables handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1dTruthTablesHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.1dTruthTables.10.47.mp4)
> - [Logical Equivalence Using Truth Tables handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3bLogicalEquivalenceTruthTableHandout.pdf) and [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.3bLogicalEquivalenceTruthTable.9.07.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** all eight valuations, correct useful intermediate
> columns, the correct final column, and the classification. Any consistent row
> order is acceptable. **Decisive check:** inspect the final column first; it must
> have exactly the pattern shown below and support the stated classification.

#### A.1


> [!QUESTION]- Full question statement
> **Common directions for A.1–A.5.** Construct a complete eight-row truth
> table. Show useful intermediate columns and classify the final proposition as
> a tautology, contradiction, or contingency.
>
> $$
>
> p\to(\neg q\lor r)
>
> $$

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
> **How the table was built:** compute $\neg q\lor r$ first, and only then the
> implication. An implication is false only when its antecedent is T and its
> consequent is F, which happens only on the second row.
> The final column contains both truth values, so this is a **contingency**.

#### A.2


> [!QUESTION]- Full question statement
> **Common directions for A.1–A.5.** Construct a complete eight-row truth
> table. Show useful intermediate columns and classify the final proposition as
> a tautology, contradiction, or contingency.
>
> $$
>
> \neg p\to(q\to r)
>
> $$

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
> **How the table was built:** compute $\neg p$ and $q\to r$ separately.
> The outer implication can be false only when $\neg p$ is T and $q\to r$ is
> F. That requires $p=F,q=T,r=F$, exactly the sixth row.
> This is a **contingency**.

#### A.3


> [!QUESTION]- Full question statement
> **Common directions for A.1–A.5.** Construct a complete eight-row truth
> table. Show useful intermediate columns and classify the final proposition as
> a tautology, contradiction, or contingency.
>
> $$
>
> (p\to q)\lor(\neg p\to r)
>
> $$

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
> **Why every row is true:** if $p$ is T, then $\neg p\to r$ has a false
> antecedent and is true. If $p$ is F, then $p\to q$ has a false antecedent
> and is true. Thus at least one side of the disjunction is true in every row.
> The final proposition $(p\to q)\lor(\neg p\to r)$ is always true, so it is a **tautology**.

#### A.4


> [!QUESTION]- Full question statement
> **Common directions for A.1–A.5.** Construct a complete eight-row truth
> table. Show useful intermediate columns and classify the final proposition as
> a tautology, contradiction, or contingency.
>
> $$
>
> (p\to q)\land(\neg p\to r)
>
> $$

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
> **How to check the final column:** a conjunction is true only when both
> implication columns are true. For example, on row 3 the left implication is
> false, so the conjunction is false even though the right implication is true.
> The final proposition $(p\to q)\land(\neg p\to r)$ is a **contingency**.

#### A.5


> [!QUESTION]- Full question statement
> **Common directions for A.1–A.5.** Construct a complete eight-row truth
> table. Show useful intermediate columns and classify the final proposition as
> a tautology, contradiction, or contingency.
>
> $$
>
> (p\leftrightarrow q)\lor(\neg q\leftrightarrow r)
>
> $$

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
> **How to check the biconditionals:** $p\leftrightarrow q$ is true when $p$
> and $q$ match; $\neg q\leftrightarrow r$ is true when $\neg q$ and $r$
> match. The final disjunction is false only when both comparisons fail.
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


> [!QUESTION]- Full question statement
> **Common directions for B.1–B.5.** Each problem has three parts:
> (a) translate conditional language into propositional logic; (b) translate
> between English and predicate logic; and (c) diagnose a proposed translation.
> Define every predicate and domain not already supplied. For part (c), say
> whether the proposal is correct, repair it if needed, and explain the error in
> one sentence.
>
> - **(a)** Let $e$ mean “you can edit a protected encyclopedia entry” and $a$
> mean “you are an administrator.” Translate: “You cannot edit a
> protected entry unless you are an administrator.”
> - **(b)** Let $Q(x,y)$ mean “student $x$ sent a message to student $y$.”
> Translate $\exists x\,\forall y\,Q(x,y)$ into ordinary English.
> - **(c)** A student says the formula in (b) means “Every student sent a message
> to at least one student.” Diagnose the claim.

> [!NOTE]- Solution
> - **(a)** “$\neg e$ unless $a$” is $\neg a\to\neg e$: without administrator
>   status, editing is impossible. Taking the contrapositive gives the cleaner
>   equivalent form $e\to a$.
> - **(b)** Both variables range over students. Read the quantifiers from left to right. $\exists x$ chooses one
>   student; $\forall y$ then requires that same student to message every
>   student. Thus: **There is a student who sent a message to every student.**
> - **(c)** The proposal is incorrect. “Every student sent a message to at
>   least one student” first chooses every sender and then permits a recipient
>   to depend on that sender: $\forall x\,\exists y\,Q(x,y)$. That is a
>   different quantifier order and a different claim.

#### B.2


> [!QUESTION]- Full question statement
> **Common directions for B.1–B.5.** Each problem has three parts:
> (a) translate conditional language into propositional logic; (b) translate
> between English and predicate logic; and (c) diagnose a proposed translation.
> Define every predicate and domain not already supplied. For part (c), say
> whether the proposal is correct, repair it if needed, and explain the error in
> one sentence.
>
> - **(a)** Let $m$ mean “you can see the movie,” $e$ mean “you are over 18,”
> and $p$ mean “you have parental permission.” Translate: “You can
> see the movie only if you are over 18 or have parental permission.”
> - **(b)** With $Q(x,y)$ as in B.1, translate $\forall x\,\exists y\,Q(x,y)$
> into ordinary English.
> - **(c)** A student translates “One student sent a message to every student”
> as $\forall y\,\exists x\,Q(x,y)$. Diagnose the translation.

> [!NOTE]- Solution
> - **(a)** “Only if” points toward the necessary condition. Seeing the movie
>   requires at least one of the two permissions, so $m\to(e\lor p)$.
> - **(b)** Both variables range over students, and $Q(x,y)$ means that $x$
>   sent a message to $y$. $\forall x$ chooses each student as sender; for that sender,
>   $\exists y$ supplies at least one recipient. Thus: **Every student sent a
>   message to at least one student.**
> - **(c)** $\forall y\,\exists x\,Q(x,y)$ says every student $y$ received a
>   message from some sender $x$; the sender may vary. “One student sent a
>   message to every student” instead needs one fixed sender:
>   $\exists x\,\forall y\,Q(x,y)$.

#### B.3


> [!QUESTION]- Full question statement
> **Common directions for B.1–B.5.** Each problem has three parts:
> (a) translate conditional language into propositional logic; (b) translate
> between English and predicate logic; and (c) diagnose a proposed translation.
> Define every predicate and domain not already supplied. For part (c), say
> whether the proposal is correct, repair it if needed, and explain the error in
> one sentence.
>
> - **(a)** Let $g$ mean “you can graduate,” $r$ mean “you completed your major
> requirements,” $m$ mean “you owe the university money,” and $b$
> mean “you have an overdue library book.” Translate: “You can
> graduate only if you completed the requirements, owe no money, and
> have no overdue library book.”
> - **(b)** Let $P(x,y)$ mean “student $x$ has taken computer-science course
> $y$.” Translate $\exists y\,\forall x\,P(x,y)$ into English.
> - **(c)** A student instead writes $\forall x\,\exists y\,P(x,y)$ for the
> sentence in (b). Diagnose the change in meaning.

> [!NOTE]- Solution
> - **(a)** Graduation is the claim with three necessary conditions. Put all
>   three in the consequent, negating the two prohibited conditions:
>   $g\to(r\land\neg m\land\neg b)$.
> - **(b)** Here $x$ ranges over students and $y$ over computer-science courses.
>   $\exists y$ fixes one computer-science course before $\forall x$
>   ranges over students. Thus: **There is a computer-science course that every
>   student has taken.**
> - **(c)** $\forall x\,\exists y\,P(x,y)$ instead lets the course $y$ depend
>   on the student $x$. It says every student has taken at least one course,
>   possibly a different course for each student, and does not guarantee a
>   common course.

#### B.4


> [!QUESTION]- Full question statement
> **Common directions for B.1–B.5.** Each problem has three parts:
> (a) translate conditional language into propositional logic; (b) translate
> between English and predicate logic; and (c) diagnose a proposed translation.
> Define every predicate and domain not already supplied. For part (c), say
> whether the proposal is correct, repair it if needed, and explain the error in
> one sentence.
>
> - **(a)** Let $w$ mean “you may use the airport wireless network,” $d$ mean
> “you pay the daily fee,” and $s$ mean “you subscribe to the
> service.” Translate: “To use the network, you must pay the daily fee
> unless you are a subscriber.”
> - **(b)** Let $L(x,y)$ mean “person $x$ loves person $y$.” Translate
> “Everybody loves somebody.”
> - **(c)** A student claims that $\exists y\,\forall x\,L(x,y)$ is an equivalent
> translation of (b). Diagnose the claim.

> [!NOTE]- Solution
> - **(a)** If you use the network and are not a subscriber, you must pay:
>   $w\land\neg s\to d$. Rewriting the requirement as a condition for using
>   the network gives the equivalent $w\to(d\lor s)$.
> - **(b)** Both variables range over people. For every person $x$, choose at least one person $y$ loved by $x$:
>   $\forall x\,\exists y\,L(x,y)$.
> - **(c)** $\exists y\,\forall x\,L(x,y)$ chooses one person $y$ first and
>   says everybody loves that same person. The original allows the loved person
>   to vary with $x$.

#### B.5


> [!QUESTION]- Full question statement
> **Common directions for B.1–B.5.** Each problem has three parts:
> (a) translate conditional language into propositional logic; (b) translate
> between English and predicate logic; and (c) diagnose a proposed translation.
> Define every predicate and domain not already supplied. For part (c), say
> whether the proposal is correct, repair it if needed, and explain the error in
> one sentence.
>
> - **(a)** Let $p$ mean “the message is scanned for viruses” and $q$ mean “the
> message came from an unknown system.” Translate: “It is necessary to
> scan a message whenever it comes from an unknown system.”
> - **(b)** Let $S(x)$ mean “$x$ is a student,” $F(y)$ mean “$y$ is a faculty
> member,” and $A(x,y)$ mean “$x$ asked $y$ a question.” Translate:
> “Some student has asked every faculty member a question.”
> - **(c)** A student uses $A(y,x)$ in place of $A(x,y)$ in (b). Diagnose what the
> reversed argument order says.

> [!NOTE]- Solution
> - **(a)** “Whenever” introduces the sufficient condition: whenever $q$
>   occurs, $p$ must occur. Therefore $q\to p$.
> - **(b)** Over the domain of all people,
>   $$\exists x\bigl(S(x)\land\forall y(F(y)\to A(x,y))\bigr).$$
>   Here $\exists x$ selects one student. For every person $y$, the implication
>   restricts the requirement to faculty members; the same student $x$ must
>   have asked each such $y$ a question.
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


> [!QUESTION]- Full question statement
> **Common directions for C.1–C.5.** For (a), define predicates, symbolize
> the statement, negate it with no negation immediately before a quantifier, and
> translate the result into ordinary English. For (b), rewrite the given formula
> so that every negation appears immediately before a predicate.
>
> - **(a)** All dogs have fleas. The domain is all things.
> - **(b)** $\neg\exists y\,\exists x\,P(x,y)$

> [!NOTE]- Solution
> - **(a)** Let $D(x)$ mean “$x$ is a dog” and $F(x)$ mean “$x$ has fleas.”
>   First symbolize the original: $\forall x(D(x)\to F(x))$. Then negate and
>   push the negation inward:
>   $$\neg\forall x(D(x)\to F(x))
>   \equiv\exists x\neg(D(x)\to F(x))
>   \equiv\exists x(D(x)\land\neg F(x)).$$
>   In English: **Some dog does not have fleas.**
> - **(b)** Cross one quantifier at a time:
>   $$\neg\exists y\,\exists x\,P(x,y)
>   \equiv\forall y\,\neg\exists x\,P(x,y)
>   \equiv\forall y\,\forall x\,\neg P(x,y).$$

#### C.2


> [!QUESTION]- Full question statement
> **Common directions for C.1–C.5.** For (a), define predicates, symbolize
> the statement, negate it with no negation immediately before a quantifier, and
> translate the result into ordinary English. For (b), rewrite the given formula
> so that every negation appears immediately before a predicate.
>
> - **(a)** No monkey can speak French. The domain is all things.
> - **(b)** $\neg\forall x\,\exists y\,P(x,y)$

> [!NOTE]- Solution
> - **(a)** Let $M(x)$ mean “$x$ is a monkey” and $F(x)$ mean “$x$ can speak
>   French.” The original is $\forall x(M(x)\to\neg F(x))$. Therefore
>   $$\neg\forall x(M(x)\to\neg F(x))
>   \equiv\exists x\neg(M(x)\to\neg F(x))
>   \equiv\exists x(M(x)\land F(x)).$$
>   In English: **Some monkey can speak French.**
> - **(b)**
>   $$\neg\forall x\,\exists y\,P(x,y)
>   \equiv\exists x\,\neg\exists y\,P(x,y)
>   \equiv\exists x\,\forall y\,\neg P(x,y).$$

#### C.3


> [!QUESTION]- Full question statement
> **Common directions for C.1–C.5.** For (a), define predicates, symbolize
> the statement, negate it with no negation immediately before a quantifier, and
> translate the result into ordinary English. For (b), rewrite the given formula
> so that every negation appears immediately before a predicate.
>
> - **(a)** Some old dogs can learn new tricks. The domain is all things.
> - **(b)** $\neg\forall x\,\forall y\,P(x,y)$

> [!NOTE]- Solution
> - **(a)** Let $O(x)$ mean “$x$ is old,” $D(x)$ mean “$x$ is a dog,” and
>   $T(x)$ mean “$x$ can learn new tricks.” The original is
>   $\exists x(O(x)\land D(x)\land T(x))$. Negating gives
>   $$\forall x\neg(O(x)\land D(x)\land T(x))
>   \equiv\forall x(\neg O(x)\lor\neg D(x)\lor\neg T(x)).$$
>   Repackaging the same formula as an implication gives
>   $\forall x((O(x)\land D(x))\to\neg T(x))$: **No old dog can learn new
>   tricks.**
> - **(b)**
>   $$\neg\forall x\,\forall y\,P(x,y)
>   \equiv\exists x\,\neg\forall y\,P(x,y)
>   \equiv\exists x\,\exists y\,\neg P(x,y).$$

#### C.4


> [!QUESTION]- Full question statement
> **Common directions for C.1–C.5.** For (a), define predicates, symbolize
> the statement, negate it with no negation immediately before a quantifier, and
> translate the result into ordinary English. For (b), rewrite the given formula
> so that every negation appears immediately before a predicate.
>
> - **(a)** No one in this class knows both French and Russian. The domain is all
> people.
> - **(b)** $\neg\forall y\,\exists x\,P(x,y)$

> [!NOTE]- Solution
> - **(a)** Let $C(x)$ mean “$x$ is in this class,” $F(x)$ mean “$x$ knows
>   French,” and $R(x)$ mean “$x$ knows Russian.” The original is
>   $\forall x(C(x)\to\neg(F(x)\land R(x)))$. A counterexample must be in the
>   class and know both languages:
>   $$\neg\forall x(C(x)\to\neg(F(x)\land R(x)))
>   \equiv\exists x(C(x)\land F(x)\land R(x)).$$
>   In English: **Someone in this class knows both French and Russian.**
> - **(b)**
>   $$\neg\forall y\,\exists x\,P(x,y)
>   \equiv\exists y\,\neg\exists x\,P(x,y)
>   \equiv\exists y\,\forall x\,\neg P(x,y).$$

#### C.5


> [!QUESTION]- Full question statement
> **Common directions for C.1–C.5.** For (a), define predicates, symbolize
> the statement, negate it with no negation immediately before a quantifier, and
> translate the result into ordinary English. For (b), rewrite the given formula
> so that every negation appears immediately before a predicate.
>
> - **(a)** All Swedish movies are serious. The domain is all things.
> - **(b)** $\neg\forall y\,\forall x\bigl(P(x,y)\lor Q(x,y)\bigr)$

> [!NOTE]- Solution
> - **(a)** Let $W(x)$ mean “$x$ is a Swedish movie” and $S(x)$ mean “$x$
>   is serious.” The original is $\forall x(W(x)\to S(x))$. Therefore
>   $$\neg\forall x(W(x)\to S(x))
>   \equiv\exists x\neg(W(x)\to S(x))
>   \equiv\exists x(W(x)\land\neg S(x)).$$
>   In English: **Some Swedish movie is not serious.**
> - **(b)**
>   $$\neg\forall y\,\forall x(P(x,y)\lor Q(x,y))
>   \equiv\exists y\,\neg\forall x(P(x,y)\lor Q(x,y))
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


> [!QUESTION]- Full question statement
> **Common directions for D.1–D.5.** Define one atomic proposition for
> each simple statement and translate every condition. Determine whether the
> conditions are consistent. Give a satisfying assignment when one exists; when
> none exists, give a short contradiction. Complete the additional balancing
> request in the final sentence of each problem.
>
> The system is in multiuser state if and only if it is operating normally. If
> the system is operating normally, the kernel is functioning. The kernel is not
> functioning or the system is in interrupt mode. If the system is not in
> multiuser state, it is in interrupt mode. The system is not in interrupt mode.
> If the conditions are inconsistent, identify a minimal collection of the given
> conditions that already forces the contradiction.

> [!NOTE]- Solution
> Let $M$ mean multiuser state, $N$ mean operating normally, $K$ mean the kernel is functioning, and $I$ mean interrupt mode. The conditions are
> $$M\leftrightarrow N,\quad N\to K,\quad \neg K\lor I,\quad \neg M\to I,\quad \neg I.$$
> Follow the forced consequences:
>
> 1. From $\neg I$ and $\neg K\lor I$, Disjunctive Syllogism gives $\neg K$.
> 2. From $N\to K$ and $\neg K$, Modus Tollens gives $\neg N$.
> 3. The biconditional contains $M\to N$; with $\neg N$, Modus Tollens gives $\neg M$.
> 4. From $\neg M$ and $\neg M\to I$, Modus Ponens gives $I$.
> 5. Now both $I$ and $\neg I$ have been derived, so the conditions are
>    **inconsistent**.
>
> All five conditions form a minimal inconsistent collection: removing any one allows a satisfying assignment. Listed in condition order, witnesses after removing conditions 1 through 5 are
> $$(M,N,K,I)=(T,F,F,F),(T,T,F,F),(T,T,T,F),(F,F,F,F),(F,F,F,T).$$
> Each witness makes every remaining condition true, so no proper subcollection
> obtained by deleting one condition is already inconsistent.

#### D.2


> [!QUESTION]- Full question statement
> **Common directions for D.1–D.5.** Define one atomic proposition for
> each simple statement and translate every condition. Determine whether the
> conditions are consistent. Give a satisfying assignment when one exists; when
> none exists, give a short contradiction. Complete the additional balancing
> request in the final sentence of each problem.
>
> Whenever system software is being upgraded, users cannot access the file
> system. If users can access the file system, they can save new files. If users
> cannot save new files, the software is not being upgraded. In addition to
> deciding consistency, list all satisfying assignments for the three atomic
> propositions.

> [!NOTE]- Solution
> Let $G$ mean software is being upgraded, $A$ mean users can access the file system, and $S$ mean users can save new files. The conditions are
> $$G\to\neg A,\qquad A\to S,\qquad \neg S\to\neg G.$$
> They are **consistent**. All satisfying assignments $(G,A,S)$ are
> $$(T,F,T),\quad(F,F,F),\quad(F,F,T),\quad(F,T,T).$$
> To see why the list is complete, split into cases. If $G=T$, the first
> condition forces $A=F$, while the contrapositive of the third forces $S=T$;
> this gives one model. If $G=F$, the first and third conditions are already
> true, so only $A\to S$ matters: $(A,S)=(T,F)$ is excluded and the other
> three pairs work. Direct substitution checks every listed model.

#### D.3


> [!QUESTION]- Full question statement
> **Common directions for D.1–D.5.** Define one atomic proposition for
> each simple statement and translate every condition. Determine whether the
> conditions are consistent. Give a satisfying assignment when one exists; when
> none exists, give a short contradiction. Complete the additional balancing
> request in the final sentence of each problem.
>
> The router can send packets to the edge system only if it supports the new
> address space. Supporting the new address space requires the latest software
> release. If the latest software release is installed, the router can send
> packets to the edge system. The router does not support the new address space.
> In addition to deciding consistency, determine which truth values are forced.

> [!NOTE]- Solution
> Let $P$ mean the router can send packets, $A$ mean it supports the new address space, and $L$ mean the latest release is installed. The conditions are
> $$P\to A,\qquad A\to L,\qquad L\to P,\qquad \neg A.$$
> They are **consistent**, but every value is forced:
>
> 1. $\neg A$ is given.
> 2. From $P\to A$ and $\neg A$, Modus Tollens gives $\neg P$.
> 3. From $L\to P$ and $\neg P$, Modus Tollens gives $\neg L$.
> 4. Substituting $(P,A,L)=(F,F,F)$ makes all three implications true, because
>    each has a false antecedent, and it also satisfies $\neg A$.
>
> Hence this is the unique satisfying assignment.

#### D.4


> [!QUESTION]- Full question statement
> **Common directions for D.1–D.5.** Define one atomic proposition for
> each simple statement and translate every condition. Determine whether the
> conditions are consistent. Give a satisfying assignment when one exists; when
> none exists, give a short contradiction. Complete the additional balancing
> request in the final sentence of each problem.
>
> If the file system is not locked, new messages are queued. The file system is
> not locked if and only if the system is functioning normally. If messages are
> not queued, they are sent to the message buffer. If the file system is not
> locked, messages are sent to the buffer. Messages are not sent to the buffer.
> In addition to deciding consistency, explain which conclusions follow from the
> last condition.

> [!NOTE]- Solution
> Let $L$ mean the file system is not locked, $Q$ mean new messages are queued, $N$ mean the system is functioning normally, and $B$ mean messages are sent to the buffer. The conditions are
> $$L\to Q,\qquad L\leftrightarrow N,\qquad \neg Q\to B,\qquad L\to B,\qquad \neg B.$$
> Work backward from the final fact:
>
> 1. From $\neg B$ and $L\to B$, Modus Tollens gives $\neg L$.
> 2. The biconditional contains $N\to L$; from $\neg L$, Modus Tollens gives
>    $\neg N$.
> 3. From $\neg B$ and $\neg Q\to B$, Modus Tollens gives
>    $\neg\neg Q$, hence $Q$.
> 4. Substitution shows $(L,Q,N,B)=(F,T,F,F)$ satisfies all five conditions.
>
> Therefore the conditions are **consistent**, and all four truth values are
> forced.

#### D.5


> [!QUESTION]- Full question statement
> **Common directions for D.1–D.5.** Define one atomic proposition for
> each simple statement and translate every condition. Determine whether the
> conditions are consistent. Give a satisfying assignment when one exists; when
> none exists, give a short contradiction. Complete the additional balancing
> request in the final sentence of each problem.
>
> Jasmine becomes unhappy if she attends a party with Samir. Samir attends only
> if Kanti attends. Kanti will not attend unless Jasmine attends. Determine which
> subsets of Jasmine, Samir, and Kanti can be invited without violating these
> conditions. State every satisfying combination, including the possibility of
> inviting no one.

> [!NOTE]- Solution
> We model an invitation set as the set of people who attend. Let $J,S,K$ mean that Jasmine, Samir, and Kanti attend, and let $U$ mean Jasmine is unhappy. The conditions are
> $$(J\land S)\to U,\qquad S\to K,\qquad K\to J.$$
> The last two implications determine the allowed attendance patterns. If
> $S=T$, then $K=T$, and then $J=T$. If $K=T$, then $J=T$. If both $S$ and
> $K$ are false, $J$ may be either false or true. These cases give exactly
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


> [!QUESTION]- Full question statement
> Give a chain of equivalences from the left-hand expression to the right-hand
> expression. Cite exactly one rule at every step. Each rule may be used in either
> direction.
> - **Implication:** $a\to b\equiv\neg a\lor b$.
> - **Double Negation:** $\neg\neg a\equiv a$.
> - **De Morgan:**
> $\neg(a\lor b)\equiv\neg a\land\neg b$ and
> $\neg(a\land b)\equiv\neg a\lor\neg b$.
> - **Distributive:**
> $a\lor(b\land c)\equiv(a\lor b)\land(a\lor c)$ and
> $a\land(b\lor c)\equiv(a\land b)\lor(a\land c)$.
> - **Associative:**
> $(a\lor b)\lor c\equiv a\lor(b\lor c)$ and
> $(a\land b)\land c\equiv a\land(b\land c)$.
> - **Commutative:**
> $a\lor b\equiv b\lor a$ and $a\land b\equiv b\land a$.
> - **Idempotent:**
> $a\lor a\equiv a$ and $a\land a\equiv a$.
> Changing parentheses requires Associative; changing order requires
> Commutative.
>
> Show that
>
> $$
>
> (p\to q)\land(p\to r)
> \quad\text{and}\quad
> p\to(q\land r)
>
> $$
>
> are logically equivalent.

> [!NOTE]- Solution
> **Plan:** eliminate both implications, factor the common disjunct $\neg p$,
> and then rebuild the target implication.
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


> [!QUESTION]- Full question statement
> Give a chain of equivalences from the left-hand expression to the right-hand
> expression. Cite exactly one rule at every step. Each rule may be used in either
> direction.
> - **Implication:** $a\to b\equiv\neg a\lor b$.
> - **Double Negation:** $\neg\neg a\equiv a$.
> - **De Morgan:**
> $\neg(a\lor b)\equiv\neg a\land\neg b$ and
> $\neg(a\land b)\equiv\neg a\lor\neg b$.
> - **Distributive:**
> $a\lor(b\land c)\equiv(a\lor b)\land(a\lor c)$ and
> $a\land(b\lor c)\equiv(a\land b)\lor(a\land c)$.
> - **Associative:**
> $(a\lor b)\lor c\equiv a\lor(b\lor c)$ and
> $(a\land b)\land c\equiv a\land(b\land c)$.
> - **Commutative:**
> $a\lor b\equiv b\lor a$ and $a\land b\equiv b\land a$.
> - **Idempotent:**
> $a\lor a\equiv a$ and $a\land a\equiv a$.
> Changing parentheses requires Associative; changing order requires
> Commutative.
>
> Show that
>
> $$
>
> (p\to r)\land(q\to r)
> \quad\text{and}\quad
> (p\lor q)\to r
>
> $$
>
> are logically equivalent.

> [!NOTE]- Solution
> **Plan:** after eliminating implications, put the common $r$ in the same
> position, factor it, and use De Morgan to create $\neg(p\lor q)$.
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


> [!QUESTION]- Full question statement
> Give a chain of equivalences from the left-hand expression to the right-hand
> expression. Cite exactly one rule at every step. Each rule may be used in either
> direction.
> - **Implication:** $a\to b\equiv\neg a\lor b$.
> - **Double Negation:** $\neg\neg a\equiv a$.
> - **De Morgan:**
> $\neg(a\lor b)\equiv\neg a\land\neg b$ and
> $\neg(a\land b)\equiv\neg a\lor\neg b$.
> - **Distributive:**
> $a\lor(b\land c)\equiv(a\lor b)\land(a\lor c)$ and
> $a\land(b\lor c)\equiv(a\land b)\lor(a\land c)$.
> - **Associative:**
> $(a\lor b)\lor c\equiv a\lor(b\lor c)$ and
> $(a\land b)\land c\equiv a\land(b\land c)$.
> - **Commutative:**
> $a\lor b\equiv b\lor a$ and $a\land b\equiv b\land a$.
> - **Idempotent:**
> $a\lor a\equiv a$ and $a\land a\equiv a$.
> Changing parentheses requires Associative; changing order requires
> Commutative.
>
> Show that
>
> $$
>
> (p\to q)\lor(p\to r)
> \quad\text{and}\quad
> p\to(q\lor r)
>
> $$
>
> are logically equivalent.

> [!NOTE]- Solution
> **Plan:** eliminate the implications, use Associative and Commutative to
> bring the two copies of $\neg p$ together, remove the duplicate with
> Idempotent, and rebuild the implication.
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


> [!QUESTION]- Full question statement
> Give a chain of equivalences from the left-hand expression to the right-hand
> expression. Cite exactly one rule at every step. Each rule may be used in either
> direction.
> - **Implication:** $a\to b\equiv\neg a\lor b$.
> - **Double Negation:** $\neg\neg a\equiv a$.
> - **De Morgan:**
> $\neg(a\lor b)\equiv\neg a\land\neg b$ and
> $\neg(a\land b)\equiv\neg a\lor\neg b$.
> - **Distributive:**
> $a\lor(b\land c)\equiv(a\lor b)\land(a\lor c)$ and
> $a\land(b\lor c)\equiv(a\land b)\lor(a\land c)$.
> - **Associative:**
> $(a\lor b)\lor c\equiv a\lor(b\lor c)$ and
> $(a\land b)\land c\equiv a\land(b\land c)$.
> - **Commutative:**
> $a\lor b\equiv b\lor a$ and $a\land b\equiv b\land a$.
> - **Idempotent:**
> $a\lor a\equiv a$ and $a\land a\equiv a$.
> Changing parentheses requires Associative; changing order requires
> Commutative.
>
> Show that
>
> $$
>
> (p\to r)\lor(q\to r)
> \quad\text{and}\quad
> (p\land q)\to r
>
> $$
>
> are logically equivalent.

> [!NOTE]- Solution
> **Plan:** eliminate the implications, collect the two copies of $r$, remove
> the duplicate, and convert $\neg p\lor\neg q$ to $\neg(p\land q)$.
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


> [!QUESTION]- Full question statement
> Give a chain of equivalences from the left-hand expression to the right-hand
> expression. Cite exactly one rule at every step. Each rule may be used in either
> direction.
> - **Implication:** $a\to b\equiv\neg a\lor b$.
> - **Double Negation:** $\neg\neg a\equiv a$.
> - **De Morgan:**
> $\neg(a\lor b)\equiv\neg a\land\neg b$ and
> $\neg(a\land b)\equiv\neg a\lor\neg b$.
> - **Distributive:**
> $a\lor(b\land c)\equiv(a\lor b)\land(a\lor c)$ and
> $a\land(b\lor c)\equiv(a\land b)\lor(a\land c)$.
> - **Associative:**
> $(a\lor b)\lor c\equiv a\lor(b\lor c)$ and
> $(a\land b)\land c\equiv a\land(b\land c)$.
> - **Commutative:**
> $a\lor b\equiv b\lor a$ and $a\land b\equiv b\land a$.
> - **Idempotent:**
> $a\lor a\equiv a$ and $a\land a\equiv a$.
> Changing parentheses requires Associative; changing order requires
> Commutative.
>
> Show that
>
> $$
>
> \neg p\to(q\to r)
> \quad\text{and}\quad
> q\to(p\lor r)
>
> $$
>
> are logically equivalent.

> [!NOTE]- Solution
> **Plan:** eliminate the outer implication first. Double negation produces
> $p$; eliminate the inner implication, move $\neg q$ to the front one named
> rule at a time, and then rebuild the target implication.
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
