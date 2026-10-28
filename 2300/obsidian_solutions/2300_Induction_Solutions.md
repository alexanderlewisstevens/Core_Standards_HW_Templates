---
title: 2300 Induction Solutions
aliases: [2300 Induction Solutions, Induction Solutions]
linter-yaml-title-alias: 2300 Induction Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Wednesday, October 28th 2026
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

### How to read an induction solution

Read every model in the same order:

1. **State the proposition and domain.** Say exactly what $P(n)$ means and where $n$ begins.
2. **Verify the base case(s).** Substitute the first allowed value; do not merely say that the base is “obvious.”
3. **State the hypothesis.** Fix an arbitrary $k$ in the domain and assume only already established case(s).
4. **Write the next-case target.** Replace $n$ by $k+1$ before doing algebra.
5. **Build a bridge from the target expression to the hypothesis.** Mark the precise line where the hypothesis is used.
6. **Close the argument.** State that $P(k+1)$ follows and invoke induction on the stated domain.

For a diagnosis problem, compare the proposed proof against these six steps and
identify the *first* point where it stops being justified.

> [!TIP]- Relevant Materials
> - [Induction companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/induction_core_companion.pdf)
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

> [!QUESTION]- Full question statement
> For the claim that every integer $n\ge2$ is a product of one or more primes, state (i) the base case, (ii) the strong induction hypothesis for an arbitrary $k\ge2$, (iii) what must be proved for $k+1$, and (iv) the two cases used in the induction step. Do not complete the proof.

Let $P(n)$ be “$n$ is a product of primes.”

- **Base case:** $P(2)$ holds because $2$ is prime, and a prime is a product consisting of itself.
- **Strong induction hypothesis:** Fix $k\ge 2$ and assume $P(j)$ holds for every integer $j$ with $2\le j\le k$.
- **Target:** Prove that $k+1$ is a product of primes.
- **Case split for the step:** If $k+1$ is prime, the target holds immediately. If it is composite, then $k+1=ab$ for integers $a,b$ satisfying $2\le a,b\le k$. The strong hypothesis factors both $a$ and $b$ into primes, so their product $k+1$ is also a product of primes.

The important range is $2\le j\le k$; merely assuming $P(k)$ is not enough to handle arbitrary factors $a$ and $b$.

### A.2 Triangular-Sum Plan

> [!QUESTION]- Full question statement
> For $1+2+\cdots+n=n(n+1)/2$ for every $n\ge1$, state $P(n)$, verify the base case, state the induction hypothesis $P(k)$, and state exactly what must be shown for $P(k+1)$. Do not complete the next-case algebra.

Let
$$P(n):\quad 1+2+\cdots+n=\frac{n(n+1)}2.$$

- **Base case:** $P(1)$ is $1=1(2)/2$.
- **Induction hypothesis:** For an arbitrary $k\ge1$, assume
  $$1+2+\cdots+k=\frac{k(k+1)}2.$$
- **Target:**
  $$1+2+\cdots+k+(k+1)=\frac{(k+1)(k+2)}2.$$

The left side of the target is the old sum plus the genuinely next term,
$k+1$. The planned bridge is
$$
1+2+\cdots+k+(k+1)
=\frac{k(k+1)}2+(k+1)
=\frac{(k+1)(k+2)}2,
$$
where the first equality using a formula is exactly the induction-hypothesis
step.

### A.3 Exponential Divisibility Plan

> [!QUESTION]- Full question statement
> For the claim $7\mid(8^n-1)$ for every integer $n\ge0$, state $P(n)$, the base case, the induction hypothesis using an integer witness, and the divisibility statement required for $k+1$. Do not complete the algebra.

Let $P(n)$ be $7\mid(8^n-1)$ for $n\ge0$.

- **Base case:** $8^0-1=0$, and $7\mid0$.
- **Induction hypothesis:** For an arbitrary $k\ge0$, assume
  $8^k-1=7t$ for some integer $t$.
