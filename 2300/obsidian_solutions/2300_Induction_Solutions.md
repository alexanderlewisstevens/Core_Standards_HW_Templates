---
title: 2300 Induction Solutions
aliases: [2300 Induction Solutions, Induction Solutions]
linter-yaml-title-alias: 2300 Induction Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Wednesday, October 21st 2026
publish: true
permalink: core-assessment-solutions/2300-induction-solutions
---
# 2300 Induction Solutions

> [!IMPORTANT] Current practice bank and scoring
> These solutions correspond to the current A–C practice bank, not a live graded form. A supervised attempt lasts 20 minutes and contains one problem from each section. Section C is essential. **Meets** requires a fully correct C problem and either A or B fully correct. **Exceeds** requires A, B, and C fully correct. Every retake is a new complete form. Staff record **Not Yet / Meets / Exceeds** as **0 / 4 / 5** in Canvas.

## Full-credit and grader guidance

The solutions below are models, not scripts students must reproduce word for
word. A different proof earns full credit when it uses the required induction
method, states a sufficient hypothesis, proves all necessary base cases, and
actually derives the next case. Algebraically equivalent arrangements and
different variable names are acceptable.

The **decisive check** is the fastest place for a grader to see whether the
central reasoning is sound. It does not replace the rest of a requested proof:
under the course mastery rule, every requested part must be present and correct.

