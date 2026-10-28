---
title: 2300 Sets Solutions
aliases: [2300 Sets Solutions, Sets Solutions]
linter-yaml-title-alias: 2300 Sets Solutions
date created: Monday, March 9th 2026, 2:29:50 pm
date modified: Wednesday, October 28th 2026
publish: true
permalink: core-assessment-solutions/2300-sets-solutions
---
# 2300 Sets Solutions

> [!IMPORTANT] How the Sets Core works
> These solutions accompany the public Sets Core practice source; they do not reveal a live form. A supervised attempt lasts 20 minutes and contains five problems, one from each section A–E. Each labeled problem is one scoring unit, including all required parts. Four fully correct problems earn **Meets**; five earn **Exceeds**. Every retake uses a complete new five-problem form.

> [!IMPORTANT] Full-credit and grader guidance
> Equivalent roster order, notation, witnesses, counterexamples, and elementwise
> proofs are acceptable. The **decisive check** in each section identifies the
> central mathematical distinction, but full credit still requires every requested
> subpart of the selected problem.

[[attachments/COMP 2300 Sets Core Practice.pdf|Download the four-page Sets Core practice source (PDF)]]

Use this packet for representative practice; the numbered solutions below follow the same A–E section labels.

## A. Set Language and Finite Constructions

> [!TIP]- Step-by-step method for Section A
> 1. Enforce the stated domain, then list each distinct value once and in a convenient order.
> 2. Check the *type* of each object before deciding membership: an integer, an ordered pair, and a set are different kinds of objects.
> 3. For $T\subseteq S$, check every element of $T$. For $T\in S$, check whether the set $T$ itself appears as one element of $S$.
> 4. Build a power set by subset size: empty set, singletons, larger subsets, then the whole set. Build a Cartesian product by pairing every first-coordinate choice with every second-coordinate choice.
> 5. Verify the count: $|\mathcal P(T)|=2^{|T|}$ and $|T\times S|=|T||S|$.

