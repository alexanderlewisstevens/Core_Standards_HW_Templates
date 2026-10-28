---
title: 2300 Divisibility Solutions
aliases: [2300 Divisibility Solutions, Divisibility Solutions]
linter-yaml-title-alias: 2300 Divisibility Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Thursday, October 22nd 2026
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

## How to use these solutions

For a computation, follow three moves: **choose the relevant definition or
algorithm**, **show the intermediate arithmetic**, and **verify the final
representation**. For a proof, introduce integer witnesses from the definition
of divisibility or congruence, manipulate the expression, and finish by naming
the integer witness that establishes the conclusion.

## A. Division Algorithm and Congruence

> [!TIP]- Relevant Materials
> - [Divisibility companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/divisibility_core_companion.pdf)
> - [Division Algorithm and Congruence (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1dDivisionAlgorithmAndCongruenceModNHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1dDivisionAlgorithmAndCongruenceModN.7.42.mp4)
> - [Division Algorithm Revisited (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1eDivisionAlgorithmRevisitedHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch4/2300.4.1eDivisionAlgorithmRevisited.7.00.mp4)
> - [[Books/book_sections_md/4.1_Divisibility_and_Modular_Arithmetic|Rosen 4.1 — Divisibility and Modular Arithmetic]]

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the quotient/remainder or congruence requested,
> the equation $a=bq+r$, the bound $0\le r<b$, and any requested divisibility
> verification. **Decisive check:** for a negative dividend, the remainder must
> still be the least nonnegative representative.

### A.1 Quotients and Remainders

> [!QUESTION]- Full question statement
> **Common directions.** Use the division algorithm and the least
> nonnegative remainder. Justify congruence claims from the definition.
>
> For each pair $(a,b)$, find $a\,\mathrm{div}\,b$ and $a\bmod b$, then write
> $a=bq+r$: (a) $(137,12)$; (b) $(-47,9)$.

The division algorithm requires $a=bq+r$ with $0\le r<b$.

1. For $137$ divided by $12$, choose $q=11$ because $12(11)=132$. The
   remainder is $137-132=5$, so $137=12(11)+5$. Since $0\le5<12$,
   $137\,\mathrm{div}\,12=11$ and $137\bmod12=5$.
2. For $-47$ divided by $9$, $q=-5$ would give remainder $-2$, which is not
   allowed. Decrease the quotient to $-6$: $9(-6)=-54$, and
   $-47-(-54)=7$. Thus $-47=9(-6)+7$, with $0\le7<9$, so
   $-47\,\mathrm{div}\,9=-6$ and $-47\bmod9=7$.

The inequality check is what selects $7$, rather than $-2$, as the canonical
remainder.

### A.2 Three Connected Views

> [!QUESTION]- Full question statement
> **Common directions.** Use the division algorithm and the least
> nonnegative remainder. Justify congruence claims from the definition.
>
> Complete the three equivalent descriptions and verify $0\le r<23$:
>
> $$
>
> \begin{gathered}
> 418=23q+r,\qquad 418\bmod 23=r,\\
> 418\equiv r\pmod{23}.
> \end{gathered}
>
> $$

**Division view:** $418=23(18)+4$, and $0\le4<23$. Therefore
$$
418\bmod23=4
\qquad\text{and}\qquad
418\equiv4\pmod{23}.
$$
**Divisibility view:** subtract the proposed residue:
$418-4=414=23(18)$. Hence $23\mid(418-4)$, which verifies the congruence
directly from its definition.

### A.3 Negative Dividend

> [!QUESTION]- Full question statement
> **Common directions.** Use the division algorithm and the least
> nonnegative remainder. Justify congruence claims from the definition.
>
> Find $q,r$ such that $-83=7q+r$ and $0\le r<7$. State
> $-83\,\mathrm{div}\,7$, $-83\bmod7$, and the corresponding congruence.

Start from $-83=7(-11)-6$, but $-6$ is not an allowed remainder. Replace
$-6$ by $1$ and decrease the quotient by $1$:
$$
-83=7(-12)+1.
$$
Now $0\le1<7$, so $q=-12$, $r=1$,
$-83\,\mathrm{div}\,7=-12$, $-83\bmod7=1$, and
$-83\equiv1\pmod7$.

### A.4 Recover the Integer

> [!QUESTION]- Full question statement
> **Common directions.** Use the division algorithm and the least
> nonnegative remainder. Justify congruence claims from the definition.
>
> An integer $a$ satisfies $a\,\mathrm{div}\,13=-4$ and $a\bmod13=9$.
> Find $a$ and verify the required remainder bound.

Use the division-algorithm equation $a=13q+r$. Substitute $q=-4$ and $r=9$:
$$
a=13(-4)+9=-52+9=-43.
$$
The remainder check $0\le9<13$ confirms that these really are the canonical
quotient and remainder.

### A.5 Congruence from Divisibility

> [!QUESTION]- Full question statement
> **Common directions.** Use the division algorithm and the least
> nonnegative remainder. Justify congruence claims from the definition.
>
> Decide whether $347\equiv-13\pmod{24}$. Justify directly from the definition,
> then give the least nonnegative residue of $347$ modulo $24$.

To test $347\equiv-13\pmod{24}$, subtract the two numbers:
$$
347-(-13)=360=24(15),
$$
so $24\mid(347-(-13))$ and the congruence is true. To find the canonical
representative, write $347=24(14)+11$. Because $0\le11<24$, the least
nonnegative residue is $\boxed{11}$.

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

> [!QUESTION]- Full question statement
> **Common directions.** Show place values, digit grouping, or repeated
> division as appropriate, and check that every digit is valid in its base.
>
> Convert $(11010110)_2$ to decimal, and convert $173$ from decimal to binary.

For binary to decimal, attach each bit to its power of $2$:
$$
(11010110)_2
=1(2^7)+1(2^6)+0(2^5)+1(2^4)+0(2^3)+1(2^2)+1(2)+0
=128+64+16+4+2=\boxed{214}.
$$
For decimal to binary, choose powers of $2$ from largest to smallest:
$173=128+32+8+4+1=2^7+2^5+2^3+2^2+2^0$. Put $1$s in exactly those
positions and $0$s elsewhere:
$$
173=\boxed{(10101101)_2}.
$$

### B.2 Hexadecimal and Binary

> [!QUESTION]- Full question statement
> **Common directions.** Show place values, digit grouping, or repeated
> division as appropriate, and check that every digit is valid in its base.
>
> Convert $(\mathrm{3AF})_{16}$ to binary and decimal. Keep four binary digits
> for each hexadecimal digit.

Replace each hexadecimal digit with its four-bit block:
$$
3\mapsto0011,\qquad A(=10)\mapsto1010,\qquad F(=15)\mapsto1111,
$$
so
$$
(3AF)_{16}=(0011\ 1010\ 1111)_2.
$$
To verify in decimal, use hexadecimal place values:
$$
3(16^2)+10(16)+15=768+160+15=\boxed{943}.
$$

### B.3 Octal and Binary

> [!QUESTION]- Full question statement
> **Common directions.** Show place values, digit grouping, or repeated
> division as appropriate, and check that every digit is valid in its base.
>
> Convert $(725)_8$ to binary and decimal. Keep three binary digits for each
> octal digit.

Replace each octal digit with its three-bit block:
$$
7\mapsto111,\qquad2\mapsto010,\qquad5\mapsto101,
$$
so $(725)_8=(111\ 010\ 101)_2$. A decimal check gives
$$
7(8^2)+2(8)+5=448+16+5=\boxed{469}.
$$

### B.4 Decimal to Hexadecimal

> [!QUESTION]- Full question statement
> **Common directions.** Show place values, digit grouping, or repeated
> division as appropriate, and check that every digit is valid in its base.
>
> Convert $1000$ from decimal to hexadecimal using repeated division. Check by
> expanding the result in powers of $16$.

Repeated division by $16$ records one remainder at each step:
$$
1000=16(62)+8,\qquad 62=16(3)+14.
$$
The final quotient is $3$. Read the final quotient and then the remainders from
last to first: $3,14,8$. Writing $14$ as $E$ gives
$\boxed{(3E8)_{16}}$. Verify:
$3(16^2)+14(16)+8=768+224+8=1000$.

### B.5 Cross-Base Conversion

> [!QUESTION]- Full question statement
> **Common directions.** Show place values, digit grouping, or repeated
> division as appropriate, and check that every digit is valid in its base.
>
> Convert $(101101011)_2$ to octal and hexadecimal without first converting the
> whole number to decimal. Explain the grouping rule.

For octal, group bits by threes from the right and translate each block:
$$
101\ 101\ 011\longrightarrow 5\ 5\ 3,
$$
so $(101101011)_2=\boxed{(553)_8}$. For hexadecimal, group by fours from the
right, padding only the leftmost group:
$$
0001\ 0110\ 1011\longrightarrow 1\ 6\ B,
$$
so $(101101011)_2=\boxed{(16B)_{16}}$. Grouping from the right preserves the
place values of the original bits.

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

> [!QUESTION]- Full question statement
> **Common directions.** Give least nonnegative residues and show
> reductions that avoid unnecessarily large arithmetic.
>
> Compute (a) $\bigl((-38)(27)+15\bigr)\bmod11$ and
> (b) $3^{47}\bmod10$.

First reduce each term modulo $11$: $-38=-44+6$, so $-38\equiv6$;
$27=22+5$, so $27\equiv5$; and $15\equiv4$. Therefore
$$
(-38)(27)+15\equiv6\cdot5+4=34\equiv\boxed1\pmod{11}.
$$
For the power, list one full cycle:
$3^1,3^2,3^3,3^4\equiv3,9,7,1\pmod{10}$. The cycle length is $4$, and
$47=4(11)+3$, so
$$
3^{47}\equiv3^3\equiv\boxed7\pmod{10}.
$$

### C.2 Addition and Products

> [!QUESTION]- Full question statement
> **Common directions.** Give least nonnegative residues and show
> reductions that avoid unnecessarily large arithmetic.
>
> Compute the residues of $784+519$ and $784\cdot519$ modulo $17$. Reduce the
> factors before combining them.

Divide to obtain small representatives:
$784=17(46)+2$ and $519=17(30)+9$. Thus $784\equiv2$ and $519\equiv9$
modulo $17$. Reduce after each operation:
$$
784+519\equiv2+9=\boxed{11}\pmod{17},
$$
and
$$
784\cdot519\equiv2\cdot9=18\equiv\boxed1\pmod{17}.
$$

### C.3 Powers by Cycles

> [!QUESTION]- Full question statement
> **Common directions.** Give least nonnegative residues and show
> reductions that avoid unnecessarily large arithmetic.
>
> Compute $7^{103}\bmod10$. Identify the cycle and explain how the exponent
> selects the answer.

Compute until the residue returns to $1$:
$7^1,7^2,7^3,7^4\equiv7,9,3,1\pmod{10}$. This gives a cycle of length $4$.
Since $103=4(25)+3$,
$$
7^{103}\equiv7^3\equiv\boxed3\pmod{10}.
$$

### C.4 Modular Exponentiation

> [!QUESTION]- Full question statement
> **Common directions.** Give least nonnegative residues and show
> reductions that avoid unnecessarily large arithmetic.
>
> Compute $5^{117}\bmod13$ by repeated squaring. Display the powers used in the
> final product.

Repeated squaring modulo $13$ gives
$$
5^2\equiv12\equiv-1,
\qquad 5^4\equiv1.
$$
Squaring again shows $5^8,5^{16},5^{32},5^{64}\equiv1$. Decompose the
exponent as $117=64+32+16+4+1$. Every selected power except $5^1$ therefore
has residue $1$, so
$$
5^{117}\equiv1\cdot1\cdot1\cdot1\cdot5\equiv\boxed5\pmod{13}.
$$

### C.5 Preserving Congruence

> [!QUESTION]- Full question statement
> **Common directions.** Give least nonnegative residues and show
> reductions that avoid unnecessarily large arithmetic.
>
> Suppose $a\equiv b\pmod m$ and $c\equiv d\pmod m$, where
> $a,b,c,d\in\mathbb Z$ and $m\ge2$. Prove from the definition that
> $ac\equiv bd\pmod m$.

Unpack both congruences. There are integers $h,k$ such that
$a-b=mh$ and $c-d=mk$. To create $ac-bd$, add and subtract $ad$:
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


> [!QUESTION]- Full question statement
> **Common directions.** Use the Euclidean algorithm to find the gcd.
> Then back-substitute through your displayed equations to find integers $s,t$
> in the requested Bézout identity.
>
> Find $\gcd(252,198)$ and integers $s,t$ such that
> $252s+198t=\gcd(252,198)$.

The Euclidean algorithm gives
$$
252=198+54,\quad198=3(54)+36,\quad54=36+18,
$$
and the next remainder is $0$, so the last nonzero remainder is
$\gcd(252,198)=18$. Now reverse the equations:
$$
18=54-36
=54-[198-3(54)]
=4(54)-198
=4(252-198)-198
=4(252)-5(198).
$$
Thus $\boxed{18=4(252)-5(198)}$. Substitution verifies
$4(252)-5(198)=1008-990=18$.

### D.2


> [!QUESTION]- Full question statement
> **Common directions.** Use the Euclidean algorithm to find the gcd.
> Then back-substitute through your displayed equations to find integers $s,t$
> in the requested Bézout identity.
>
> Find $\gcd(414,662)$ and express it as $414s+662t$.

$$
662=414+248,\quad414=248+166,\quad248=166+82,\quad166=2(82)+2.
$$
The next remainder is $0$, so $\gcd(414,662)=2$. Back-substitute one equation
at a time:
$$
\begin{aligned}
2&=166-2(82)\\
 &=166-2(248-166)=3(166)-2(248)\\
 &=3(414-248)-2(248)=3(414)-5(248)\\
 &=3(414)-5(662-414)=8(414)-5(662).
\end{aligned}
$$
Therefore $\boxed{2=8(414)-5(662)}$; checking gives $3312-3310=2$.

### D.3


> [!QUESTION]- Full question statement
> **Common directions.** Use the Euclidean algorithm to find the gcd.
> Then back-substitute through your displayed equations to find integers $s,t$
> in the requested Bézout identity.
>
> Find $\gcd(119,544)$ and express it as $119s+544t$.

$$
544=4(119)+68,\quad119=68+51,\quad68=51+17.
$$
The last nonzero remainder is $17$, so $\gcd(119,544)=17$. Reverse the chain:
$$
17=68-51=68-(119-68)=2(68)-119
=2(544-4(119))-119=2(544)-9(119).
$$
Therefore $\boxed{17=-9(119)+2(544)}$, and substitution confirms the value.

### D.4


> [!QUESTION]- Full question statement
> **Common directions.** Use the Euclidean algorithm to find the gcd.
> Then back-substitute through your displayed equations to find integers $s,t$
> in the requested Bézout identity.
>
> Find $\gcd(391,299)$ and express it as $391s+299t$.

$$
391=299+92,\qquad299=3(92)+23.
$$
The next division has remainder $0$, so $\gcd(391,299)=23$. Substitute
$92=391-299$ into the last nonzero remainder:
$$
23=299-3(92)=299-3(391-299)=-3(391)+4(299).
$$
Therefore $\boxed{23=-3(391)+4(299)}$; indeed, $-1173+1196=23$.

### D.5


> [!QUESTION]- Full question statement
> **Common directions.** Use the Euclidean algorithm to find the gcd.
> Then back-substitute through your displayed equations to find integers $s,t$
> in the requested Bézout identity.
>
> Find $\gcd(527,341)$ and express it as $527s+341t$.

$$
527=341+186,\quad341=186+155,\quad186=155+31.
$$
The last nonzero remainder is $31$, so $\gcd(527,341)=31$. Back-substitute:
$$
31=186-155=2(186)-341=2(527)-3(341).
$$
Therefore $\boxed{31=2(527)-3(341)}$, and $1054-1023=31$ verifies the
coefficients.

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

> [!QUESTION]- Full question statement
> **Common directions.** State arbitrary elements and integer witnesses
> explicitly. End by matching the definition of the conclusion.
>
> Let $d,a,b,m,n\in\mathbb Z$. Suppose $d\mid a$ and $d\mid b$. Prove directly
> from the definition that $d\mid(ma+nb)$. State where each hypothesis is used.

Unpack both divisibility hypotheses. Since $d\mid a$ and $d\mid b$, there are
integers $r,s$ such that $a=dr$ and $b=ds$. For arbitrary integers $m,n$,
$$
ma+nb=m(dr)+n(ds)=d(mr+ns).
$$
Because $m,n,r,s$ are integers, closure gives $mr+ns\in\mathbb Z$. Thus the
last display writes $ma+nb$ as $d$ times an integer, so
$\boxed{d\mid(ma+nb)}$. The witness is $mr+ns$.

### E.2 A Congruence Proof

> [!QUESTION]- Full question statement
> **Common directions.** State arbitrary elements and integer witnesses
> explicitly. End by matching the definition of the conclusion.
>
> Prove that if $n$ is odd, then $n^2\equiv1\pmod{8}$. Begin with the definition
> of odd and end by exhibiting an integer multiplier of $8$.

Let $n$ be odd, so $n=2k+1$ for some integer $k$. Expand and factor:
$$
n^2-1=(2k+1)^2-1=4k(k+1).
$$
One of the consecutive integers $k,k+1$ is even, so their product is even:
$k(k+1)=2t$ for some $t\in\mathbb Z$. Substitution gives
$n^2-1=4(2t)=8t$, hence $8\mid(n^2-1)$. By the definition of congruence,
$\boxed{n^2\equiv1\pmod8}$.

### E.3 Divisibility Chain

> [!QUESTION]- Full question statement
> **Common directions.** State arbitrary elements and integer witnesses
> explicitly. End by matching the definition of the conclusion.
>
> Prove directly that if $a\mid b$ and $b\mid c$, then $a\mid c$. Use distinct
> integer witnesses for the two hypotheses.

Unpack each hypothesis separately. If $a\mid b$, then $b=ar$ for some
$r\in\mathbb Z$. If $b\mid c$, then $c=bs$ for some $s\in\mathbb Z$.
Substitute the first equation into the second:
$$
c=(ar)s=a(rs).
$$
Since $rs\in\mathbb Z$, the equation writes $c$ as $a$ times an integer.
Therefore $\boxed{a\mid c}$.

### E.4 Diagnose a False Claim

> [!QUESTION]- Full question statement
> **Common directions.** State arbitrary elements and integer witnesses
> explicitly. End by matching the definition of the conclusion.
>
> Give a numerical counterexample to “if $a\mid bc$, then $a\mid b$ or
> $a\mid c$.” Then state the corrected theorem under the extra hypothesis that
> $a$ is prime.

To refute the claim, make the divisor composite and split its factors. Take
$a=6$, $b=2$, and $c=3$. The premise is true because
$bc=6=6(1)$, so $6\mid bc$. The conclusion is false because $6\nmid2$ and
$6\nmid3$. Thus the implication is false. If $a$ is prime, Euclid's lemma
supplies the corrected theorem: $a\mid bc$ implies $a\mid b$ or $a\mid c$.

### E.5 Consecutive Integers

> [!QUESTION]- Full question statement
> **Common directions.** State arbitrary elements and integer witnesses
> explicitly. End by matching the definition of the conclusion.
>
> Prove that the product of any three consecutive integers is divisible by $6$.
> Exhibit factors of $2$ and $3$, then combine their integer witnesses to
> produce an integer factor of $6$.

Let $n\in\mathbb Z$ be arbitrary and set $P=n(n+1)(n+2)$.

**Exhibit the factor of $2$.** One of $n,n+1$ is even. If $n=2k$, then
$P=2[k(n+1)(n+2)]$; if $n+1=2k$, then $P=2[nk(n+2)]$. In either case
$P=2r$ for an explicitly displayed integer $r$.

**Exhibit the factor of $3$.** If $n\equiv0,1,2\pmod3$, respectively,
then $n,n+2,n+1$, respectively, is a multiple of $3$. Write that factor as
$3\ell$. Multiplying $\ell$ by the other two integer factors gives an integer
$s$ with $P=3s$.

**Combine the witnesses, not just the divisibility claims.** Since
$3-2=1$, both expressions for $P$ give
$$
P=3P-2P=3(2r)-2(3s)=6(r-s).
$$
The number $r-s$ is an integer, so the definition of divisibility gives
$6\mid P$. This also covers negative integers and products containing zero.

**Minimum full-credit bridge:** after establishing $P=2r=3s$ with
$r,s\in\mathbb Z$, the single line $P=6(r-s)$ supplies the requested
factor-$6$ witness. Merely citing $\gcd(2,3)=1$ omits that requested step.