- **Target:** Prove that $8^{k+1}-1=7s$ for some integer $s$.

The next-case expression can be rewritten to expose the hypothesis:
$$
8^{k+1}-1=8(8^k-1)+7=8(7t)+7=7(8t+1).
$$
Since $8t+1\in\mathbb Z$, it is the required witness $s$.

Writing divisibility as an integer equation makes clear exactly what must be
constructed in the induction step.

### A.4 Postage by Strong Induction

> [!QUESTION]- Full question statement
> For the claim that every amount $n\ge18$ can be made using 4-cent and 7-cent stamps, list sufficient base cases, state a strong induction hypothesis through $k$, and explain which earlier amount is used to construct $k+1$. Do not complete the proof.

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

> [!QUESTION]- Full question statement
> For $2^n\ge n+1$ for every integer $n\ge0$, state $P(n)$, verify the base case, state the induction hypothesis, and write the first equality and inequality that should begin the $k+1$ step. Do not finish the proof.

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

> [!QUESTION]- Full question statement
> A student tries to prove $2^n\ge n+1$ for $n\ge0$ by assuming $2^{k+1}\ge k+2$ in the induction step. Identify the circularity, state the correct induction hypothesis, and give a valid chain of inequalities for the next case.

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

> [!QUESTION]- Full question statement
> A recurrence proof uses both $P(k)$ and $P(k-1)$ to prove $P(k+1)$ but verifies only $P(0)$. Explain what is missing. State sufficient base cases and a valid strong induction hypothesis.

If the recurrence step uses both $P(k)$ and $P(k-1)$, proving only $P(0)$ does
not supply enough information to begin: the first nontrivial step also needs
$P(1)$.

Prove both $P(0)$ and $P(1)$. Then, for $k\ge1$, either:

- use strong induction and assume $P(j)$ for every $0\le j\le k$, or
- explicitly assume the two preceding statements $P(k)$ and $P(k-1)$ in a valid two-step induction formulation.

Either repair is acceptable when its indexing is consistent.

### B.3 The False “All Entries Are Equal” Proof

> [!QUESTION]- Full question statement
> In the false proof that all positive integers in any finite list are equal, the step applies the hypothesis to the first $k$ and last $k$ entries and claims the groups overlap. Identify the first $k$ for which overlap is needed and explain precisely why the step fails.

The first required step goes from a list of length $1$ to a list of length $2$.
The first $1$ entry and last $1$ entry are disjoint, so there is no common entry
through which equality can be transferred. The claimed overlap exists only
when the two sublists have length at least $2$.

Thus the induction step fails precisely at $k=1$; checking only later values
cannot repair a missing first step. The statement itself is false, so there is
no sound induction proof of it.

### B.4 Wrong Next Term in the Odd-Number Sum

> [!QUESTION]- Full question statement
> A student proving $1+3+\cdots+(2n-1)=n^2$ writes $k^2+(2k-1)=(k+1)^2$. Identify the incorrect next term, repair the calculation, and state where the induction hypothesis is used.

The formula
$$1+3+\cdots+(2n-1)=n^2$$
has next term $2(k+1)-1=2k+1$, not $2k-1$. With the correct hypothesis and
next term,
$$1+3+\cdots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2.$$

The decisive repair is both to use the actual next term and to replace the old
partial sum by $k^2$ using the hypothesis.

### B.5 Divisibility Step That Assumes the Next Case

> [!QUESTION]- Full question statement
> A student proving $7\mid(8^n-1)$ says, “Assume $7\mid(8^{k+1}-1)$; therefore the next case holds.” Identify the error, replace it with the correct induction hypothesis, and show an algebraic decomposition that proves the $k+1$ case.

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
Here are the transformations in words:

