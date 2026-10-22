---
title: 2300 Counting Solutions
aliases: [2300 Counting Solutions, Counting Solutions]
linter-yaml-title-alias: 2300 Counting Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Wednesday, October 21st 2026
publish: true
permalink: core-assessment-solutions/2300-counting-solutions
---
# 2300 Counting Solutions

> [!IMPORTANT] Public practice bank
> These solutions correspond to practice-bank problems, not a live graded form. A supervised attempt lasts 20 minutes and contains exactly five problems, one from each section A–E. **Meets** requires four fully correct problems; **Exceeds** requires all five. Every retake is a new complete form. Staff record **Not Yet / Meets / Exceeds** as **0 / 4 / 5** in Canvas.

> [!IMPORTANT] Full-credit and grader guidance
> An unsimplified exact expression is full credit whenever the problem permits it.
> Equivalent counting decompositions and probability calculations are acceptable.
> The **decisive check** in each section locates the modeling choice a grader should
> inspect first; all explicitly requested interpretations and subparts remain
> required.

## A. Fundamental Counting Rules

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/6.1_The_Basics_of_Counting|Rosen 6.1 — The Basics of Counting]]
> - [[Books/book_sections_md/6.2_The_Pigeonhole_Principle|Rosen 6.2 — The Pigeonhole Principle]]
> - [Counting Methods (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1aMultiplicationRuleHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1aMultiplicationRule.4.58.mp4)
> - [More Counting Methods (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethodsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethods.13.17.mp4)
> - [Pigeonhole Principle (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.2PigeonholePrincipleHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.2PigeonholePrinciple.9.19.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the correct sum/product/function count or ceiling,
> plus the requested rule or explanation. **Decisive check:** decide first whether
> the choices are disjoint alternatives, sequential independent choices, or
> objects forced into buckets.

### A.1 Sum Rule

The soup and salad choices are disjoint alternatives, so the sum rule gives
$$5+4=9$$
possible lunches.

### A.2 Product Rule

The five positions are filled in sequence. Repetition leaves 26 choices for each letter and 10 for each digit, so the product rule gives
$$26^2\cdot 10^3.$$

### A.3 Counting Functions

Each of the five domain elements independently chooses one of eight images. Thus the number of functions is
$$8^5.$$

### A.4 Inclusion–Exclusion

The two set sizes count the intersection twice. Inclusion–exclusion gives
$$|A\cup B|=|A|+|B|-|A\cap B|=19+20-8=31.$$

### A.5 Generalized Pigeonhole Principle

The generalized pigeonhole principle guarantees a bucket containing at least
$$\left\lceil\frac{40}{20}\right\rceil=2$$
keys. It does not guarantee three: a distribution with exactly two keys in every bucket is possible.

## B. Arrangements and Selections

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/6.3_Permutations_and_Combinations|Rosen 6.3 — Permutations and Combinations]]
> - [[Books/book_sections_md/6.4_Binomial_Coefficients_and_Identities|Rosen 6.4 — Binomial Coefficients and Identities]]
> - [Permutations and Combinations (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.3PermutationsAndCombinationsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.3PermutationsAndCombination.6.55.mp4)
> - [Binomial Theorem (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.4aBinomialTheoremHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.4aBinomialTheorem.9.09.mp4)
> - [Binomial-Coefficient Identities (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.4bBinomialCoefficientTheoremsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.4bBinomialCoefficientTheorems.13.37.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** a correct permutation, combination, repeated-letter,
> or coefficient expression; an exact unsimplified form is enough unless a number
> is requested. **Decisive check:** ask whether changing the order produces a new
> outcome and whether any objects are indistinguishable.

### B.1 Committees

Only the selected set matters, so order does not matter:
$$\binom{10}{3}=120.$$

### B.2 Distinct Offices

The two offices are distinguishable, so order matters:
$$P(10,2)=10\cdot 9=90.$$

### B.3 Repeated Letters

There are six letters, with three A's and two N's indistinguishable:
$$\frac{6!}{3!2!}=60.$$

### B.4 Fixed-Weight Bit Strings

Choose the three positions occupied by the $1$s:
$$\binom{8}{3}=56.$$

### B.5 Binomial Coefficient

The binomial theorem gives
$$(1+x)^8=\sum_{k=0}^8\binom{8}{k}x^k.$$
Therefore the coefficient of $x^3$ is
$$\binom{8}{3}=56.$$

## C. Constrained Counting

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/6.1_The_Basics_of_Counting|Rosen 6.1 — The Basics of Counting]]
> - [[Books/book_sections_md/6.3_Permutations_and_Combinations|Rosen 6.3 — Permutations and Combinations]]
> - [[Books/book_sections_md/6.4_Binomial_Coefficients_and_Identities|Rosen 6.4 — Binomial Coefficients and Identities]]
> - [More Counting Methods (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethodsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethods.13.17.mp4)
> - [Permutations and Combinations (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.3PermutationsAndCombinationsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.3PermutationsAndCombination.6.55.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the correct exact expression and an explanation of
> every restriction, complement, or independent selection. Equivalent direct and
> complementary counts are acceptable. **Decisive check:** make sure every counted
> object satisfies the constraint exactly once.

### C.1 Card Hands

Choose two of the 13 hearts and three of the 39 non-hearts:
$$\binom{13}{2}\binom{39}{3}.$$

### C.2 Complement Counting

There are $2^8$ bit strings in total. Exclude the one string with no $1$s and the eight strings with exactly one $1$:
$$2^8-\binom80-\binom81=256-1-8=247.$$

### C.3 Mixed Committees

Choose the three computer-science majors and the two mathematics majors independently:
$$\binom{12}{3}\binom{8}{2}.$$

### C.4 Injective Functions

The five domain elements must receive distinct images. Their ordered choices are
$$P(8,5)=8\cdot7\cdot6\cdot5\cdot4=6720.$$

### C.5 Codes with a Required First Type

There are five choices for the initial vowel. After it is used, the remaining five positions are filled without repetition from the remaining 25 letters:
$$5\cdot25\cdot24\cdot23\cdot22\cdot21=5P(25,5).$$

## D. Probability Models

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/7.1_An_Introduction_to_Discrete_Probability|Rosen 7.1 — Introduction to Discrete Probability]]
> - [[Books/book_sections_md/7.2_Probability_Theory|Rosen 7.2 — Probability Theory]]
> - [Discrete Probability (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.1aDiscreteProbabilityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.1aDiscreteProbability.7.07.mp4)
> - [Probability Laws (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.1bProbabilityLawsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.1bProbabilityLaws.9.22.mp4)
> - [Conditional Probability (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2aConditionalProbabilityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2aConditionalProbability.11.57.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** a correct sample space or probability identity,
> exact probability, and the requested conditioning/product work. An equivalent
> favorable-outcome count is acceptable. **Decisive check:** the denominator must
> match the conditioning event, and without-replacement denominators must change.

### D.1 Coin and Die

There are 12 equally likely outcomes. Six have heads; among the six tails outcomes, three have an even die. Hence
$$P(H\cup\text{even})=\frac{6+3}{12}=\frac34.$$

### D.2 Probability Identities

Inclusion–exclusion gives
$$P(A\cup B)=0.55+0.40-0.25=0.70.$$
The part of $B$ outside $A$ is
$$P(A^c\cap B)=P(B)-P(A\cap B)=0.40-0.25=0.15.$$

### D.3 Bit-String Probability

All $2^8$ strings are equally likely, and $\binom83$ have exactly three $1$s. Therefore
$$P(\text{exactly three 1s})=\frac{\binom83}{2^8}=\frac{56}{256}=\frac7{32}.$$

### D.4 Without Replacement

Use the conditional product rule:
$$P(R_1\cap B_2)=P(R_1)P(B_2\mid R_1)=\frac4{10}\cdot\frac6{9}=\frac4{15}.$$

### D.5 Conditional Probabilities

The conditioning set determines the denominator:
$$P(\text{Python}\mid\text{Java})=\frac{10}{18}=\frac59,\qquad
P(\text{Java}\mid\text{Python})=\frac{10}{24}=\frac5{12}.$$

## E. Modeling and Interpretation

> [!TIP]- Relevant Materials
> - [[Books/book_sections_md/7.2_Probability_Theory|Rosen 7.2 — Probability Theory]]
> - [[Books/book_sections_md/7.3_Bayes’_Theorem|Rosen 7.3 — Bayes' Theorem]]
> - [[Books/book_sections_md/7.4_Expected_Value_and_Variance|Rosen 7.4 — Expected Value and Variance]]
> - [More Conditional Probability (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2bMoreConditionalProbabilityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2bMoreConditionalProbability.10.35.mp4)
> - [Independence of Events (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2cIndependenceOfEventsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.2cIndependenceOfEvents.8.47.mp4)
> - [Bayes' Rule (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.3BayesRuleHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.3BayesRule.12.16.mp4)
> - [Expected Value and Variance (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.4ExpectedValueAndVarianceHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch7/2300.7.4ExpectedValueAndVariance.9.59.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the full numerical model and the requested verbal
> interpretation. Equivalent probability-tree, table, or formula work is
> acceptable. **Decisive check:** include base rates in Bayes problems, subtract
> costs when the prompt asks for net value, and compare the within-group rates
> separately from the aggregate rates.

### E.1 Independence Test

Because
$$P(A)P(B)=0.6(0.5)=0.3=P(A\cap B),$$
the events are independent. Also,
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{0.3}{0.5}=0.6.$$

### E.2 Screening and Base Rates

Total probability gives
$$P(+)=0.01(0.95)+0.99(0.08)=0.0887.$$
Bayes' rule then gives
$$P(\text{condition}\mid +)=\frac{0.01(0.95)}{0.0887}\approx0.1071.$$
The result is much smaller than $95\%$ because the low base rate leaves many more unaffected people available to produce false positives.

### E.3 Factory Bayes Model

The overall defective probability is
$$P(D)=0.40(0.03)+0.60(0.01)=0.018.$$
Therefore
$$P(A\mid D)=\frac{0.40(0.03)}{0.018}=\frac{0.012}{0.018}=\frac23.$$

### E.4 Expected Net Value

The expected payout is
$$10\left(\frac16\right)+2\left(\frac26\right)=\frac{14}{6}=\frac73.$$
After subtracting the $2$ cost, the expected net value is
$$\frac73-2=\frac13\text{ dollar}.$$
Its positive sign means a long-run average gain of about 33 cents per play.

### E.5 Aggregation Reversal

Within Group 1, Treatment B has the higher rate because $400/1000>30/100$. Within Group 2, Treatment B again has the higher rate because $90/100>800/1000$.

Overall,
$$P(\text{success}\mid A)=\frac{830}{1100},\qquad
P(\text{success}\mid B)=\frac{490}{1100},$$
so Treatment A has the higher aggregate rate. The reversal occurs because A was used mostly in the higher-success group while B was used mostly in the lower-success group; aggregation changes the weights.

> [!TIP]- More Resources
> [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)
