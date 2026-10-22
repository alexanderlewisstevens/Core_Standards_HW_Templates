---
title: 2300 Proofs Solutions
aliases: [2300 Proofs Solutions, Proofs Solutions]
linter-yaml-title-alias: 2300 Proofs Solutions
date created: Monday, March 9th 2026, 2:29:50 pm
date modified: Wednesday, October 21st 2026
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

## A. Inference and Proof Structure (1.6)

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/1.6_Rules_of_Inference|Rosen 1.6 — Rules of Inference]]
> - [Full chapter resource page](https://cs.du.edu/~ftl/2300/resources/)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the requested conclusion, named inference rules,
> and every requested diagnosis/countermodel. A shorter valid derivation is fine.
> **Decisive check:** existential instantiation must not reuse an unlicensed common
> witness, and universal generalization must begin with an arbitrary object.

#### A.1
If the server is overloaded, requests are delayed; if requests are delayed,
the monitoring system sends an alert; and the server is overloaded. Derive
that the monitoring system sends an alert.

> [!NOTE]- Solution
> Let $O$ mean the server is overloaded, $D$ mean requests are delayed, and
> $A$ mean an alert is sent. From $O\to D$ and $O$, infer $D$ by **modus
> ponens**. From $D\to A$ and $D$, infer $A$ by **modus ponens**. Equivalently,
> one may first derive $O\to A$ by hypothetical syllogism and then use modus
> ponens.

#### A.2
Determine whether each argument is valid. Name the valid inference rule or the invalid form.

- (a) If the program compiles, then it has no syntax errors. It has no syntax
  errors. Therefore, it compiles.
> [!NOTE]- Solution
> **Invalid:** affirming the consequent. A program can have no syntax errors yet fail to compile for another reason, such as a missing dependency.

- (b) If the network is down, then the site is unavailable. The site is
  available. Therefore, the network is not down.
> [!NOTE]- Solution
> **Valid:** modus tollens.

#### A.3
Identify the error in the proposed inference and give a counterexample interpretation:
$$
\exists x\,P(x),\qquad \exists x\,Q(x)
\quad\therefore\quad
\exists x\,(P(x)\land Q(x)).
$$

> [!NOTE]- Solution
> The two existential statements can have different witnesses; nothing permits us to use the same witness for both. For a counterexample, let the domain be $\{a,b\}$, let $P$ hold only for $a$, and let $Q$ hold only for $b$. Then both premises are true, but no object satisfies both $P$ and $Q$, so the conclusion is false.

#### A.4
From $p\to q$, $q\to r$, and $\neg r$, derive $\neg p$, naming each rule.

> [!NOTE]- Solution
> From $q\to r$ and $\neg r$, infer $\neg q$ by **modus tollens**. From
> $p\to q$ and $\neg q$, infer $\neg p$ by **modus tollens**. One may instead
> first derive $p\to r$ by hypothetical syllogism and then apply modus tollens
> with $\neg r$.

#### A.5
From $\forall x\,(P(x)\to Q(x))$ and $\forall x\,P(x)$, derive
$\forall x\,Q(x)$ over a nonempty domain, naming each rule.

> [!NOTE]- Solution
> Let $c$ be an arbitrary object in the domain. Universal instantiation gives
> $P(c)\to Q(c)$ from the first premise and $P(c)$ from the second. Modus
> ponens gives $Q(c)$. Because $c$ was arbitrary, universal generalization
> gives $\forall x\,Q(x)$.

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
Give a direct proof that if an integer $n$ is even, then $n^2$ is even.

> [!NOTE]- Solution
> Suppose $n$ is even. Then $n=2k$ for some integer $k$. Thus
> $$n^2=(2k)^2=4k^2=2(2k^2).$$
> Because $2k^2$ is an integer, $n^2$ is even.

#### B.2
Give a direct proof that the sum of two rational numbers is rational.

> [!NOTE]- Solution
> Let $x$ and $y$ be rational. Then $x=a/b$ and $y=c/d$ for integers $a,b,c,d$ with $b\ne0$ and $d\ne0$. Therefore
> $$x+y=\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd}.$$
> The numerator and denominator are integers and $bd\ne0$, so $x+y$ is rational.