1. The $j=0$ endpoint contributes $w^{k+1}$, and the $j=k+1$ endpoint contributes $1$.
2. Pascal's identity splits every interior coefficient into two terms.
3. Factor $w$ from the first family; together with $w^{k+1}$ it becomes $wS_k(w)$.
4. For the second family, set $i=j-1$. Its first index changes from $j=1$ to $i=0$, and its last from $j=k$ to $i=k-1$.

Thus the second parenthesis becomes
$1+\sum_{i=0}^{k-1}w^{\,k-i}\binom{k}{i}=S_k(w)$, with the final $1$ being
the $i=k$ term. Therefore,
$$
S_{k+1}(w)=(w+1)S_k(w)=(w+1)(w+1)^k=(w+1)^{k+1}.
$$
This proves the identity for every $n\ge0$.

An equally complete proof that uses the conventions
$\binom{k}{-1}=\binom{k}{k+1}=0$ to absorb the endpoints is also acceptable.

### C.1 Unweighted Binomial Sum

> [!QUESTION]- Full question statement
> You may use Pascal's identity
>
> $$
>
> \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}
> \quad(1\le j\le k),\qquad
> \binom{n}{0}=\binom{n}{n}=1.
>
> $$
>
> Prove by mathematical induction that
>
> $$
>
> \sum_{j=0}^{n}\binom{n}{j}=2^n\qquad\text{for every integer }n\ge0.
>
> $$
>
> State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof.

We prove by mathematical induction that
$$
P(n):\qquad \sum_{j=0}^{n}\binom{n}{j}=2^n
$$
for every integer $n\ge 0$.

#### Base case: $n=0$

When $n=0$, the sum contains only the term with $j=0$. Therefore
$$
\sum_{j=0}^{0}\binom{0}{j}
=\binom{0}{0}
=1
=2^0.
$$
The first equality expands the one-term sum, the second uses the endpoint
identity $\binom00=1$, and the third uses $2^0=1$. Thus $P(0)$ is true.

#### Induction hypothesis

Let $k\ge0$ be arbitrary. Assume that $P(k)$ is true; that is, assume
$$
\sum_{j=0}^{k}\binom{k}{j}=2^k.
$$
This is the induction hypothesis. We may use it for the complete sum of the
entries in row $k$, but we may not assume anything about the sum in row
$k+1$.

#### Induction step

We must prove $P(k+1)$:
$$
\sum_{j=0}^{k+1}\binom{k+1}{j}=2^{k+1}.
$$
Because the stated form of Pascal's identity applies to the interior indices
$1\le j\le k$, first separate the two endpoint terms. Then calculate:
$$
\begin{aligned}
\sum_{j=0}^{k+1}\binom{k+1}{j}
&=\binom{k+1}{0}
  +\sum_{j=1}^{k}\binom{k+1}{j}
  +\binom{k+1}{k+1} \\
&=1+\sum_{j=1}^{k}\binom{k+1}{j}+1 \\
&=1+\sum_{j=1}^{k}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)+1 \\
&=1+\sum_{j=1}^{k}\binom{k}{j}
  +\sum_{j=1}^{k}\binom{k}{j-1}+1 \\
&=\binom{k}{0}+\sum_{j=1}^{k}\binom{k}{j}
  +\sum_{i=0}^{k-1}\binom{k}{i}+\binom{k}{k} \\
&=\sum_{j=0}^{k}\binom{k}{j}
  +\sum_{i=0}^{k}\binom{k}{i} \\
&=2^k+2^k \\
&=2\cdot2^k \\
&=2^{k+1}.
\end{aligned}
$$

Each line has a specific justification:

1. **Separate the endpoints.** The first line rewrites the sum as its $j=0$
   term, its interior terms $1\le j\le k$, and its $j=k+1$ term. No terms are
   added or removed.
2. **Evaluate the endpoints.** The identities
   $\binom{k+1}{0}=\binom{k+1}{k+1}=1$ give the second line.
3. **Apply Pascal's identity.** For every interior index $1\le j\le k$,
   $$
   \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}.
   $$
   This replaces each row-$(k+1)$ interior entry by two entries from row $k$.