> [!TIP]- Relevant Materials
> - [Proof by Induction (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.1aProofByInductionHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.1aProofByInduction.10.20.mp4)
> - [Another Proof by Induction (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.1bSecondProofByInductionHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.1bSecondProofByInduction.5.52.mp4)
> - [Proof by Strong Induction (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.2aProofByStrongInductionHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch5/2300.5.2aProofByStrongInduction.15.07.mp4)
> - [[Books/book_sections_md/5.1_Mathematical_Induction|Rosen 5.1 — Mathematical Induction]]
> - [[Books/book_sections_md/5.2_Strong_Induction_andWell-Ordering|Rosen 5.2 — Strong Induction and Well-Ordering]]

## A. Build the Induction Plan

For each problem, a complete plan identifies the proposition, base case or
cases, induction hypothesis, and exact target. It need not carry out the entire
proof unless the prompt asks for it.

> [!CHECK]- Minimum full-credit response and decisive check
> A minimum complete response gives all four requested components with the correct range. Equivalent notation is acceptable. **Decisive check:** the hypothesis concerns already established cases, while the target is the new case; the response must not assume the target.

### A.1 Prime Factorization by Strong Induction

Let $P(n)$ be “$n$ is a product of primes.”

- **Base case:** $P(2)$ holds because $2$ is prime, and a prime is a product consisting of itself.
- **Strong induction hypothesis:** Fix $k\ge 2$ and assume $P(j)$ holds for every integer $j$ with $2\le j\le k$.
- **Target:** Prove that $k+1$ is a product of primes.
- **Case split for the step:** If $k+1$ is prime, the target holds immediately. If it is composite, then $k+1=ab$ for integers $a,b$ satisfying $2\le a,b\le k$. The strong hypothesis factors both $a$ and $b$ into primes, so their product $k+1$ is also a product of primes.

The important range is $2\le j\le k$; merely assuming $P(k)$ is not enough to handle arbitrary factors $a$ and $b$.

### A.2 Triangular-Sum Plan

Let
$$P(n):\quad 1+2+\cdots+n=\frac{n(n+1)}2.$$

- **Base case:** $P(1)$ is $1=1(2)/2$.
- **Induction hypothesis:** For an arbitrary $k\ge1$, assume
  $$1+2+\cdots+k=\frac{k(k+1)}2.$$
- **Target:**
  $$1+2+\cdots+k+(k+1)=\frac{(k+1)(k+2)}2.$$

The left side of the target is the old sum plus the genuinely next term,
$k+1$.

### A.3 Exponential Divisibility Plan

Let $P(n)$ be $7\mid(8^n-1)$ for $n\ge0$.

- **Base case:** $8^0-1=0$, and $7\mid0$.
- **Induction hypothesis:** For an arbitrary $k\ge0$, assume
  $8^k-1=7t$ for some integer $t$.
- **Target:** Prove that $8^{k+1}-1=7s$ for some integer $s$.

Writing divisibility as an integer equation makes clear exactly what must be
constructed in the induction step.

### A.4 Postage by Strong Induction

Let $P(n)$ be “$n$ cents can be formed using 4-cent and 7-cent stamps,” for
$n\ge18$.

- **Base cases:**
  $$18=7+7+4,\qquad19=7+4+4+4,\qquad20=4+4+4+4+4,\qquad21=7+7+7.$$
- **Strong induction hypothesis:** For an arbitrary $k\ge21$, assume every amount $j$ with $18\le j\le k$ can be formed.
- **Target:** Form $k+1$ cents.
- **Step plan:** Since $k\ge21$, $18\le k-3\le k$. Use the hypothesis to form $k-3$ cents, then add one 4-cent stamp to obtain $(k-3)+4=k+1$.

The four consecutive base cases are what allow the “add 4” step to reach every
later amount.

### A.5 Exponential Inequality Plan

Let $P(n)$ be $2^n\ge n+1$ for $n\ge0$.

- **Base case:** $2^0=1\ge1$.
- **Induction hypothesis:** For an arbitrary $k\ge0$, assume $2^k\ge k+1$.
- **Target:** Prove $2^{k+1}\ge k+2$.
- **Planned step:**
  $$2^{k+1}=2\cdot2^k\ge2(k+1)\ge k+2,$$
  where the last inequality holds because $k\ge0$.

## B. Diagnose and Repair Induction

> [!CHECK]- Minimum full-credit response and decisive check
> A complete response identifies the exact failure and supplies the smallest sound repair, including any missing base cases or corrected hypothesis. **Decisive check:** the repaired step may use only established cases and must reach the actual $k+1$ statement.

### B.1 Circular Use of the Target

The flawed proof assumes $2^{k+1}\ge k+2$, which is exactly the claim it is
supposed to prove. That makes the step circular.

The repair is:

1. Base case: $2^0=1\ge1$.
2. Assume $2^k\ge k+1$ for an arbitrary $k\ge0$.
3. Then
   $$2^{k+1}=2\cdot2^k\ge2(k+1)\ge k+2.$$

A response using a different but valid chain from the hypothesis to the target
also earns full credit.

### B.2 A Two-Step Recurrence with One Base Case

If the recurrence step uses both $P(k)$ and $P(k-1)$, proving only $P(0)$ does
not supply enough information to begin: the first nontrivial step also needs
$P(1)$.

Prove both $P(0)$ and $P(1)$. Then, for $k\ge1$, either:

- use strong induction and assume $P(j)$ for every $0\le j\le k$, or
- explicitly assume the two preceding statements $P(k)$ and $P(k-1)$ in a valid two-step induction formulation.

Either repair is acceptable when its indexing is consistent.

### B.3 The False “All Entries Are Equal” Proof

The first required step goes from a list of length $1$ to a list of length $2$.
The first $1$ entry and last $1$ entry are disjoint, so there is no common entry
through which equality can be transferred. The claimed overlap exists only
when the two sublists have length at least $2$.

Thus the induction step fails precisely at $k=1$; checking only later values
cannot repair a missing first step. The statement itself is false, so there is
no sound induction proof of it.

### B.4 Wrong Next Term in the Odd-Number Sum

The formula
$$1+3+\cdots+(2n-1)=n^2$$
has next term $2(k+1)-1=2k+1$, not $2k-1$. With the correct hypothesis and
next term,
$$1+3+\cdots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2.$$

The decisive repair is both to use the actual next term and to replace the old
partial sum by $k^2$ using the hypothesis.

### B.5 Divisibility Step That Assumes the Next Case

The invalid proof assumes the $k+1$ divisibility statement. Instead assume
only that $8^k-1=7t$ for some integer $t$. Then
$$
8^{k+1}-1
=8(8^k-1)+7
=8(7t)+7
=7(8t+1).
$$
Because $8t+1$ is an integer, this proves $7\mid(8^{k+1}-1)$ without assuming
the target.

## C. Complete the Essential Binomial-Sum Proof

Every C problem is the identity
$$
S_n(w)=\sum_{j=0}^{n}w^{\,n-j}\binom{n}{j}=(w+1)^n
$$
for one fixed value of $w$. The proof must use induction and Pascal's identity;
citing the binomial theorem alone does not satisfy that instruction.

> [!CHECK]- Minimum full-credit response and decisive check
> A minimum complete proof states $P(n)$, proves the $n=0$ base case, states the induction hypothesis, applies Pascal's identity in the $k+1$ sum, handles both endpoints, reindexes correctly, invokes the hypothesis, and concludes $P(k+1)$. Equivalent endpoint bookkeeping is acceptable. **Decisive check:** after the Pascal split, the two sums must become $wS_k(w)$ and $S_k(w)$, producing the factor $(w+1)$.

### Reusable worked proof

Fix the specified value of $w$, and let $P(n)$ be $S_n(w)=(w+1)^n$.

**Base case.** At $n=0$,
$$S_0(w)=w^0\binom00=1=(w+1)^0.$$

**Induction hypothesis.** For an arbitrary $k\ge0$, assume
$$S_k(w)=\sum_{j=0}^{k}w^{\,k-j}\binom{k}{j}=(w+1)^k.$$

**Induction step.** Using the endpoint terms separately and Pascal's identity
$\binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}$ for $1\le j\le k$,
$$
\begin{aligned}
S_{k+1}(w)
&=w^{k+1}+1+
  \sum_{j=1}^{k}w^{\,k+1-j}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)\\
&=w\left(w^k+\sum_{j=1}^{k}w^{\,k-j}\binom{k}{j}\right)
  +\left(1+\sum_{j=1}^{k}w^{\,k+1-j}\binom{k}{j-1}\right)\\
&=wS_k(w)+S_k(w).
\end{aligned}
$$
For the second parenthesis, set $i=j-1$; it becomes
$1+\sum_{i=0}^{k-1}w^{\,k-i}\binom{k}{i}=S_k(w)$, with the final $1$ being
the $i=k$ term. Therefore,
$$
S_{k+1}(w)=(w+1)S_k(w)=(w+1)(w+1)^k=(w+1)^{k+1}.
$$
This proves the identity for every $n\ge0$.

An equally complete proof that uses the conventions
$\binom{k}{-1}=\binom{k}{k+1}=0$ to absorb the endpoints is also acceptable.

### C.1 Unweighted Binomial Sum

Set $w=1$. The reusable proof gives
$$\sum_{j=0}^{n}\binom{n}{j}=2^n.$$
In the decisive step, the Pascal split produces $S_k(1)+S_k(1)=2S_k(1)$.

### C.2 Weight $w=2$

Set $w=2$. The proof gives
$$\sum_{j=0}^{n}2^{\,n-j}\binom{n}{j}=3^n,$$
and the induction step combines $2S_k(2)+S_k(2)=3S_k(2)$.

### C.3 Weight $w=3$

Set $w=3$. The proof gives
$$\sum_{j=0}^{n}3^{\,n-j}\binom{n}{j}=4^n,$$
and the induction step combines $3S_k(3)+S_k(3)=4S_k(3)$.

### C.4 Weight $w=4$

Set $w=4$. The proof gives
$$\sum_{j=0}^{n}4^{\,n-j}\binom{n}{j}=5^n,$$
and the induction step combines $4S_k(4)+S_k(4)=5S_k(4)$.

### C.5 Weight $w=5$

Set $w=5$. The proof gives
$$\sum_{j=0}^{n}5^{\,n-j}\binom{n}{j}=6^n,$$
and the induction step combines $5S_k(5)+S_k(5)=6S_k(5)$.
