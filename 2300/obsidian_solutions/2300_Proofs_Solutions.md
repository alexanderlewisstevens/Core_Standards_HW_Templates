---
title: 2300 Proofs Solutions
aliases: [2300 Proofs Solutions, Proofs Solutions]
linter-yaml-title-alias: 2300 Proofs Solutions
date created: Monday, March 9th 2026, 2:29:50 pm
date modified: Thursday, October 22nd 2026
publish: true
permalink: core-assessment-solutions/2300-proofs-solutions
---
# 2300 Proofs Solutions

This public page contains solutions for the Proofs practice variants; it does not reveal a live assessment form. A supervised attempt lasts 20 minutes and contains five problems, one from each section A–E. Each labeled problem is one scoring unit, including all required parts. Four fully correct problems earn **Meets**; five earn **Exceeds**. Every retake uses a complete new five-problem form.

> [!IMPORTANT] Full-credit and grader guidance
> A proof need not copy the model solution. Any logically valid proof using the
> requested method earns full credit. Equivalent variable names and different
> valid witnesses are acceptable. Each **decisive check** below identifies the
> step a grader should locate first; all requested parts must still be present.

## How to read and write these proofs

Each solution below separates the work into the same four moves students should
make on paper:

1. **Set up the claim:** name arbitrary objects, hypotheses, or the proof method.
2. **Use the definition or rule:** introduce witnesses and cite the legal step.
3. **Do the decisive work:** calculate, split into cases, or derive the contradiction.
4. **Close the proof:** identify the new witness or state exactly why the original
   claim follows.

The last sentence is not decoration: it connects the calculations back to the
definition or claim being proved.

## A. Inference and Proof Structure (1.6)