4. **Split the sum.** The identity
   $\sum_j(a_j+b_j)=\sum_j a_j+\sum_j b_j$ separates the two families of
   row-$k$ coefficients.
5. **Reindex the second family and restore the endpoints.** In
   $\sum_{j=1}^{k}\binom{k}{j-1}$, set $i=j-1$. When $j=1$, $i=0$; when
   $j=k$, $i=k-1$. Hence
   $$
   \sum_{j=1}^{k}\binom{k}{j-1}
   =\sum_{i=0}^{k-1}\binom{k}{i}.
   $$
   Also, the two outside $1$'s may be written as
   $\binom{k}{0}$ and $\binom{k}{k}$. This completes both copies of row $k$.
6. **Recognize two complete row sums.** The first group runs from $j=0$ to
   $j=k$, and the second runs from $i=0$ to $i=k$. The letters $i$ and $j$
   are dummy indices, so both groups are the same complete sum.
7. **Use the induction hypothesis.** This is the exact point where the
   hypothesis is used: each complete row-$k$ sum equals $2^k$.
8. **Simplify powers of two.** Since
   $2^k+2^k=2\cdot2^k=2^{k+1}$, the resulting expression is exactly the
   right side required by $P(k+1)$.

The displayed calculation also works when $k=0$: the interior sums are empty,
and the two endpoint terms produce two copies of $\binom00$.

We have proved that $P(0)$ is true and that, for every $k\ge0$, $P(k)$ implies
$P(k+1)$. Therefore, by mathematical induction,
$$
\boxed{\displaystyle\sum_{j=0}^{n}\binom{n}{j}=2^n}
$$
for every integer $n\ge0$.

### C.2 Weight $w=2$

> [!QUESTION]- Full question statement
> You may use Pascal's identity
>
> $$
>
> \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}
> \quad(1\le j\le k),\qquad
> \binom{n}{0}=\binom{n}{n}=1.
>
> $$
>
> Prove by mathematical induction that
>
> $$
>
> \sum_{j=0}^{n} 2^{n-j}\binom{n}{j}=3^n\qquad\text{for every integer }n\ge0.
>
> $$
>
> State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof.

Let
$$
P(n):\qquad S_n(2)=\sum_{j=0}^{n}2^{\,n-j}\binom{n}{j}=3^n.
$$

**Base case.** When $n=0$, the sum has one term:
$$
S_0(2)=2^0\binom00=1=3^0.
$$

**Induction hypothesis and target.** Fix an arbitrary $k\ge0$ and assume
$S_k(2)=3^k$. We must prove $S_{k+1}(2)=3^{k+1}$.

**Induction step.** Separate the two endpoint terms, use Pascal's identity on
the interior coefficients, and split the resulting sum. After reindexing the
second family, the first family is two copies of the row-$k$ weighted sum and
the second family is one copy:
$$
\begin{aligned}
S_{k+1}(2)
&=\sum_{j=0}^{k+1}2^{\,k+1-j}\binom{k+1}{j}\\
&=2^{k+1}+\sum_{j=1}^{k}2^{k+1-j}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)+1\\
&=2\left(2^k\binom{k}{0}+\sum_{j=1}^{k}2^{k-j}\binom{k}{j}\right)
  +\sum_{i=0}^{k-1}2^{k-i}\binom{k}{i}+1\\
&=2\sum_{j=0}^{k}2^{\,k-j}\binom{k}{j}
  +\sum_{j=0}^{k}2^{\,k-j}\binom{k}{j}\\
&=2S_k(2)+S_k(2)\\
&=3S_k(2)\\
&=3\cdot3^k=3^{k+1}.
\end{aligned}
$$
Here $i=j-1$ changes the second interior family's bounds from $1\le j\le k$
to $0\le i\le k-1$. Its missing endpoint is exactly
$1=2^0\binom{k}{k}$. The same calculation works at $k=0$, with empty
interior sums. The final line substitutes the induction hypothesis
$S_k(2)=3^k$. Therefore
$P(k+1)$ follows, and induction proves the identity for every $n\ge0$.

