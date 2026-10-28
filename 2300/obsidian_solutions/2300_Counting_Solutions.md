---
title: 2300 Counting Solutions
aliases: [2300 Counting Solutions, Counting Solutions]
linter-yaml-title-alias: 2300 Counting Solutions
date created: Saturday, March 7th 2026, 8:03:22 pm
date modified: Thursday, October 22nd 2026
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

### How to read a counting solution

For every problem, separate **modeling** from **calculation**:

1. Describe one outcome being counted or one experiment being performed.
2. Decide whether the next choices are alternatives (add), successive choices (multiply), unordered selections (combine), ordered selections (permute), or complementary cases (subtract from a total).
3. Write an exact expression and label what each factor, term, numerator, and denominator counts.
4. Check that every allowed outcome appears exactly once and every forbidden outcome appears zero times.
5. Only then simplify and interpret the result in the words of the problem.

## A. Fundamental Counting Rules

> [!TIP]- Relevant Materials
> - [Counting companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/counting_core_companion.pdf)
> - [[Books/book_sections_md/6.1_The_Basics_of_Counting|Rosen 6.1 — The Basics of Counting]]
> - [[Books/book_sections_md/6.2_The_Pigeonhole_Principle|Rosen 6.2 — The Pigeonhole Principle]]
> - [Counting Methods (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1aMultiplicationRuleHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1aMultiplicationRule.4.58.mp4)
> - [More Counting Methods (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethodsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.1cMoreCountingMethods.13.17.mp4)
> - [Pigeonhole Principle (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.2PigeonholePrincipleHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch6/2300.6.2PigeonholePrinciple.9.19.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the correct sum/product/function count or ceiling,
> plus the requested rule or explanation. **Decisive check:** decide first whether
> the choices are disjoint alternatives, successive choices, or
> objects forced into buckets.

### A.1 Sum Rule

> [!QUESTION]- Full question statement
> A cafe offers 5 soups and 4 salads. A lunch includes either one soup
> or one salad, but not both. How many lunches are possible? Name the counting
> rule.

1. One lunch contains either one soup or one salad.
2. These are disjoint alternatives: no lunch in this model is counted in both categories.
3. Add the five soup choices and four salad choices:
   $$5+4=9.$$

Therefore there are **9 possible lunches**, by the **sum rule**.

### A.2 Product Rule

> [!QUESTION]- Full question statement
> A password contains two uppercase letters followed by three digits.
> Repetition is allowed. How many passwords are possible? Give an unsimplified
> product and name the counting rule.

1. Fill the five positions in order: letter, letter, digit, digit, digit.
2. Repetition is allowed, so a previous choice does not reduce a later choice.
3. The numbers of choices are $26,26,10,10,10$.
4. Multiply successive choices:
   $$26\cdot26\cdot10\cdot10\cdot10=26^2\cdot10^3.$$

This is the **product rule**: each factor counts the choices for one position.

### A.3 Counting Functions

> [!QUESTION]- Full question statement
> Let $A=\{1,2,3,4,5\}$ and $B=\{1,2,\ldots,8\}$. How many functions
> $f:A\to B$ exist? Identify the sequence of choices being counted.

Label the five domain elements. A function is completely determined once an
image is chosen for each label. Each domain element has eight possible images,
and ordinary functions allow the same image to be reused. Thus the product
rule gives
$$\underbrace{8\cdot8\cdot8\cdot8\cdot8}_{\text{one factor per domain element}}=8^5.$$

### A.4 Inclusion–Exclusion

> [!QUESTION]- Full question statement
> If $|A|=19$, $|B|=20$, and $|A\cap B|=8$, find $|A\cup B|$. Write
> the formula you used and name the principle.

Adding $|A|+|B|$ counts elements in $A\cap B$ twice: once as members of $A$
and once as members of $B$. Subtract one copy of the overlap:
$$
|A\cup B|=|A|+|B|-|A\cap B|=19+20-8=31.
$$
Every element in the union is then counted exactly once. This is the
**inclusion–exclusion principle** for two sets.

### A.5 Generalized Pigeonhole Principle

> [!QUESTION]- Full question statement
> A hash table maps 40 distinct keys to 20 possible hash values. What
> bucket occupancy is guaranteed? State the generalized pigeonhole calculation
> and explain why the data do not guarantee a larger occupancy.

1. The objects are the 40 keys; the boxes are the 20 hash values.
2. Divide and round up:
   $$\left\lceil\frac{40}{20}\right\rceil=2.$$
3. Therefore at least one bucket contains at least two keys.
4. To see that three is not guaranteed, place exactly two keys in every bucket.

The strongest forced conclusion is therefore **at least 2**, not at least 3.

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

> [!QUESTION]- Full question statement
> A committee of 3 students is selected from 10 students. How many
> committees are possible? Give a binomial-coefficient expression and explain
> why order does not matter.

A committee is an unordered set: choosing Ana, Bo, and Chen in a different
order does not create a new committee. Choose 3 of the 10 students:
$$
\binom{10}{3}=\frac{10!}{3!7!}
=\frac{10\cdot9\cdot8}{3\cdot2\cdot1}=120.
$$

### B.2 Distinct Offices

> [!QUESTION]- Full question statement
> A president and a vice president are selected from 10 students, with
> no student holding both offices. How many outcomes are possible? Give a
> permutation or product expression and explain why order matters.

The offices are different roles. Choose the president first (10 choices), then
the vice president from the remaining students (9 choices):
$$P(10,2)=10\cdot9=90.$$
Swapping the two people changes the assignment, so a combination would
undercount.

### B.3 Repeated Letters

> [!QUESTION]- Full question statement
> How many distinct strings can be made by reordering the letters of
> `BANANA`? Give the appropriate multinomial expression.

If all six letter copies were distinguishable, there would be $6!$
arrangements. Permuting the three A copies does not change a word, so divide by
$3!$; likewise divide by $2!$ for the two N copies:
$$\frac{6!}{3!2!}=\frac{720}{12}=60.$$
The single B contributes a factor $1!$, which has no effect.

### B.4 Fixed-Weight Bit Strings

> [!QUESTION]- Full question statement
> How many bit strings of length 8 contain exactly three $1$s? Give a
> binomial-coefficient expression and identify what is being selected.

An eight-bit string with exactly three $1$s is determined by the set of three
positions receiving $1$. The other five positions are then forced to be $0$:
$$\binom{8}{3}=\frac{8\cdot7\cdot6}{3\cdot2\cdot1}=56.$$

### B.5 Binomial Coefficient

> [!QUESTION]- Full question statement
> Find the coefficient of $x^3$ in $(1+x)^8$. State the binomial-theorem
> term that determines your answer.

The binomial theorem gives
$$(1+x)^8=\sum_{k=0}^8\binom{8}{k}x^k.$$
The $x^3$ term occurs when exactly three of the eight factors contribute their
$x$ term and the remaining five contribute $1$. There are therefore
$$\binom{8}{3}=56$$
such choices, so 56 is the coefficient of $x^3$.

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

> [!QUESTION]- Full question statement
> How many 5-card hands from a standard 52-card deck contain exactly
> two hearts? Give an unsimplified product of binomial coefficients.

1. “Exactly two hearts” forces the hand to contain two of the 13 hearts.
2. The remaining three cards must all come from the 39 non-hearts.
3. A hand is unordered, so use combinations in both categories.
4. The two selections are made from disjoint card pools, so multiply:
   $$\binom{13}{2}\binom{39}{3}.$$

Every qualifying hand has one unique two-heart/three-non-heart decomposition.

### C.2 Complement Counting

> [!QUESTION]- Full question statement
> How many bit strings of length 8 contain at least two $1$s? Use a
> complement and show the subtracted cases.

1. There are $2^8$ total eight-bit strings.
2. “At least two $1$s” fails only for zero $1$s or exactly one $1$.
3. There are $\binom80=1$ strings of the first type and $\binom81=8$ of the second.
4. These forbidden cases are disjoint, so subtract both:
   $$2^8-\binom80-\binom81=256-1-8=247.$$

### C.3 Mixed Committees

> [!QUESTION]- Full question statement
> A group of 5 students is selected from disjoint pools of 12
> computer-science majors and 8 mathematics majors. How many groups contain exactly 3 computer-science
> majors? Give an unsimplified product of binomial coefficients.

**Model check:** the question specifies disjoint groups of students. If dual majors were allowed, their
overlap would need to be specified before the count could be determined.

Thus, “exactly three computer-science majors” in a five-person committee forces the
other two members to be mathematics majors. Choose the two unordered category
subsets independently and combine them:
$$
\underbrace{\binom{12}{3}}_{\text{three CS majors}}
\underbrace{\binom{8}{2}}_{\text{two mathematics majors}}.
$$
No committee is duplicated because its two category subsets are uniquely
determined.

### C.4 Injective Functions

> [!QUESTION]- Full question statement
> Let $|A|=5$ and $|B|=8$. How many injective functions $f:A\to B$
> exist? Give a permutation or product expression and explain the restriction.

Order the five labeled domain elements. The first may map to any of 8 images;
injectivity leaves 7 for the second, then 6, 5, and 4:
$$P(8,5)=8\cdot7\cdot6\cdot5\cdot4=6720.$$
Do not divide by $5!$: the domain labels distinguish which input receives
which image.

### C.5 Codes with a Required First Type

> [!QUESTION]- Full question statement
> A six-character code uses uppercase letters without repetition and
> must begin with a vowel. How many codes are possible? Treat
> $A,E,I,O,U$ as the five vowels and give an unsimplified product.

1. Enforce the first-position restriction immediately: 5 vowels can begin the code.
2. The selected vowel is now unavailable because repetition is forbidden.
3. Fill the remaining five ordered positions from the other 25 letters, giving $25,24,23,22,21$ choices.
4. Multiply the successive choices:
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

> [!QUESTION]- Full question statement
> A fair coin is tossed independently of a fair six-sided die roll. Find the
> probability that the coin is heads or the die is even (or both). Show the
> favorable-outcome count or an equivalent probability calculation.

**Model check:** the question states that the coin toss and die roll are independent. Fairness
alone specifies their separate probabilities, not their joint distribution.
Under this independent model, the sample space has
$2\cdot6=12$ equally likely coin–die pairs. Count the
union without double counting:

- 6 outcomes have heads;
- 6 outcomes have an even die;
- 3 outcomes have both heads and an even die.

Thus
$$P(H\cup\text{even})=\frac{6+6-3}{12}=\frac9{12}=\frac34.$$
Equivalently, count the 6 heads outcomes plus the 3 *tails-and-even* outcomes.

### D.2 Probability Identities

> [!QUESTION]- Full question statement
> Suppose $P(A)=0.55$, $P(B)=0.40$, and $P(A\cap B)=0.25$. Find
> $P(A\cup B)$ and $P(A^c\cap B)$, showing the probability identities used.

For the union, add the two event probabilities and remove the overlap counted
twice:
$$P(A\cup B)=0.55+0.40-0.25=0.70.$$

Next partition $B$ into disjoint pieces:
$$B=(A\cap B)\mathbin{\dot\cup}(A^c\cap B).$$
Therefore
$$P(A^c\cap B)=P(B)-P(A\cap B)=0.40-0.25=0.15.$$

### D.3 Bit-String Probability

> [!QUESTION]- Full question statement
> A uniformly chosen 8-bit string is selected. Find the probability
> that it contains exactly three $1$s. Give an exact fraction.

All $2^8$ eight-bit strings are equally likely. A favorable string is
determined by choosing the three positions containing $1$s, so there are
$\binom83$ favorable outcomes. Hence
$$P(\text{exactly three 1s})=\frac{\binom83}{2^8}
=\frac{56}{256}=\frac7{32}.$$
The numerator and denominator count outcomes in the same sample space.

### D.4 Without Replacement

> [!QUESTION]- Full question statement
> A bag contains 4 red and 6 blue tokens. Two tokens are drawn without
> replacement. Find the probability that the first is red and the second is
> blue. Show the conditional product.

On the first draw, 4 of 10 tokens are red. Given that a red token was removed,
9 tokens remain and all 6 blue tokens remain. Use the conditional product rule:
$$
P(R_1\cap B_2)=P(R_1)P(B_2\mid R_1)
=\frac4{10}\cdot\frac6{9}=\frac{24}{90}=\frac4{15}.
$$
The changed denominator $9$ is the essential without-replacement step.

### D.5 Conditional Probabilities

> [!QUESTION]- Full question statement
> In a class, 24 students use Python, 18 use Java, and 10 use both.
> One student is chosen uniformly. Find
> $P(\text{Python}\mid\text{Java})$ and
> $P(\text{Java}\mid\text{Python})$.

The 10 students using both languages form the intersection in both
calculations. The event after the vertical bar determines the denominator:
$$P(\text{Python}\mid\text{Java})=\frac{10}{18}=\frac59,\qquad
P(\text{Java}\mid\text{Python})=\frac{10}{24}=\frac5{12}.$$
The two fractions differ because the conditioning groups have different sizes.

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

> [!QUESTION]- Full question statement
> Events $A$ and $B$ satisfy $P(A)=0.6$, $P(B)=0.5$, and
> $P(A\cap B)=0.3$. Determine whether $A$ and $B$ are independent, showing
> the numerical test, and then find $P(A\mid B)$.

1. Compute the product of the marginal probabilities:
   $$P(A)P(B)=0.6(0.5)=0.3.$$
2. Compare it with the given intersection: $P(A\cap B)=0.3$.
3. The values are equal, so the events satisfy the definition of independence.
4. As a check,
   $$P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{0.3}{0.5}=0.6=P(A).$$

### E.2 Screening and Base Rates

> [!QUESTION]- Full question statement
> A condition occurs in $1\%$ of a population. A test is positive for
> $95\%$ of people who have the condition and for $8\%$ of people who do not.
> Find $P(\text{positive})$ and then
> $P(\text{condition}\mid\text{positive})$. Give a one-sentence base-rate
> interpretation.

Let $C$ be the condition and $+$ a positive result.

1. True positives occur with probability
   $$P(C\cap +)=P(C)P(+\mid C)=0.01(0.95)=0.0095.$$
2. False positives occur with probability
   $$P(C^c\cap +)=0.99(0.08)=0.0792.$$
3. Add these disjoint routes to a positive result:
   $$P(+)=0.0095+0.0792=0.0887.$$
4. Bayes' rule selects the true-positive part of all positives:
   $$P(C\mid +)=\frac{0.0095}{0.0887}\approx0.1071.$$

The result is much smaller than $95\%$ because the low base rate leaves many
more unaffected people available to produce false positives.

### E.3 Factory Bayes Model

> [!QUESTION]- Full question statement
> Factory A supplies $40\%$ of a store's batteries and $3\%$ of its
> batteries are defective. Factory B supplies the rest and $1\%$ of its
> batteries are defective. A randomly selected battery is defective. Find the
> probability that it came from Factory A. Show total probability and Bayes'
> rule.

Let $D$ mean defective. A defective item can arrive through two disjoint routes:
$$P(A\cap D)=0.40(0.03)=0.012,$$
$$P(B\cap D)=0.60(0.01)=0.006.$$
Therefore the overall defective probability is
$$P(D)=0.012+0.006=0.018.$$
Among defective items, the fraction from A is
$$P(A\mid D)=\frac{P(A\cap D)}{P(D)}
=\frac{0.012}{0.018}=\frac23.$$

### E.4 Expected Net Value

> [!QUESTION]- Full question statement
> A game uses a fair six-sided die. It pays \$10 for a 6, \$2 for a 4
> or 5, and \$0 otherwise. A play costs \$2. Find the expected *net*
> value of one play and interpret the sign.

There are three payout cases: $10$ with probability $1/6$, $2$ with
probability $2/6$, and $0$ with probability $3/6$. Thus
$$E[\text{payout}]
=10\left(\frac16\right)+2\left(\frac26\right)+0\left(\frac36\right)
=\frac{14}{6}=\frac73.$$
The $2$ cost is paid every time, so subtract it from the expectation:
$$E[\text{net}]=\frac73-2=\frac13\text{ dollar}.$$
Equivalently, average the net outcomes $8,0,-2$ with probabilities
$1/6,2/6,3/6$. The positive sign means a long-run average gain of about 33
cents per play, not a guaranteed profit on any one play.

### E.5 Aggregation Reversal

> [!QUESTION]- Full question statement
> The table gives successes/participants for two treatments.
>
> $$
>
> \begin{array}{c|cc}
> &\text{Treatment A}&\text{Treatment B}\\\hline
> \text{Group 1}&30/100&400/1000\\
> \text{Group 2}&800/1000&90/100
> \end{array}
>
> $$
>
> Identify the better treatment within each group and overall. Then explain in
> one sentence how the unequal treatment denominators produce the reversal.

Compute rates before comparing them.

- Group 1: A has $30/100=30\%$, while B has $400/1000=40\%$, so B is higher.
- Group 2: A has $800/1000=80\%$, while B has $90/100=90\%$, so B is again higher.

Overall,
$$P(\text{success}\mid A)=\frac{30+800}{100+1000}
=\frac{830}{1100}\approx75.5\%,$$
$$P(\text{success}\mid B)=\frac{400+90}{1000+100}
=\frac{490}{1100}\approx44.5\%.$$
So A has the higher aggregate rate even though B has the higher rate within
each group. The reversal occurs because A was used mostly in the
higher-success group while B was used mostly in the lower-success group;
pooling changes the weights, not the within-group arithmetic.

> [!TIP]- More Resources
> [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)