#### B.3
Give a direct proof that the sum of two odd integers is even.

> [!NOTE]- Solution
> Let $a$ and $b$ be odd. Then $a=2j+1$ and $b=2k+1$ for some integers $j$ and $k$. Hence
> $$a+b=2j+1+2k+1=2(j+k+1).$$
> Since $j+k+1$ is an integer, $a+b$ is even.

#### B.4
Give a direct proof that the difference of two even integers is even.

> [!NOTE]- Solution
> Let $a$ and $b$ be even. Then $a=2j$ and $b=2k$ for some integers $j$ and
> $k$. Therefore
> $$a-b=2j-2k=2(j-k).$$
> Since $j-k$ is an integer, $a-b$ is even.

#### B.5
Let $A,B,C$ be sets. Prove directly that if $A\subseteq B$, then
$A\cap C\subseteq B\cap C$.

> [!NOTE]- Solution
> Assume $A\subseteq B$, and let $x$ be an arbitrary element of $A\cap C$.
> Then $x\in A$ and $x\in C$. Because $A\subseteq B$, we have $x\in B$.
> Hence $x\in B\cap C$. Since every element of $A\cap C$ lies in $B\cap C$,
> $A\cap C\subseteq B\cap C$.

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
Let $m,n\in\mathbb Z$. Prove by contraposition that if $mn$ is odd, then both
$m$ and $n$ are odd.

> [!NOTE]- Solution
> The contrapositive is: **if $m$ is even or $n$ is even, then $mn$ is even.**
> If $m=2k$, then $mn=2(kn)$ is even. If $n=2\ell$, then
> $mn=2(m\ell)$ is even. The cases cover the disjunction, so the
> contrapositive—and therefore the original statement—is true.

#### C.2
Prove by contraposition that if $3n+2$ is odd, then the integer $n$ is odd.

> [!NOTE]- Solution
> The contrapositive is: if $n$ is even, then $3n+2$ is even. Suppose $n=2k$ for some integer $k$. Then
> $$3n+2=3(2k)+2=2(3k+1).$$
> Since $3k+1$ is an integer, $3n+2$ is even. Therefore the original statement follows by contraposition.

#### C.3
Prove by contradiction that there is no largest integer.

> [!NOTE]- Solution
> Suppose, for contradiction, that a largest integer $N$ exists. Then $N+1$ is also an integer and $N+1>N$. This contradicts the assumption that $N$ is largest. Therefore there is no largest integer.

#### C.4
Let $r$ be rational and $x$ irrational. Prove by contradiction that $r+x$ is irrational.

> [!NOTE]- Solution
> Suppose, for contradiction, that $r+x$ is rational. The difference of two rational numbers is rational, so
> $$x=(r+x)-r$$
> would be rational. This contradicts the hypothesis that $x$ is irrational. Therefore $r+x$ is irrational.

#### C.5
Prove by contraposition that if $n^2$ is even, then $n$ is even.

> [!NOTE]- Solution
> The contrapositive is: if $n$ is odd, then $n^2$ is odd. Suppose
> $n=2k+1$ for some integer $k$. Then
> $$n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1.$$
> Thus $n^2$ is odd, proving the contrapositive and therefore the original
> implication.

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
Prove by cases that $n(n+1)$ is even for every integer $n$.

> [!NOTE]- Solution
> Every integer is even or odd.
>
> **Case 1:** If $n$ is even, then $n=2k$ for some integer $k$, so $n(n+1)=2k(n+1)$ is even.
>
> **Case 2:** If $n$ is odd, then $n=2k+1$ for some integer $k$. Thus $n+1=2(k+1)$ is even, so $n(n+1)=2n(k+1)$ is even.
>
> The cases are exhaustive, so $n(n+1)$ is always even.

#### D.2
Prove by cases that $|x|\ge 0$ for every real number $x$, with equality exactly when $x=0$.

> [!NOTE]- Solution
> **Case 1:** If $x\ge0$, then $|x|=x\ge0$. In this case $|x|=0$ exactly when $x=0$.
>
> **Case 2:** If $x<0$, then $|x|=-x>0$, so equality cannot occur.
>
> Thus $|x|\ge0$ for every real $x$, and equality holds exactly when $x=0$.