**Decisive check:** the Pascal split must produce $2S_k(2)+S_k(2)$; merely
citing the binomial theorem does not meet the stated proof-method requirement.

### C.3 Weight $w=3$

> [!QUESTION]- Full question statement
> You may use Pascal's identity
>
> $$
>
> \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}
> \quad(1\le j\le k),\qquad
> \binom{n}{0}=\binom{n}{n}=1.
>
> $$
>
> Prove by mathematical induction that
>
> $$
>
> \sum_{j=0}^{n} 3^{n-j}\binom{n}{j}=4^n\qquad\text{for every integer }n\ge0.
>
> $$
>
> State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof.

Let
$$
P(n):\qquad S_n(3)=\sum_{j=0}^{n}3^{\,n-j}\binom{n}{j}=4^n.
$$

**Base case.** At $n=0$,
$S_0(3)=3^0\binom00=1=4^0$.

**Induction hypothesis and target.** Fix $k\ge0$ and assume
$S_k(3)=4^k$. The target is $S_{k+1}(3)=4^{k+1}$.

**Induction step.** Pascal's identity replaces each row-$(k+1)$ coefficient
with two row-$k$ coefficients. Once the endpoints are restored and the second
sum is reindexed, those two families are
$$
\begin{aligned}
S_{k+1}(3)
&=3^{k+1}+\sum_{j=1}^{k}3^{k+1-j}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)+1\\
&=3\left(3^k\binom{k}{0}+\sum_{j=1}^{k}3^{k-j}\binom{k}{j}\right)
  +\sum_{i=0}^{k-1}3^{k-i}\binom{k}{i}+1\\
&=3\sum_{j=0}^{k}3^{\,k-j}\binom{k}{j}
  +\sum_{j=0}^{k}3^{\,k-j}\binom{k}{j}\\
&=3S_k(3)+S_k(3)\\
&=4S_k(3)\\
&=4\cdot4^k=4^{k+1}.
\end{aligned}
$$
The reindexing is $i=j-1$, so the bounds $1,\ldots,k$ become
$0,\ldots,k-1$ and $3^{k+1-j}$ becomes $3^{k-i}$. The outside $1$
restores $i=k$ because $3^0\binom{k}{k}=1$. Empty sums make this valid
also for $k=0$. Only the final line uses $S_k(3)=4^k$.
Thus $P(k+1)$ holds. By induction,
$\sum_{j=0}^{n}3^{\,n-j}\binom{n}{j}=4^n$ for every $n\ge0$.

**Decisive check:** the factor $3$ comes from
$3^{k+1-j}=3\cdot3^{k-j}$; it is not introduced by the induction hypothesis.

### C.4 Weight $w=4$

> [!QUESTION]- Full question statement
> You may use Pascal's identity
>
> $$
>
> \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}
> \quad(1\le j\le k),\qquad
> \binom{n}{0}=\binom{n}{n}=1.
>
> $$
>
> Prove by mathematical induction that
>
> $$
>
> \sum_{j=0}^{n} 4^{n-j}\binom{n}{j}=5^n\qquad\text{for every integer }n\ge0.
>
> $$
>
> State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof.

Let
$$
P(n):\qquad S_n(4)=\sum_{j=0}^{n}4^{\,n-j}\binom{n}{j}=5^n.
$$

**Base case.** At $n=0$,
$S_0(4)=4^0\binom00=1=5^0$.

**Induction hypothesis and target.** Fix an arbitrary $k\ge0$ and assume
$S_k(4)=5^k$. We must obtain $S_{k+1}(4)=5^{k+1}$ without assuming it.