> [!TIP]- Relevant Materials
> - [Proofs companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/proofs_core_companion.pdf)
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen 1.6 — Rules of Inference]]
> - [Full chapter resource page](https://cs.du.edu/~ftl/2300/resources/)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the requested conclusion, named inference rules,
> and every requested diagnosis/countermodel. A shorter valid derivation is fine.
> **Decisive check:** existential instantiation must not reuse an unlicensed common
> witness, and universal generalization must begin with an arbitrary object.

#### A.1

> [!QUESTION]- Full question statement
> Suppose that if the server is overloaded, requests are delayed; if requests are
> delayed, the monitoring system sends an alert; and the server is overloaded.
> Derive that the monitoring system sends an alert, naming the rule used at each
> step.

> [!NOTE]- Solution
> **Step 1: symbolize.** Let $O$ mean the server is overloaded, $D$ mean
> requests are delayed, and $A$ mean an alert is sent. The premises are
> $O\to D$, $D\to A$, and $O$.
>
> **Step 2: use the first conditional.** From $O\to D$ and $O$, infer $D$ by
> **modus ponens**.
>
> **Step 3: use the second conditional.** From $D\to A$ and the newly derived
> $D$, infer $A$ by **modus ponens**. Thus the monitoring system sends an alert.
> Equivalently, hypothetical syllogism first gives $O\to A$, followed by one
> application of modus ponens.

#### A.2

> [!QUESTION]- Full question statement
> Determine whether each argument is valid. Name the valid inference rule or the invalid form.
> - (a) If the program compiles, then it has no syntax errors. It has no syntax errors. Therefore, it compiles.
> - (b) If the network is down, then the site is unavailable. The site is
> available. Therefore, the network is not down.

**(a)**

> [!NOTE]- Solution
> **Invalid: affirming the consequent.** The premise has the form $p\to q$, and
> the argument uses $q$ to conclude $p$. That direction is not licensed. For a
> counterexample, a program may have no syntax errors but still fail to compile
> because a dependency is missing. Then both premises are true while the
> conclusion is false.

**(b)**

> [!NOTE]- Solution
> **Valid: modus tollens.** Write the premises as $p\to q$ and $\neg q$, where
> $p$ is “the network is down” and $q$ is “the site is unavailable.” Modus
> tollens gives $\neg p$: the network is not down.

#### A.3

> [!QUESTION]- Full question statement
> Over one common domain, identify the error in the proposed inference. Then give
> a two-element domain and interpretations of $P$ and $Q$ that make both premises
> true and the conclusion false.
>
> $$
>
> \exists x\,P(x),\qquad \exists x\,Q(x)
> \quad\therefore\quad
> \exists x\,(P(x)\land Q(x)).
>
> $$

> [!NOTE]- Solution
> **Step 1: locate the gap.** The two existential premises may use different
> witnesses; neither premise says that one object has both properties.
>
> **Step 2: build a countermodel.** Let the domain be $\{a,b\}$. Make $P$ true
> only of $a$, and make $Q$ true only of $b$.
>
> **Step 3: check every statement.** The witness $a$ makes $\exists xP(x)$
> true, and $b$ makes $\exists xQ(x)$ true. But $P(a)\land Q(a)$ is false and
> $P(b)\land Q(b)$ is false. Therefore no object satisfies both predicates,
> so $\exists x(P(x)\land Q(x))$ is false. True premises with a false
> conclusion prove that the inference is invalid.

#### A.4

> [!QUESTION]- Full question statement
> From $p\to q$, $q\to r$, and $\neg r$, derive $\neg p$. Name the rule used at
> each step.

> [!NOTE]- Solution
> Work backward through the conditional chain:
>
> 1. $q\to r$ and $\neg r$ give $\neg q$ by **modus tollens**.
> 2. $p\to q$ and $\neg q$ give $\neg p$ by **modus tollens**.
>
> Hence $\neg p$ follows. Another correct route is to derive $p\to r$ by
> hypothetical syllogism and then combine it with $\neg r$ by modus tollens.

#### A.5

> [!QUESTION]- Full question statement
> Over a nonempty domain, use the premises
> $\forall x\,(P(x)\to Q(x))$ and $\forall x\,P(x)$ to derive
> $\forall x\,Q(x)$. Name the rule used at each step.

> [!NOTE]- Solution
> **Step 1: choose an arbitrary object.** Let $c$ be any object in the domain;
> do not give $c$ a special property.
>
> **Step 2: instantiate both universal premises.** Universal instantiation gives
> $P(c)\to Q(c)$ and $P(c)$.
>
> **Step 3: infer the property.** Modus ponens gives $Q(c)$.
>
> **Step 4: generalize.** Because $c$ was arbitrary, universal generalization
> gives $\forall x\,Q(x)$. The arbitrary choice of $c$ is what makes this final
> step legal.

## B. Direct Proofs (1.7)

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.7_Introduction_to_Proofs|Rosen 1.7 — Introduction to Proofs]]
> - [Direct Proofs handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7aDirectProofsHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7aDirectProofs.9.10.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** begin from the definition in the hypothesis, perform
> valid algebra or an element argument, and finish with the exact definition in the
> conclusion. **Decisive check:** the final expression must display the required
> integer witness (such as $2t$) or the arbitrary element in the target set.

#### B.1

> [!QUESTION]- Full question statement
> Give a direct proof that if an integer $n$ is even, then $n^2$ is even.

> [!NOTE]- Solution
> Let $n$ be an arbitrary even integer. By definition, $n=2k$ for some
> $k\in\mathbb Z$. Substitute this form and factor out a $2$:
> $$n^2=(2k)^2=4k^2=2(2k^2).$$
> The quantity $2k^2$ is an integer, so this displays $n^2$ in the form
> $2(\text{integer})$. Therefore $n^2$ is even by definition.

#### B.2

> [!QUESTION]- Full question statement
> Give a direct proof that the sum of two rational numbers is rational.

> [!NOTE]- Solution
> Let $x$ and $y$ be arbitrary rational numbers. By definition, choose
> integers $a,b,c,d$ with $b\ne0$, $d\ne0$, $x=a/b$, and $y=c/d$. Use a
> common denominator:
> $$x+y=\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd}.$$
> Since integers are closed under multiplication and addition, $ad+bc$ and
> $bd$ are integers. Also, $bd\ne0$ because neither factor is zero. Thus the
> displayed fraction satisfies the definition of a rational number, so
> $x+y\in\mathbb Q$.