#### D.3
Give a constructive existence proof that there are four consecutive composite
positive integers.

> [!NOTE]- Solution
> The integers $24,25,26,27$ are consecutive and composite:
> $24=4\cdot6$, $25=5\cdot5$, $26=2\cdot13$, and $27=3\cdot9$.
> These explicit witnesses prove the existence claim constructively.

#### D.4
Disprove each universal statement by giving a counterexample.

- (a) The sum of two irrational numbers is irrational.
> [!NOTE]- Solution
> Take $\sqrt2$ and $-\sqrt2$. Both are irrational, but their sum is $0$, which is rational.

- (b) $n^2+n+41$ is prime for every nonnegative integer $n$.
> [!NOTE]- Solution
> Take $n=40$. Then $n^2+n+41=40^2+40+41=1681=41^2$, which is composite.

#### D.5
Give a constructive existence proof that two irrational real numbers can have
a rational product.

> [!NOTE]- Solution
> Take $a=b=\sqrt2$. Both numbers are irrational, while
> $$ab=\sqrt2\,\sqrt2=2,$$
> which is rational. These explicit witnesses prove the existence statement.

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
For each statement, choose a promising first strategy and state the first
substantive step.

- (a) If $n^2$ is even, then $n$ is even.
> [!NOTE]- Solution
> **Contraposition:** the contrapositive says that an odd $n$ has an odd square, which follows directly from $n=2k+1$.

- (b) There is no smallest positive real number.
> [!NOTE]- Solution
> **Contradiction:** if $s$ were the smallest positive real number, then $s/2$ would be a smaller positive real number.

#### E.2
The following proof is intended to show that the sum of two even integers is even. Identify the gap and repair it.

“Let $a$ and $b$ be even. Then $a=2k$ and $b=2k$ for some integer $k$. Hence $a+b=4k$, which is even.”

> [!NOTE]- Solution
> The proof incorrectly assumes that two arbitrary even integers use the same witness $k$. Instead, write $a=2j$ and $b=2k$ for possibly different integers $j$ and $k$. Then
> $$a+b=2j+2k=2(j+k),$$
> which is even because $j+k$ is an integer.

#### E.3
The following proof is intended to show that the product of a rational number and an irrational number is irrational. Identify why the claim or proof needs repair, state a correct theorem, and prove it.

“Let $r$ be rational and $x$ irrational. If $rx$ were rational, then $x=(rx)/r$ would be rational, a contradiction.”

> [!NOTE]- Solution
> The proof divides by $r$ without knowing that $r\ne0$, and the original claim is false when $r=0$ because $0x=0$ is rational. A correct theorem is: **the product of a nonzero rational number and an irrational number is irrational.** Let $r\ne0$ be rational and $x$ irrational. If $rx$ were rational, then $(rx)/r$ would be rational because the quotient of rational numbers with nonzero denominator is rational. But $(rx)/r=x$, contradicting that $x$ is irrational. Therefore $rx$ is irrational.

#### E.4
The following argument is circular. Explain the circularity, then replace it with a valid proof.

“To prove that $n^2$ is odd whenever $n$ is odd, assume $n^2$ is odd. Thus
$n^2=2k+1$ for some integer $k$, so $n^2$ is odd.”

> [!NOTE]- Solution
> The argument assumes its conclusion, so it is circular. For a valid direct
> proof, assume $n$ is odd. Then $n=2j+1$ for some integer $j$, and
> $$n^2=(2j+1)^2=4j^2+4j+1=2(2j^2+2j)+1.$$
> Since $2j^2+2j$ is an integer, $n^2$ is odd.

#### E.5
The following proof is intended to show that $A\subseteq B$ whenever
$A\cap B=A$. Identify the gap and repair it.

“Let $x\in A\cap B$. Then $x\in B$. Therefore $A\subseteq B$.”

> [!NOTE]- Solution
> The argument starts with an element already known to be in $A\cap B$ rather
> than with an arbitrary element of $A$, so it never proves that every element
> of $A$ belongs to $B$. For the repair, assume $A\cap B=A$ and let $x\in A$
> be arbitrary. The equality gives $x\in A\cap B$, so $x\in B$. Therefore
> every element of $A$ is in $B$, and $A\subseteq B$.