**Induction step.** Separate the $j=0$ and $j=k+1$ endpoints, apply
$\binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}$ to the interior terms, and
reindex the second family. The complete row-$k$ sums then appear as
$$
\begin{aligned}
S_{k+1}(4)
&=4^{k+1}+\sum_{j=1}^{k}4^{k+1-j}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)+1\\
&=4\left(4^k\binom{k}{0}+\sum_{j=1}^{k}4^{k-j}\binom{k}{j}\right)
  +\sum_{i=0}^{k-1}4^{k-i}\binom{k}{i}+1\\
&=4\sum_{j=0}^{k}4^{\,k-j}\binom{k}{j}
  +\sum_{j=0}^{k}4^{\,k-j}\binom{k}{j}\\
&=4S_k(4)+S_k(4)\\
&=5S_k(4)\\
&=5\cdot5^k=5^{k+1}.
\end{aligned}
$$
In the second interior family, set $i=j-1$: its bounds become
$0\le i\le k-1$ and its power becomes $4^{k-i}$. The outside $1$
is the missing $i=k$ term, $4^0\binom{k}{k}$. At $k=0$ the interior
sums are empty, so the endpoint calculation still applies.
The induction hypothesis is used only in the final substitution
$S_k(4)=5^k$. Hence the identity holds for all $n\ge0$.

**Decisive check:** both endpoint terms must be absorbed so that each displayed
sum runs all the way from $0$ to $k$.

### C.5 Weight $w=5$

> [!QUESTION]- Full question statement
> You may use Pascal's identity
>
> $$
>
> \binom{k+1}{j}=\binom{k}{j}+\binom{k}{j-1}
> \quad(1\le j\le k),\qquad
> \binom{n}{0}=\binom{n}{n}=1.
>
> $$
>
> Prove by mathematical induction that
>
> $$
>
> \sum_{j=0}^{n} 5^{n-j}\binom{n}{j}=6^n\qquad\text{for every integer }n\ge0.
>
> $$
>
> State $P(n)$, verify the base case, state the induction hypothesis, show the complete next-case calculation including reindexing, and conclude the proof.

Let
$$
P(n):\qquad S_n(5)=\sum_{j=0}^{n}5^{\,n-j}\binom{n}{j}=6^n.
$$

**Base case.** At $n=0$,
$S_0(5)=5^0\binom00=1=6^0$.

**Induction hypothesis and target.** Let $k\ge0$ be arbitrary and assume
$S_k(5)=6^k$. The target is $S_{k+1}(5)=6^{k+1}$.

**Induction step.** Apply Pascal's identity to row $k+1$. Factoring one $5$
from the first family and shifting the second family's index yields two
complete copies of the row-$k$ weighted sum, with coefficients $5$ and $1$:
$$
\begin{aligned}
S_{k+1}(5)
&=5^{k+1}+\sum_{j=1}^{k}5^{k+1-j}
  \left(\binom{k}{j}+\binom{k}{j-1}\right)+1\\
&=5\left(5^k\binom{k}{0}+\sum_{j=1}^{k}5^{k-j}\binom{k}{j}\right)
  +\sum_{i=0}^{k-1}5^{k-i}\binom{k}{i}+1\\
&=5\sum_{j=0}^{k}5^{\,k-j}\binom{k}{j}
  +\sum_{j=0}^{k}5^{\,k-j}\binom{k}{j}\\
&=5S_k(5)+S_k(5)\\
&=6S_k(5)\\
&=6\cdot6^k=6^{k+1}.
\end{aligned}
$$
The second interior sum was reindexed with $i=j-1$; the new range is
$0,\ldots,k-1$, and the outside $1=5^0\binom{k}{k}$ completes it through
$k$. For $k=0$ the interior sums are empty. The induction hypothesis
$S_k(5)=6^k$ enters only in the last line.
This is exactly the required next case, so induction proves the identity for
every $n\ge0$.

**Decisive check:** after the Pascal split, the two families must recombine as
$5S_k(5)+S_k(5)$; a proof that skips this bridge has not shown how the
induction hypothesis applies.
