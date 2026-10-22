---
title: 2300 Divisibility Solutions
aliases: [2300 Divisibility Solutions, Divisibility Solutions]
linter-yaml-title-alias: 2300 Divisibility Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Wednesday, October 21st 2026
publish: true
permalink: core-assessment-solutions/2300-divisibility-solutions
---
# 2300 Divisibility Solutions

> [!IMPORTANT] Public practice bank
> These solutions correspond to public practice-bank problems, not a live graded form. A supervised Core attempt lasts 20 minutes and contains exactly five problems: one from each section A–E. **Meets** requires four fully correct problems; **Exceeds** requires all five. Every retake is a new complete form, including a retake after Meets. Staff record **Not Yet / Meets / Exceeds** as **0 / 4 / 5** in Canvas.

> [!IMPORTANT] Full-credit and grader guidance
> Equivalent computations, residue representatives, Bézout coefficients, and
> valid proof routes are acceptable. A **decisive check** identifies the central
> mathematical evidence, but every requested computation, verification, or proof
> part must still be present for the selected problem to count as correct.

## A. Division Algorithm and Congruence

> [!TIP]- Relevant Materials
> - [Division Algorithm and Congruence (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1dDivisionAlgorithmAndCongruenceModNHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1dDivisionAlgorithmAndCongruenceModN.7.42.mp4)
> - [Division Algorithm Revisited (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1eDivisionAlgorithmRevisitedHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1eDivisionAlgorithmRevisited.7.00.mp4)
> - [[Books/book_sections_md/4.1_Divisibility_and_Modular_Arithmetic|Rosen 4.1 — Divisibility and Modular Arithmetic]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the quotient/remainder or congruence requested,
> the equation $a=bq+r$, the bound $0\le r<b$, and any requested divisibility
> verification. **Decisive check:** for a negative dividend, the remainder must
> still be the least nonnegative representative.

### A.1 Quotients and Remainders

The division algorithm requires $a=bq+r$ with $0\le r<b$.

1. $137=12(11)+5$, so $137\,\mathrm{div}\,12=11$ and $137\bmod12=5$.
2. $-47=9(-6)+7$, so $-47\,\mathrm{div}\,9=-6$ and $-47\bmod9=7$.

The second remainder is $7$, not $-2$, because the canonical remainder must be nonnegative.

### A.2 Three Connected Views

Because $418=23(18)+4$,
$$
418\bmod23=4
\qquad\text{and}\qquad
418\equiv4\pmod{23}.
$$
The bound $0\le4<23$ holds. Also, $418-4=414=23(18)$, so $23\mid(418-4)$, which proves the congruence from its definition.

### A.3 Negative Dividend

We need a nonnegative remainder smaller than $7$:
$$
-83=7(-12)+1.
$$
Thus $q=-12$, $r=1$, $-83\,\mathrm{div}\,7=-12$, $-83\bmod7=1$, and $-83\equiv1\pmod7$.

### A.4 Recover the Integer

Substitute the given quotient and remainder into $a=13q+r$:
$$
a=13(-4)+9=-43.
$$
The remainder is valid because $0\le9<13$.

### A.5 Congruence from Divisibility

The congruence is true because
$$
347-(-13)=360=24(15),
$$
so $24\mid(347-(-13))$. Since $347=24(14)+11$, its least nonnegative residue modulo $24$ is $\boxed{11}$.

## B. Integer Representations

> [!TIP]- Relevant Materials
> - [Numbers in Other Bases (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2aOtherBasesHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2aOtherBases.5.53.mp4)
> - [Horner's Rule: Convert to Decimal (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2bHornersRuleConvertToDecimalHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2bHornersRule.10.32.mp4)
> - [Decimal to Other Bases (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2cDecimalToOtherBasesHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2cDecimalToOtherBases.6.41.mp4)
> - [Binary, Octal, and Hexadecimal (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2dBinaryOctalHexHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2dBinaryOctalHex.4.30.mp4)
> - [[Books/book_sections_md/4.2_Integer_Representations_and_Algorithms|Rosen 4.2 — Integer Representations and Algorithms]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the requested representation in every named base
> and enough place-value, repeated-division, or bit-grouping work to verify it.
> Leading zeroes in grouped binary are optional. **Decisive check:** expanding the
> final digits by powers of the base must recover the original integer.

### B.1 Binary and Decimal

Expanding by place value,
$$
(11010110)_2=128+64+16+4+2=\boxed{214}.
$$
Since $173=128+32+8+4+1$,
$$
173=\boxed{(10101101)_2}.
$$

### B.2 Hexadecimal and Binary

Replace each hexadecimal digit with four binary digits:
$$
(3AF)_{16}=(0011\ 1010\ 1111)_2.
$$
In decimal,
$$
3(16^2)+10(16)+15=768+160+15=\boxed{943}.
$$

### B.3 Octal and Binary

Replace each octal digit with three binary digits:
$$
(725)_8=(111\ 010\ 101)_2.
$$
Also,
$$
7(8^2)+2(8)+5=448+16+5=\boxed{469}.
$$

### B.4 Decimal to Hexadecimal

Repeated division gives
$$
1000=16(62)+8,\qquad 62=16(3)+14.
$$
Reading the remainders upward and writing $14$ as $E$ gives $\boxed{(3E8)_{16}}$. The check is $3(16^2)+14(16)+8=768+224+8=1000$.

### B.5 Cross-Base Conversion

For octal, group bits by threes from the right:
$$
101\ 101\ 011\longrightarrow 5\ 5\ 3,
$$
so $(101101011)_2=\boxed{(553)_8}$. For hexadecimal, group by fours and pad on the left:
$$
0001\ 0110\ 1011\longrightarrow 1\ 6\ B,
$$
so $(101101011)_2=\boxed{(16B)_{16}}$.

## C. Modular Arithmetic

> [!TIP]- Relevant Materials
> - [Arithmetic Modulo $n$ (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1fArithmeticModNHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1fArithmeticModN.9.57.mp4)
> - [Modular Exponentiation (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2hModularExponentiationHandout.pdf) | [Part 1](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2hModularExponentiation.10.55Part1.mp4) | [Part 2](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.2hModularExponentiation.9.14Part2.mp4)
> - [[Books/book_sections_md/4.1_Divisibility_and_Modular_Arithmetic|Rosen 4.1 — Divisibility and Modular Arithmetic]]
> - [[Books/book_sections_md/4.2_Integer_Representations_and_Algorithms|Rosen 4.2 — Integer Representations and Algorithms]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** each requested least nonnegative residue and a
> valid reduction, cycle, or repeated-squaring calculation. Equivalent negative
> representatives are acceptable during the work, but the final residue should
> be in the requested range. **Decisive check:** verify the exponent reduction
> against the actual cycle length rather than reducing the exponent modulo the
> modulus without justification.

### C.1 Residue Computations

Modulo $11$, $-38\equiv6$ and $27\equiv5$, so
$$
(-38)(27)+15\equiv6\cdot5+4=34\equiv\boxed1\pmod{11}.
$$
The powers of $3$ modulo $10$ repeat $3,9,7,1$. Because $47\equiv3\pmod4$,
$$
3^{47}\equiv3^3\equiv\boxed7\pmod{10}.
$$

### C.2 Addition and Products

Modulo $17$, $784\equiv2$ and $519\equiv9$. Therefore
$$
784+519\equiv2+9=\boxed{11}\pmod{17},
$$
and
$$
784\cdot519\equiv2\cdot9=18\equiv\boxed1\pmod{17}.
$$

### C.3 Powers by Cycles

The powers of $7$ modulo $10$ repeat $7,9,3,1$. Since $103\equiv3\pmod4$,
$$
7^{103}\equiv7^3\equiv\boxed3\pmod{10}.
$$

### C.4 Modular Exponentiation

Repeated squaring modulo $13$ gives
$$
5^2\equiv12\equiv-1,
\qquad 5^4\equiv1.
$$
Since $117=64+32+16+4+1$, every selected power except $5^1$ has residue $1$. Hence
$$
5^{117}\equiv1\cdot1\cdot1\cdot1\cdot5\equiv\boxed5\pmod{13}.
$$

### C.5 Preserving Congruence

From $a\equiv b\pmod m$ and $c\equiv d\pmod m$, there are integers $h,k$ such that $a-b=mh$ and $c-d=mk$. Then
$$
ac-bd=a(c-d)+d(a-b)=a(mk)+d(mh)=m(ak+dh).
$$
Thus $m\mid(ac-bd)$, so $\boxed{ac\equiv bd\pmod m}$.

## D. GCD and Bézout Coefficients

> [!TIP]- Relevant Materials
> - [Euclidean Algorithm for GCDs (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.3bGCDEuclideanAlgorithmHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.3bGCDEuclideanAlgorithm.12.26.mp4)
> - [Bézout and the Extended Euclidean Algorithm (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.3dBezoutPlusREEAHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.3dBezoutPlusREEA.13.39.mp4)
> - [[Books/book_sections_md/4.3_Primes_and_Greatest_Common_Divisors|Rosen 4.3 — Primes and Greatest Common Divisors]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** a correct Euclidean-algorithm remainder chain, the
> gcd, and one valid Bézout identity. Different Bézout coefficients earn full
> credit. **Decisive check:** substitute the reported coefficients into the final
> linear combination; it must equal the gcd exactly.

### D.1

The Euclidean algorithm gives
$$
252=198+54,\quad198=3(54)+36,\quad54=36+18,
$$
so $\gcd(252,198)=18$. Back-substitution gives
$$
18=54-36=4(54)-198=4(252)-5(198).
$$
Thus $\boxed{18=4(252)-5(198)}$.

### D.2

$$
662=414+248,\quad414=248+166,\quad248=166+82,\quad166=2(82)+2.
$$
Thus $\gcd(414,662)=2$. Back-substitution gives
$$
2=166-2(82)=3(166)-2(248)=3(414)-5(248)=8(414)-5(662).
$$
Therefore $\boxed{2=8(414)-5(662)}$.

### D.3

$$
544=4(119)+68,\quad119=68+51,\quad68=51+17.
$$
Thus $\gcd(119,544)=17$, and
$$
17=68-51=2(68)-119=2(544)-9(119).
$$
Therefore $\boxed{17=-9(119)+2(544)}$.

### D.4

$$
391=299+92,\qquad299=3(92)+23.
$$
Thus $\gcd(391,299)=23$, and
$$
23=299-3(92)=299-3(391-299)=-3(391)+4(299).
$$
Therefore $\boxed{23=-3(391)+4(299)}$.

### D.5

$$
527=341+186,\quad341=186+155,\quad186=155+31.
$$
Thus $\gcd(527,341)=31$, and
$$
31=186-155=2(186)-341=2(527)-3(341).
$$
Therefore $\boxed{31=2(527)-3(341)}$.

## E. Synthesis and Proof

> [!TIP]- Relevant Materials
> - [Divisibility (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1aDivisibilityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1aDivisibility.5.54.mp4)
> - [Proofs and Divisibility (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1bProofsAndDivisibilityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1bProofsAndDivisibility.6.40.mp4)
> - [[Books/book_sections_md/4.1_Divisibility_and_Modular_Arithmetic|Rosen 4.1 — Divisibility and Modular Arithmetic]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** invoke the relevant definition, introduce integer
> witnesses where needed, and reach the exact divisibility/congruence conclusion;
> for a false claim, give and verify a counterexample. A different correct proof
> or counterexample is acceptable. **Decisive check:** the final displayed form
> must expose the required divisor as an integer factor, or make all premises true
> and the claimed conclusion false.

### E.1 Divisibility from Linear Combinations

Because $d\mid a$ and $d\mid b$, there are integers $r,s$ such that $a=dr$ and $b=ds$. For arbitrary integers $m,n$,
$$
ma+nb=m(dr)+n(ds)=d(mr+ns).
$$
Because $mr+ns$ is an integer, the definition of divisibility gives $\boxed{d\mid(ma+nb)}$. The first hypothesis supplied $a=dr$; the second supplied $b=ds$.

### E.2 A Congruence Proof

If $n$ is odd, then $n=2k+1$ for some integer $k$. Therefore
$$
n^2-1=(2k+1)^2-1=4k(k+1).
$$
One of the consecutive integers $k,k+1$ is even, so $k(k+1)=2t$ for some integer $t$. Hence $n^2-1=8t$, which proves $\boxed{n^2\equiv1\pmod8}$.

### E.3 Divisibility Chain

If $a\mid b$, then $b=ar$ for some integer $r$. If $b\mid c$, then $c=bs$ for some integer $s$. Substitution gives
$$
c=(ar)s=a(rs).
$$
Since $rs$ is an integer, $\boxed{a\mid c}$.

### E.4 Diagnose a False Claim

Take $a=6$, $b=2$, and $c=3$. Then $6\mid(2\cdot3)$, but $6\nmid2$ and $6\nmid3$. Thus the original claim is false. If $a$ is prime, Euclid's lemma makes the implication true: $a\mid bc$ implies $a\mid b$ or $a\mid c$.

### E.5 Consecutive Integers

Among any three consecutive integers, at least one is even, so their product has a factor of $2$. Exactly one is divisible by $3$, so their product also has a factor of $3$. Since $2$ and $3$ are coprime, the product is divisible by $2\cdot3=6$.