#### B.3

> [!QUESTION]- Full question statement
> Give a direct proof that the sum of two odd integers is even.

> [!NOTE]- Solution
> Let $a$ and $b$ be arbitrary odd integers. Use separate witnesses:
> $a=2j+1$ and $b=2k+1$ for some $j,k\in\mathbb Z$. Then
> $$a+b=(2j+1)+(2k+1)=2j+2k+2=2(j+k+1).$$
> Because $j+k+1\in\mathbb Z$, the sum has the form $2(\text{integer})$.
> Hence $a+b$ is even.

#### B.4

> [!QUESTION]- Full question statement
> Give a direct proof that the difference of two even integers is even.

> [!NOTE]- Solution
> Let $a$ and $b$ be arbitrary even integers. Then $a=2j$ and $b=2k$ for
> some (possibly different) integers $j$ and $k$. Subtract and factor:
> $$a-b=2j-2k=2(j-k).$$
> Integers are closed under subtraction, so $j-k\in\mathbb Z$. Thus $a-b$
> has the form $2(\text{integer})$ and is even.

#### B.5

> [!QUESTION]- Full question statement
> Let $A,B,C$ be sets. Give a direct element proof that if $A\subseteq B$, then
> $A\cap C\subseteq B\cap C$.

> [!NOTE]- Solution
> Assume $A\subseteq B$. To prove a subset claim, start with an arbitrary
> element of the set on the left: let $x\in A\cap C$. By the definition of
> intersection, $x\in A$ and $x\in C$. Since $A\subseteq B$, the first fact
> gives $x\in B$. We now have both $x\in B$ and $x\in C$, so
> $x\in B\cap C$. Because the argument works for every $x\in A\cap C$, we
> conclude $A\cap C\subseteq B\cap C$.