> [!TIP]- Relevant Materials
> - [Sets companion — definitions and worked examples (4-page PDF)](https://raw.githubusercontent.com/alexanderlewisstevens/Core_Standards_HW_Templates/main/2300/cheat_sheets/companion_pdfs/sets_core_companion.pdf)
> - Rosen: [[Books/book_sections_md/2.1_Sets|§2.1 — Sets]]
> - [2.1a Sets (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1aSetsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1aSets.10.21.mp4)
> - [2.1b Subsets and Set Equality (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1bSubsetsAndSetEqualityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1bSubsetsAndSetEquality.3.28.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the complete finite set, both membership/subset
> decisions with enough explanation to distinguish $\in$ from $\subseteq$, and
> every requested power-set or Cartesian-product element. Order is irrelevant.
> **Decisive check:** verify element-versus-set type before checking the lists.

### A.1


> [!QUESTION]- Full question statement
> For each problem, complete every part.
>
> Let $S=\{x\in\mathbb Z:-2\le x<3\}$ and $T=\{-2,2\}$.
> - **(a)** Write $S$ in roster notation.
> - **(b)** Decide whether $T\subseteq S$ and whether $T\in S$.
> - **(c)** List every element of $\mathcal P(T)$.

> [!Note] Solution
> (a) $S=\{-2,-1,0,1,2\}$.
>
> (b) $T\subseteq S$ is true because both $-2$ and $2$ belong to $S$. The statement $T\in S$ is false: the elements of $S$ are integers, not the set $\{-2,2\}$.
>
> (c) $\mathcal P(T)=\{\varnothing,\{-2\},\{2\},\{-2,2\}\}$.

### A.2


> [!QUESTION]- Full question statement
> For each problem, complete every part.
>
> Let $S=\{x\in\mathbb Z:-4\le x\le4\text{ and }x\text{ is even}\}$ and
> $T=\{-2,4\}$.
> - **(a)** Write $S$ in roster notation.
> - **(b)** Decide whether $T\subseteq S$ and whether $-2\in T$.
> - **(c)** List $T\times\{0,1\}$.

> [!Note] Solution
> (a) $S=\{-4,-2,0,2,4\}$.
>
> (b) Both statements are true: every element of $T$ lies in $S$, and $-2$ is an element of $T$.
>
> (c) $T\times\{0,1\}=\{(-2,0),(-2,1),(4,0),(4,1)\}$.

### A.3


> [!QUESTION]- Full question statement
> For each problem, complete every part.
>
> Let $S=\{x\in\mathbb Z^+:x\mid12\}$ and $T=\{2,3\}$.
> - **(a)** Write $S$ in roster notation.
> - **(b)** Decide whether $T\subseteq S$ and whether $T\in\mathcal P(S)$.
> - **(c)** List every element of $\mathcal P(T)$.

> [!Note] Solution
> (a) $S=\{1,2,3,4,6,12\}$.
>
> (b) $T\subseteq S$ is true. Consequently $T\in\mathcal P(S)$ is also true, because the elements of a power set are precisely the subsets of the original set.
>
> (c) $\mathcal P(T)=\{\varnothing,\{2\},\{3\},\{2,3\}\}$.

### A.4


> [!QUESTION]- Full question statement
> For each problem, complete every part.
>
> Let $S=\{n^2:n\in\mathbb Z,-2\le n\le2\}$ and $T=\{0,1\}$.
> - **(a)** Write $S$ in roster notation, without repetitions.
> - **(b)** Decide whether $T\subset S$ and whether $2\in S$.
> - **(c)** List $T\times S$.

> [!Note] Solution
> (a) $S=\{0,1,4\}$. Repeated outputs such as $(-2)^2=2^2$ are listed only once in a set.
>
> (b) $T\subset S$ is true because $T\subseteq S$ and $4\in S\setminus T$. The statement $2\in S$ is false.
>
> (c) $T\times S=\{(0,0),(0,1),(0,4),(1,0),(1,1),(1,4)\}$.

### A.5


> [!QUESTION]- Full question statement
> For each problem, complete every part.
>
> Let $S=\{x\in\mathbb Z:|x|\le2\}$ and $T=\{-1,1\}$.
> - **(a)** Write $S$ in roster notation.
> - **(b)** Decide whether $T\subseteq S$ and whether $\{0\}\in S$.
> - **(c)** List every element of $\mathcal P(T)$.

> [!Note] Solution
> (a) $S=\{-2,-1,0,1,2\}$.
>
> (b) $T\subseteq S$ is true. The statement $\{0\}\in S$ is false: $0$ is an element of $S$, but the singleton set $\{0\}$ is not.
>
> (c) $\mathcal P(T)=\{\varnothing,\{-1\},\{1\},\{-1,1\}\}$.

## B. Set Operations and Venn Regions

> [!TIP]- Step-by-step method for Section B
> 1. Replace set membership with a proposition: for example, $P$ means $x\in A$.
> 2. Eliminate $\to$ and $\leftrightarrow$ using propositional equivalences.
> 3. Translate $\neg,\land,\lor$ into complement, intersection, and union.
> 4. Simplify only after the logical structure is correct.
> 5. Check the answer by testing representative points from the Venn regions, especially the true-hypothesis/false-conclusion region of an implication.

> [!TIP]- Relevant Materials
> - Rosen: [[Books/book_sections_md/2.2_Set_Operations|§2.2 — Set Operations]]
> - [2.2a Set Operations (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2aSetOperationsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2aSetOperations.7.07.mp4)
> - [2.2b More Set Operations (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2bMoreSetOperationsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2bMoreSetOperations.4.14.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the exact shaded region and an equivalent expression
> using the permitted set operations. Any equivalent expression earns full credit.
> **Decisive check:** test one point in each relevant Venn region, especially where
> an implication is false (hypothesis in, conclusion out) or a biconditional has
> matching truth values.

### B.1


> [!QUESTION]- Full question statement
> For each formula, shade exactly the set of points $x\in\mathfrak U$ for which
> the formula is true. Then write the shaded region using only union,
> intersection, complement, and set difference.
>
> $(x\in A\setminus B)\lor(x\in C)$

> [!Note] Solution
> First, $x\in A\setminus B$ means $x\in A$ **and** $x\notin B$, so it corresponds to $A\cap\overline B$. The outer “or $x\in C$” becomes a union with $C$. Therefore shade
> $$
> (A\setminus B)\cup C=(A\cap\overline B)\cup C.
> $$
> As a check, every point of $C$ is included, and outside $C$ only the part of $A$ lying outside $B$ is included.

### B.2


> [!QUESTION]- Full question statement
> For each formula, shade exactly the set of points $x\in\mathfrak U$ for which
> the formula is true. Then write the shaded region using only union,
> intersection, complement, and set difference.
>
> $(x\in \overline A)\lor(x\in B\cup C)$

> [!Note] Solution
> Translate the three alternatives one at a time: $x\notin A$ gives $\overline A$, $x\in B$ gives $B$, and $x\in C$ gives $C$. Because they are joined by “or,” take their union:
> $$
> \overline A\cup B\cup C.
> $$
> The only points excluded are those simultaneously inside $A$, outside $B$, and outside $C$.

### B.3


> [!QUESTION]- Full question statement
> For each formula, shade exactly the set of points $x\in\mathfrak U$ for which
> the formula is true. Then write the shaded region using only union,
> intersection, complement, and set difference.
>
> $(x\in A\cup B)\to(x\in C)$

> [!Note] Solution
> Let $P$ mean $x\in A\cup B$ and $Q$ mean $x\in C$. Eliminate the implication:
> $$
> P\to Q\equiv\neg P\lor Q.
> $$
> Substituting the set statements gives $\neg(x\in A\cup B)\lor(x\in C)$, so the required region is
> $$
> \overline{A\cup B}\cup C.
> $$
> This includes every point except one where the hypothesis is true (inside $A\cup B$) and the conclusion is false (outside $C$).

### B.4


> [!QUESTION]- Full question statement
> For each formula, shade exactly the set of points $x\in\mathfrak U$ for which
> the formula is true. Then write the shaded region using only union,
> intersection, complement, and set difference.
>
> $((x\in A)\to(x\in B))\land(x\in C)$

> [!Note] Solution
> First rewrite the implication:
> $$
> x\in A\to x\in B
> \equiv x\notin A\text{ or }x\in B
> \equiv x\in\overline A\cup B.
> $$
> The additional requirement $x\in C$ is joined by “and,” so intersect with $C$. The final region is
> $$
> (\overline A\cup B)\cap C.
> $$

### B.5


> [!QUESTION]- Full question statement
> For each formula, shade exactly the set of points $x\in\mathfrak U$ for which
> the formula is true. Then write the shaded region using only union,
> intersection, complement, and set difference.
>
> $(x\in A)\leftrightarrow(x\in B\setminus C)$

> [!Note] Solution
> Let $P$ mean $x\in A$ and $Q$ mean $x\in B\setminus C$. A biconditional is true when both sides are true or both are false:
> $$
> P\leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q).
> $$
> Now $B\setminus C=B\cap\overline C$, and by De Morgan’s law,
> $\overline{B\cap\overline C}=\overline B\cup C$. Substituting yields
> $$
> (A\cap B\cap\overline C)\cup
> \bigl(\overline A\cap(\overline B\cup C)\bigr).
> $$

## C. Relations as Subsets of Cartesian Products

> [!TIP]- Step-by-step method for Section C
> 1. Convert every plotted point into an ordered pair $(x,y)$; scan one input-column at a time so none are missed.
> 2. Translate a quantified statement into a visual test: $\forall x$ checks every column, $\forall y$ checks every row, $\exists$ needs one witness, and $\exists!$ needs exactly one.
> 3. For a false universal statement, name a specific empty or overfilled row/column. For a true existential statement, name the witness.
> 4. Test “function” before testing injective or surjective: every declared input needs exactly one output.
> 5. Only if it is a function, check whether outputs collide (injectivity) and whether every codomain value is hit (surjectivity).

> [!TIP]- Relevant Materials
> - Rosen: [[Books/book_sections_md/2.1_Sets|§2.1 — Sets]] | [[Books/book_sections_md/2.3_Functions|§2.3 — Functions]]
> - [1.4a Quantifiers (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4aQuantifiersHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch1/2300.1.4aQuantifiers.4.07.mp4)
> - [2.3a Functions (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3aFunctionsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3aFunctions.12.44.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** every ordered pair, both quantified truth values
> with a witness or counterexample, and the function verdict/classification.
> **Decisive check:** a function needs exactly one output for every input; one input
> with zero or multiple outputs settles the negative verdict.

### C.1


> [!QUESTION]- Full question statement
> For each plotted relation $R\subseteq X\times Y$, where
> $X=Y=\{1,2,3\}$:
> - **(a)** list $R$ as a set of ordered pairs;
> - **(b)** decide whether each stated quantified proposition is true or false; and
> - **(c)** decide whether $R$ is a function from $X$ to $Y$. If it is, classify it
> as injective, surjective, both, or neither. If it is not, identify an input
> with either no output or more than one output.
>
> Evaluate $\forall x\,\exists!y\,((x,y)\in R)$ and
> $\forall y\,\exists!x\,((x,y)\in R)$.
> ![[assets/set_plot1.jpg]]

> [!Note] Solution
> **(a) List the relation.** Reading the plot one input-column at a time gives
> one point in each column:
> $$R=\{(1,1),(2,2),(3,3)\}.$$
>
> **(b) Evaluate the quantified claims.** For $x=1,2,3$, the unique related
> outputs are respectively $1,2,3$. Hence
> $\forall x\,\exists!y\,((x,y)\in R)$ is true. Looking by rows instead, each
> $y=1,2,3$ occurs with exactly one input, so
> $\forall y\,\exists!x\,((x,y)\in R)$ is also true.
>
> **(c) Classify the relation.** It is a function because every input has
> exactly one output. It is injective because no two inputs share an output,
> and surjective because every element of $Y=\{1,2,3\}$ occurs as an output.
> Therefore it is **bijective**.
>
> **Decisive check:** the plot contains exactly one point in every column and
> exactly one point in every row.

### C.2


> [!QUESTION]- Full question statement
> For each plotted relation $R\subseteq X\times Y$, where
> $X=Y=\{1,2,3\}$:
> - **(a)** list $R$ as a set of ordered pairs;
> - **(b)** decide whether each stated quantified proposition is true or false; and
> - **(c)** decide whether $R$ is a function from $X$ to $Y$. If it is, classify it
> as injective, surjective, both, or neither. If it is not, identify an input
> with either no output or more than one output.
>
> Evaluate $\forall x\,\exists y\,((x,y)\in R)$ and
> $\exists x\,\forall y\,((x,y)\in R)$.
> ![[assets/set_plot2.jpg]]

> [!Note] Solution
> **(a) List the relation.** The plotted points are
> $$R=\{(1,1),(2,1),(2,2),(2,3),(3,2)\}.$$
>
> **(b) Evaluate the quantified claims.** Every input has at least one output:
> $x=1$ reaches $1$, $x=2$ reaches $1,2,3$, and $x=3$ reaches $2$.
> Therefore $\forall x\,\exists y\,((x,y)\in R)$ is true. The second claim is
> also true because $x=2$ is a witness for
> $\exists x\,\forall y\,((x,y)\in R)$: all three pairs
> $(2,1),(2,2),(2,3)$ occur.
>
> **(c) Classify the relation.** It is **not a function** from $X$ to $Y$.
> A function may assign only one output to an input, but input $2$ has the
> three outputs $1,2,3$. No injective/surjective classification is needed once
> the function test fails.
>
> **Decisive check:** the three points in column $x=2$ violate uniqueness.

### C.3


> [!QUESTION]- Full question statement
> For each plotted relation $R\subseteq X\times Y$, where
> $X=Y=\{1,2,3\}$:
> - **(a)** list $R$ as a set of ordered pairs;
> - **(b)** decide whether each stated quantified proposition is true or false; and
> - **(c)** decide whether $R$ is a function from $X$ to $Y$. If it is, classify it
> as injective, surjective, both, or neither. If it is not, identify an input
> with either no output or more than one output.
>
> Evaluate $\forall y\,\exists x\,((x,y)\in R)$ and
> $\exists y\,\forall x\,((x,y)\in R)$.
> ![[assets/set_plot3.jpg]]

> [!Note] Solution
> **(a) List the relation.** Reading the four plotted points gives
> $$R=\{(1,1),(1,2),(2,1),(3,1)\}.$$
>
> **(b) Evaluate the quantified claims.** The universal claim over $y$ is
> false: $y=3$ is a counterexample because no pair $(x,3)$ belongs to $R$.
> The existential claim is true: choose $y=1$. Then
> $(1,1),(2,1),(3,1)\in R$, so this one $y$ is related to every input.
>
> **(c) Classify the relation.** It is **not a function** because input $1$
> is assigned both outputs $1$ and $2$. The fact that inputs $2$ and $3$ each
> have one output cannot repair that collision.
>
> **Decisive check:** $y=3$ refutes the first quantified statement, while
> $y=1$ witnesses the second.

### C.4


> [!QUESTION]- Full question statement
> For each plotted relation $R\subseteq X\times Y$, where
> $X=Y=\{1,2,3\}$:
> - **(a)** list $R$ as a set of ordered pairs;
> - **(b)** decide whether each stated quantified proposition is true or false; and
> - **(c)** decide whether $R$ is a function from $X$ to $Y$. If it is, classify it
> as injective, surjective, both, or neither. If it is not, identify an input
> with either no output or more than one output.
>
> Evaluate $\forall x\,\exists!y\,((x,y)\in R)$ and
> $\exists x\,\forall y\,((x,y)\in R)$.
> ![[assets/set_plot4.jpg]]

> [!Note] Solution
> **(a) List the relation.** The plot contains all pairs in $X\times Y$
> except $(3,3)$:
> $$R=\{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2)\}.$$
>
> **(b) Evaluate the quantified claims.** The unique-output claim is false.
> For example, $x=1$ is related to $y=1,2,3$, so there is not a unique $y$.
> The second claim is true: either $x=1$ or $x=2$ is a witness, because each
> of those inputs is related to every $y\in\{1,2,3\}$.
>
> **(c) Classify the relation.** It is **not a function** because inputs $1$
> and $2$ each have three outputs (and input $3$ has two). One counterexample
> input, such as $x=1$, is sufficient.
>
> **Decisive check:** distinguish “there exists an input related to every
> output,” which is true, from “every input has a unique output,” which is false.

### C.5


> [!QUESTION]- Full question statement
> For each plotted relation $R\subseteq X\times Y$, where
> $X=Y=\{1,2,3\}$:
> - **(a)** list $R$ as a set of ordered pairs;
> - **(b)** decide whether each stated quantified proposition is true or false; and
> - **(c)** decide whether $R$ is a function from $X$ to $Y$. If it is, classify it
> as injective, surjective, both, or neither. If it is not, identify an input
> with either no output or more than one output.
>
> Evaluate $\forall y\,\exists!x\,((x,y)\in R)$ and
> $\exists y\,\forall x\,((x,y)\in R)$.
> ![[assets/set_plot5.jpg]]

> [!Note] Solution
> **(a) List the relation.** The five plotted points give
> $$R=\{(1,1),(1,2),(2,2),(2,3),(3,2)\}.$$
>
> **(b) Evaluate the quantified claims.** The first statement is false.
> Although $y=1$ and $y=3$ each have one related input, $y=2$ has three:
> $x=1,2,3$. Thus uniqueness fails. The second statement is true, also with
> $y=2$ as the witness, because $(1,2),(2,2),(3,2)$ all belong to $R$.
>
> **(c) Classify the relation.** It is **not a function**. Input $1$ has
> outputs $1$ and $2$, while input $2$ has outputs $2$ and $3$; either input
> alone disproves the exactly-one-output requirement.
>
> **Decisive check:** the same row $y=2$ makes the universal-uniqueness claim
> false but supplies the witness for the existential-universal claim.

## D. Functions, Images, and Preimages

> [!TIP]- Step-by-step method for Section D
> 1. Read the declared domain and codomain before using the formula.
> 2. For an image, evaluate the function on each listed input and remove repeated outputs.
> 3. For a preimage, solve or test $f(x)\in P$ and list the allowed inputs—not the output values.
> 4. To disprove injectivity, exhibit two distinct inputs with the same output; to prove it, start from $f(m)=f(n)$ and derive $m=n$.
> 5. To disprove surjectivity, give one codomain value with no preimage; to prove it, start with arbitrary $y$ in the codomain and construct an allowed $x$ with $f(x)=y$.

> [!TIP]- Relevant Materials
> - Rosen: [[Books/book_sections_md/2.3_Functions|§2.3 — Functions]]
> - [2.3a Functions (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3aFunctionsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3aFunctions.12.44.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** both requested image/preimage sets and a justified
> injective/surjective classification. Algebraic proofs or concrete witnesses are
> both acceptable when appropriate. **Decisive check:** use the declared domain
> and codomain; injectivity looks for output collisions, while surjectivity asks
> whether every codomain element has a preimage.

### D.1


> [!QUESTION]- Full question statement
> Let $A=\{1,2,3,4\}$ and $B=\{a,b,c\}$. Define $f:A\to B$ by
> $f(1)=a$, $f(2)=b$, $f(3)=b$, and $f(4)=c$.
> - **(a)** Find $f(\{1,3,4\})$ and $f^{-1}(\{a,b\})$.
> - **(b)** Classify $f$ as injective, surjective, both, or neither. Justify your
> answer.

> [!Note] Solution
> **(a) Image and preimage.** Evaluate the listed inputs:
> $$f(1)=a,\qquad f(3)=b,\qquad f(4)=c.$$
> Removing no values is necessary because the outputs are distinct, so
> $f(\{1,3,4\})=\{a,b,c\}$. For the preimage, inspect all inputs in $A$ and
> keep those whose outputs lie in $\{a,b\}$: inputs $1,2,3$ qualify and input
> $4$ does not. Hence $f^{-1}(\{a,b\})=\{1,2,3\}$.
>
> **(b) Classification.** The function is surjective because $a,b,c$ all
> appear as outputs. It is not injective because the distinct inputs $2$ and
> $3$ collide: $f(2)=f(3)=b$. Therefore $f$ is **surjective but not
> injective**.
>
> **Decisive check:** a preimage is a set of inputs, so its members here are
> $1,2,3$, not the output labels $a,b$.

### D.2


> [!QUESTION]- Full question statement
> Let $g:\mathbb Z\to\mathbb Z$ be $g(n)=n+5$.
> - **(a)** Find $g(\{-1,0,2\})$ and $g^{-1}(\{4,7\})$.
> - **(b)** Classify $g$ as injective, surjective, both, or neither. Justify both
> properties.

> [!Note] Solution
> **(a) Image and preimage.** Substitute the three inputs:
> $$g(-1)=4,\qquad g(0)=5,\qquad g(2)=7,$$
> so $g(\{-1,0,2\})=\{4,5,7\}$. To find the preimage, solve
> $n+5=4$ or $n+5=7$. The solutions are $n=-1$ and $n=2$, so
> $g^{-1}(\{4,7\})=\{-1,2\}$.
>
> **(b) Classification.** If $g(m)=g(n)$, then $m+5=n+5$, and subtracting
> $5$ gives $m=n$; hence $g$ is injective. For an arbitrary codomain value
> $y\in\mathbb Z$, choose $n=y-5$. This is an allowed integer input and
> $g(n)=(y-5)+5=y$, so $g$ is surjective. Therefore $g$ is **bijective**.
>
> **Decisive check:** the constructed preimage $y-5$ remains in the declared
> domain $\mathbb Z$ for every codomain integer $y$.

### D.3


> [!QUESTION]- Full question statement
> Let $h:\mathbb Z\to\mathbb Z$ be $h(n)=n^2$.
> - **(a)** Find $h(\{-2,-1,0,2\})$ and $h^{-1}(\{0,1,4\})$.
> - **(b)** Classify $h$ as injective, surjective, both, or neither. Give concrete
> witnesses for any failed property.

> [!Note] Solution
> **(a) Image and preimage.** Squaring the listed inputs gives
> $4,1,0,4$. Sets do not repeat values, so
> $h(\{-2,-1,0,2\})=\{0,1,4\}$. For the preimage, solve
> $n^2\in\{0,1,4\}$. The integer solutions are
> $n=0$, $n=\pm1$, and $n=\pm2$, so
> $$h^{-1}(\{0,1,4\})=\{-2,-1,0,1,2\}.$$
>
> **(b) Classification.** The function is not injective: the distinct inputs
> $1$ and $-1$ have the same output $1$. It is not surjective onto
> $\mathbb Z$: every square is nonnegative, so the codomain value $-1$, for
> example, has no preimage. Therefore $h$ is **neither injective nor
> surjective**.
>
> **Decisive check:** one collision disproves injectivity and one missed
> codomain value disproves surjectivity.

### D.4


> [!QUESTION]- Full question statement
> Let $k:\mathbb Z\to\mathbb Z$ be $k(n)=2n$.
> - **(a)** Find $k(\{-1,0,1\})$ and $k^{-1}(\{-2,0,4\})$.
> - **(b)** Classify $k$ as injective, surjective, both, or neither. Justify your
> answer.

> [!Note] Solution
> **(a) Image and preimage.** Direct substitution gives
> $k(-1)=-2$, $k(0)=0$, and $k(1)=2$, so
> $k(\{-1,0,1\})=\{-2,0,2\}$. For the preimage, solve
> $2n=-2$, $2n=0$, or $2n=4$; this gives $n=-1,0,2$. Thus
> $k^{-1}(\{-2,0,4\})=\{-1,0,2\}$.
>
> **(b) Classification.** If $k(m)=k(n)$, then $2m=2n$, so division by the
> nonzero number $2$ gives $m=n$; therefore $k$ is injective. It is not
> surjective onto $\mathbb Z$ because every output is even. For instance, no
> integer input satisfies $2n=1$. Hence $k$ is **injective but not
> surjective**.
>
> **Decisive check:** the output formula covers all even integers, but the
> declared codomain also contains odd integers.

### D.5


> [!QUESTION]- Full question statement
> Let $q:\mathbb N_0\to\{m^2:m\in\mathbb N_0\}$ be $q(n)=n^2$, where
> $\mathbb N_0=\{0,1,2,\ldots\}$.
> - **(a)** Find $q(\{0,2,3\})$ and $q^{-1}(\{1,16\})$.
> - **(b)** Classify $q$ as injective, surjective, both, or neither. Explain how
> the declared domain and codomain affect the answer.

> [!Note] Solution
> **(a) Image and preimage.** Evaluate on the listed inputs:
> $q(0)=0$, $q(2)=4$, and $q(3)=9$, so
> $q(\{0,2,3\})=\{0,4,9\}$. For the preimage, solve $n^2=1$ or $n^2=16$
> within the restricted domain $\mathbb N_0$. The allowed solutions are
> $n=1$ and $n=4$; the negative roots are outside the domain. Thus
> $q^{-1}(\{1,16\})=\{1,4\}$.
>
> **(b) Classification.** Suppose $q(m)=q(n)$ for $m,n\in\mathbb N_0$.
> Then $m^2=n^2$, so $(m-n)(m+n)=0$. Nonnegativity rules out $m=-n$
> except when both are $0$, and in every case $m=n$; hence $q$ is injective.
> Every element $y$ of the declared codomain has the form $y=r^2$ for some
> $r\in\mathbb N_0$, and then $q(r)=y$; hence $q$ is surjective. Therefore
> $q$ is **bijective**.
>
> Restricting the domain removes the usual $r,-r$ collision, while restricting
> the codomain to perfect squares removes values with no square-root preimage.
> **Decisive check:** both the domain and codomain restrictions are essential.

## E. Prove or Refute a Set/Function Claim

> [!TIP]- Step-by-step method for Section E
> 1. Test a few small cases to decide whether the claim is likely true or false; examples guide the method but do not prove a universal claim.
> 2. For a true equality, choose an arbitrary element and chase membership through definitions using “if and only if.” This proves both inclusions at once.
> 3. For a false claim, choose the smallest finite sets and simplest function that make the two sides behave differently.
> 4. Compute both sides of a proposed counterexample explicitly.
> 5. Finish by stating why the membership chain proves equality or why the computed unequal sides refute the universal claim.

> [!TIP]- Relevant Materials
> - Rosen: [[Books/book_sections_md/2.2_Set_Operations|§2.2 — Set Operations]] | [[Books/book_sections_md/2.3_Functions|§2.3 — Functions]]
> - [2.2c Set Proofs (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2cSetProofsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.2cSetProofs.6.55.mp4)
> - [2.3c Function Proofs (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3cFunctionProofsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.3cFunctionProofs.6.10.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** a true/false verdict plus an arbitrary-element proof
> for a true claim or a fully computed finite counterexample for a false one.
> Different valid witnesses earn full credit. **Decisive check:** a proof must
> establish both set inclusions (an iff membership chain does this); a counterexample
> must satisfy every hypothesis while making the conclusion false.

### E.1


> [!QUESTION]- Full question statement
> For each problem, decide whether the claim is true for all sets and functions
> of the stated types. If it is true, prove it by following an arbitrary element.
> If it is false, give a specific finite counterexample and compute both sides.
>
> If $f:X\to Y$ and $U,V\subseteq X$, then
>
> $$
>
> f(U\cup V)=f(U)\cup f(V).
>
> $$

> [!Note] Solution
> The claim is true. For an arbitrary $y\in Y$,
> $$
> y\in f(U\cup V)
> \iff y=f(x)\text{ for some }x\in U\cup V
> \iff \bigl(y=f(x)\text{ for some }x\in U\bigr)
>       \text{ or }\bigl(y=f(x)\text{ for some }x\in V\bigr)
> \iff y\in f(U)\text{ or }y\in f(V)
> \iff y\in f(U)\cup f(V).
> $$
> The first equivalence is the definition of an image. The next uses the
> definition of union: a witness in $U\cup V$ belongs to at least one of $U,V$.
> Each implication is reversible, so the chain proves both inclusions. The two
> sets therefore have exactly the same elements; injectivity is not needed.

### E.2


> [!QUESTION]- Full question statement
> For each problem, decide whether the claim is true for all sets and functions
> of the stated types. If it is true, prove it by following an arbitrary element.
> If it is false, give a specific finite counterexample and compute both sides.
>
> If $f:X\to Y$ and $U,V\subseteq X$, then
>
> $$
>
> f(U\cap V)=f(U)\cap f(V).
>
> $$

> [!Note] Solution
> The claim is false. Let $X=\{1,2\}$, $Y=\{a\}$, define $f(1)=f(2)=a$, and take $U=\{1\}$ and $V=\{2\}$. Then $U\cap V=\varnothing$, so $f(U\cap V)=\varnothing$. But $f(U)=f(V)=\{a\}$, so $f(U)\cap f(V)=\{a\}$.
>
> **Why it fails:** a common output need not have a common input. The output
> $a$ comes from $1\in U$ and, separately, from $2\in V$; there is no input in
> both sets. The inclusion $f(U\cap V)\subseteq f(U)\cap f(V)$ always holds,
> but this example disproves the reverse inclusion. A full-credit counterexample
> needs only the specified function and these two unequal computed sets.

### E.3


> [!QUESTION]- Full question statement
> For each problem, decide whether the claim is true for all sets and functions
> of the stated types. If it is true, prove it by following an arbitrary element.
> If it is false, give a specific finite counterexample and compute both sides.
>
> If $f:X\to Y$ and $P,Q\subseteq Y$, then
>
> $$
>
> f^{-1}(P\cap Q)=f^{-1}(P)\cap f^{-1}(Q).
>
> $$

> [!Note] Solution
> The claim is true. For an arbitrary $x\in X$,
> $$
> x\in f^{-1}(P\cap Q)
> \iff f(x)\in P\cap Q
> \iff f(x)\in P\text{ and }f(x)\in Q
> \iff x\in f^{-1}(P)\text{ and }x\in f^{-1}(Q)
> \iff x\in f^{-1}(P)\cap f^{-1}(Q).
> $$
> The first and third equivalences use the definition of preimage; the others
> use intersection. All conditions concern the **same input $x$** and its
> single output $f(x)$, so no injectivity assumption is needed. Since every
> step is reversible, the two preimages are equal.

### E.4


> [!QUESTION]- Full question statement
> For each problem, decide whether the claim is true for all sets and functions
> of the stated types. If it is true, prove it by following an arbitrary element.
> If it is false, give a specific finite counterexample and compute both sides.
>
> For all sets $A,B,C$,
>
> $$
>
> (A\cup B)\times C=(A\times C)\cup(B\times C).
>
> $$

> [!Note] Solution
> The claim is true. For an arbitrary ordered pair $(x,y)$,
> $$
> (x,y)\in(A\cup B)\times C
> \iff (x\in A\text{ or }x\in B)\text{ and }y\in C
> \iff (x\in A\text{ and }y\in C)\text{ or }(x\in B\text{ and }y\in C)
> \iff (x,y)\in A\times C\text{ or }(x,y)\in B\times C.
> $$
> The middle step distributes “and” over “or.” The final condition is equivalent
> to $(x,y)\in(A\times C)\cup(B\times C)$. Both coordinates have been checked,
> and every implication is reversible, proving the equality rather than just
> one inclusion.

### E.5


> [!QUESTION]- Full question statement
> For each problem, decide whether the claim is true for all sets and functions
> of the stated types. If it is true, prove it by following an arbitrary element.
> If it is false, give a specific finite counterexample and compute both sides.
>
> For all sets $A,B,C$, if $A\cup B=A\cup C$, then $B=C$.

> [!Note] Solution
> The claim is false. Let $A=\{1\}$, $B=\varnothing$, and $C=\{1\}$. Then
> $A\cup B=\{1\}=A\cup C$, but $B\ne C$. Union with $A$ can hide a difference consisting only of elements already in $A$.

> [!TIP]- More Resources
> [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)