## C. Contraposition and Contradiction (1.7)

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.7_Introduction_to_Proofs|Rosen 1.7 — Introduction to Proofs]]
> - [Proof by Contrapositive handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7bProofByContrapositiveHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7bProofByContrapositive.6.42.mp4)
> - [Proof by Contradiction handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7cProofByContradictionHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7cProofByContradiction.7.26.mp4)
> - [Conditional proof by contradiction handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7eProofByContradictionConditionalHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7eProofByContradictionConditional.10.15.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** explicitly state the contrapositive or contradiction
> assumption, derive the needed parity/form or a genuine contradiction, and return
> to the original claim. An equivalent contradiction is acceptable. **Decisive
> check:** the proof must use the logically correct negation of the target, not its
> converse or the original conclusion as an assumption.

#### C.1

> [!QUESTION]- Full question statement
> Let $m,n\in\mathbb Z$. Prove by contraposition that if $mn$ is odd, then both
> $m$ and $n$ are odd. Your proof must state the contrapositive explicitly and
> handle its disjunction by cases.

> [!NOTE]- Solution
> **Step 1: write the contrapositive.** The negation of “both $m$ and $n$ are
> odd” is “$m$ is even or $n$ is even.” Thus prove: if $m$ is even or $n$ is
> even, then $mn$ is even.
>
> **Step 2: handle both possibilities.** If $m=2k$, then
> $mn=(2k)n=2(kn)$, and $kn\in\mathbb Z$. If $n=2\ell$, then
> $mn=m(2\ell)=2(m\ell)$, and $m\ell\in\mathbb Z$.
>
> **Step 3: close the proof.** In either case $mn$ is twice an integer, so it
> is even. The contrapositive is true, and therefore the original implication
> is true.

#### C.2

> [!QUESTION]- Full question statement
> Prove by contraposition that if $3n+2$ is odd, then the integer $n$ is odd.

> [!NOTE]- Solution
> **Step 1:** The contrapositive is: if $n$ is even, then $3n+2$ is even.
>
> **Step 2:** Assume $n$ is even, so $n=2k$ for some $k\in\mathbb Z$. Then
> $$3n+2=3(2k)+2=6k+2=2(3k+1).$$
>
> **Step 3:** Since $3k+1\in\mathbb Z$, this is the defining form of an even
> integer. Thus the contrapositive holds, so the original implication follows.

#### C.3

> [!QUESTION]- Full question statement
> Prove by contradiction that there is no largest integer.

> [!NOTE]- Solution
> **Step 1: negate the conclusion.** Suppose, for contradiction, that a largest
> integer $N$ exists. This means every integer is at most $N$.
>
> **Step 2: construct a conflicting integer.** Because integers are closed under
> addition, $N+1$ is an integer. Also $N+1>N$.
>
> **Step 3: identify the contradiction.** The maximality assumption says
> $N+1\le N$, while arithmetic gives $N+1>N$. Therefore the assumption is
> impossible, and there is no largest integer.

#### C.4

> [!QUESTION]- Full question statement
> Let $r$ be rational and $x$ irrational. Prove by contradiction that $r+x$ is irrational.

> [!NOTE]- Solution
> **Step 1:** Assume the opposite of the desired conclusion: suppose $r+x$ is
> rational.
>
> **Step 2:** The given number $r$ is rational, and rational numbers are closed
> under subtraction. Therefore
> $$x=(r+x)-r$$
> would be rational.
>
> **Step 3:** This contradicts the hypothesis that $x$ is irrational. Hence the
> opposite assumption was false, and $r+x$ is irrational.

#### C.5

> [!QUESTION]- Full question statement
> Prove by contraposition that if $n^2$ is even, then the integer $n$ is even.

> [!NOTE]- Solution
> **Step 1:** Prove the contrapositive: if $n$ is odd, then $n^2$ is odd.
>
> **Step 2:** If $n$ is odd, write $n=2k+1$ for some $k\in\mathbb Z$. Then
> $$n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1.$$
>
> **Step 3:** Since $2k^2+2k\in\mathbb Z$, the square has the form
> $2(\text{integer})+1$ and is odd. This proves the contrapositive, so if
> $n^2$ is even then $n$ is even.

## D. Cases, Existence, and Counterexamples (1.7, 1.8)

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.7_Introduction_to_Proofs|Rosen 1.7 — Introduction to Proofs]]
> - [[Books/book_sections_md/1.8_Proof_Methods_and_Strategy|Rosen 1.8 — Proof Methods and Strategy]]
> - [Proof by Cases handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.8aProofByCasesHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.8aProofByCases.5.00.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** exhaustive cases with the conclusion in each case,
> or explicit witnesses/counterexamples with their required properties verified.
> Other valid examples earn full credit. **Decisive check:** cases must cover the
> whole domain; a counterexample must make the universal claim false, not merely
> illustrate an unusual case.

#### D.1

> [!QUESTION]- Full question statement
> Prove by cases that $n(n+1)$ is even for every integer $n$.

> [!NOTE]- Solution
> **Step 1: choose exhaustive cases.** Every integer is even or odd.
>
> **Case 1:** If $n=2k$, then
> $n(n+1)=2k(n+1)=2[k(n+1)]$. The bracketed quantity is an integer, so the
> product is even.
>
> **Case 2:** If $n=2k+1$, then $n+1=2k+2=2(k+1)$ and
> $n(n+1)=2[n(k+1)]$. Again the bracketed quantity is an integer, so the
> product is even.
>
> Because the cases cover every integer, $n(n+1)$ is even for every $n$.

#### D.2

> [!QUESTION]- Full question statement
> Prove by cases that $|x|\ge 0$ for every real number $x$, with equality exactly when $x=0$.

> [!NOTE]- Solution
> Use the two cases in the definition of absolute value.
>
> **Case 1:** If $x\ge0$, then $|x|=x\ge0$. Within this case,
> $|x|=0$ means $x=0$.
>
> **Case 2:** If $x<0$, then multiplying by $-1$ reverses the inequality, so
> $-x>0$. Since $|x|=-x$, absolute value is strictly positive and equality
> cannot occur.
>
> The cases are exhaustive. Hence $|x|\ge0$ for every real $x$, and equality
> holds exactly when $x=0$.

#### D.3

> [!QUESTION]- Full question statement
> Give a constructive existence proof that there are four consecutive composite
> positive integers. Verify explicitly that every integer in your example is
> composite.

> [!NOTE]- Solution
> **Step 1: give the witnesses.** Choose $24,25,26,27$; adjacent entries
> differ by $1$, so they are four consecutive positive integers.
>
> **Step 2: verify the required property.** Each has a nontrivial factorization:
> $24=4\cdot6$, $25=5\cdot5$, $26=2\cdot13$, and $27=3\cdot9$.
>
> Therefore all four witnesses are composite, proving the existence claim.

#### D.4

> [!QUESTION]- Full question statement
> Disprove each universal statement by giving a counterexample.
> - (a) The sum of two irrational numbers is irrational.
> - (b) $n^2+n+41$ is prime for every nonnegative integer $n$.

**(a)**

> [!NOTE]- Solution
> Take $a=\sqrt2$ and $b=-\sqrt2$. Both satisfy the hypothesis because both
> are irrational. But $a+b=\sqrt2-\sqrt2=0$, and $0$ is rational. Thus this
> single pair satisfies the hypothesis and violates the conclusion, disproving
> the universal statement.

**(b)**

> [!NOTE]- Solution
> Use the allowed input $n=40\ge0$. Substitution gives
> $$n^2+n+41=40^2+40+41=1600+81=1681=41^2.$$
> Because $1681$ factors as $41\cdot41$, it is composite. This one permitted
> input is enough to disprove “prime for every nonnegative integer.”

#### D.5

> [!QUESTION]- Full question statement
> Give a constructive existence proof that there are two irrational real numbers
> whose product is rational.

> [!NOTE]- Solution
> **Choose witnesses:** let $a=b=\sqrt2$. Each witness is irrational.
>
> **Verify the product:**
> $$ab=\sqrt2\,\sqrt2=(\sqrt2)^2=2.$$
> Since $2$ is rational, the witnesses satisfy every part of the existence
> claim.

## E. Strategy Choice and Proof Repair (1.8)

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.8_Proof_Methods_and_Strategy|Rosen 1.8 — Proof Methods and Strategy]]
> - [Direct Proofs handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7aDirectProofsHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7aDirectProofs.9.10.mp4)
> - [Proof by Contrapositive handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7bProofByContrapositiveHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7bProofByContrapositive.6.42.mp4)
> - [Proof by Contradiction handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7cProofByContradictionHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.7cProofByContradiction.7.26.mp4)
> - [Proof by Cases handout](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.8aProofByCasesHandout.pdf) | [video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.8aProofByCases.5.00.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** name the error or promising method precisely and
> supply the requested first step or complete repair. A different valid repair is
> acceptable if it fixes the same defect. **Decisive check:** confirm that the
> repaired proof no longer assumes its conclusion, divides by a possibly zero
> quantity, conflates witnesses, or begins with an element from the wrong set.

#### E.1

> [!QUESTION]- Full question statement
> For each statement, choose a promising first strategy—direct proof,
> contraposition, contradiction, cases, constructive existence, or
> counterexample—and state the first substantive step. Do not write the full
> proofs.
> - (a) If $n^2$ is even, then the integer $n$ is even.
> - (b) There is no smallest positive real number.

**(a)**

> [!NOTE]- Solution
> **Choose contraposition.** The direct hypothesis “$n^2$ is even” is difficult
> to unpack, while the negated conclusion gives the useful form
> $n=2k+1$. Start by writing the contrapositive: “if $n$ is odd, then $n^2$
> is odd,” then substitute $n=2k+1$.

**(b)**

> [!NOTE]- Solution
> **Choose contradiction.** Assume a smallest positive real number $s$ exists.
> The first substantive move is to consider $s/2$. Since $s>0$, we have
> $0<s/2<s$, so $s/2$ is a positive real smaller than the alleged minimum.
> That is the contradiction the proof will use.

#### E.2

> [!QUESTION]- Full question statement
> The following proof is intended to show that the sum of two even integers is even. Identify the gap and repair it.
>
> “Let $a$ and $b$ be even. Then $a=2k$ and $b=2k$ for some integer $k$. Hence $a+b=4k$, which is even.”

> [!NOTE]- Solution
> **Gap:** the proof assigns the same witness $k$ to two arbitrary even
> integers. That would force $a=b$, which was never assumed.
>
> **Repair:** choose independent witnesses $j,k\in\mathbb Z$ with $a=2j$ and
> $b=2k$. Then
> $$a+b=2j+2k=2(j+k).$$
> Since $j+k\in\mathbb Z$, this is twice an integer; therefore $a+b$ is even.

#### E.3

> [!QUESTION]- Full question statement
> The following proof is intended to show that the product of a rational number
> and an irrational number is irrational. Identify why the argument fails when
> $r=0$. Add the weakest necessary restriction on $r$, state the corrected
> theorem, and prove it.
>
> “Let $r$ be rational and $x$ irrational. If $rx$ were rational, then $x=(rx)/r$ would be rational, a contradiction.”

> [!NOTE]- Solution
> **Find the defect.** The proof divides by $r$ without knowing $r\ne0$.
> Indeed, the original claim is false when $r=0$, because $0x=0$ is rational.
>
> **Correct theorem:** the product of a **nonzero** rational number and an
> irrational number is irrational.
>
> **Proof:** let $r\in\mathbb Q\setminus\{0\}$ and let $x$ be irrational.
> Suppose for contradiction that $rx\in\mathbb Q$. Because $r$ is a nonzero
> rational, rational numbers are closed under division by $r$, so
> $$x=\frac{rx}{r}\in\mathbb Q.$$
> This contradicts the irrationality of $x$. Hence $rx$ is irrational.

#### E.4

> [!QUESTION]- Full question statement
> The following argument is circular. Explain the circularity, then replace it with a valid proof.
>
> “To prove that $n^2$ is odd whenever $n$ is odd, assume $n^2$ is odd. Thus
> $n^2=2k+1$ for some integer $k$, so $n^2$ is odd.”

> [!NOTE]- Solution
> **Circularity:** the sentence “assume $n^2$ is odd” assumes exactly what the
> proof is supposed to establish; the remaining lines merely repeat it.
>
> **Repair:** start from the actual hypothesis. If $n$ is odd, then
> $n=2j+1$ for some $j\in\mathbb Z$. Now calculate
> $$n^2=(2j+1)^2=4j^2+4j+1=2(2j^2+2j)+1.$$
> The quantity $2j^2+2j$ is an integer, so this is the defining form of an odd
> integer. Therefore $n^2$ is odd.

#### E.5

> [!QUESTION]- Full question statement
> The following proof is intended to show that $A\subseteq B$ whenever
> $A\cap B=A$. Identify the gap and repair it.
>
> “Let $x\in A\cap B$. Then $x\in B$. Therefore $A\subseteq B$.”

> [!NOTE]- Solution
> **Gap:** to prove $A\subseteq B$, the proof must start with an arbitrary
> $x\in A$. Starting with $x\in A\cap B$ assumes more than is available and
> checks only elements already known to lie in $B$.
>
> **Repair:** assume $A\cap B=A$ and let $x\in A$ be arbitrary. Since
> $A=A\cap B$, membership in $A$ gives $x\in A\cap B$. By the definition of
> intersection, $x\in B$. The reasoning applies to every $x\in A$, so
> $A\subseteq B$.
