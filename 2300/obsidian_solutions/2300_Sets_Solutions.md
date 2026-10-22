---
title: 2300 Sets Solutions
aliases: [2300 Sets Solutions, Sets Solutions]
linter-yaml-title-alias: 2300 Sets Solutions
date created: Monday, March 9th 2026, 2:29:50 pm
date modified: Wednesday, October 21st 2026
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

> [!TIP]- Relevant Materials
> - Rosen: [[Books/book_sections_md/2.1_Sets|§2.1 — Sets]]
> - [2.1a Sets (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1aSetsHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1aSets.10.21.mp4)
> - [2.1b Subsets and Set Equality (PDF)](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1bSubsetsAndSetEqualityHandout.pdf) | [Video](https://cs.du.edu/~ftl/2300/resources/Ch2/2300.2.1bSubsetsAndSetEquality.3.28.mp4)

> [!CHECK]- Full-credit minimum and decisive check
> **Minimum complete answer:** the complete finite set, both membership/subset
> decisions with enough explanation to distinguish $\in$ from $\subseteq$, and
> every requested power-set or Cartesian-product element. Order is irrelevant.
> **Decisive check:** verify element-versus-set type before checking the lists.

### A.1

> [!Note] Solution
> (a) $S=\{-2,-1,0,1,2\}$.
>
> (b) $T\subseteq S$ is true because both $-2$ and $2$ belong to $S$. The statement $T\in S$ is false: the elements of $S$ are integers, not the set $\{-2,2\}$.
>
> (c) $\mathcal P(T)=\{\varnothing,\{-2\},\{2\},\{-2,2\}\}$.

### A.2

> [!Note] Solution
> (a) $S=\{-4,-2,0,2,4\}$.
>
> (b) Both statements are true: every element of $T$ lies in $S$, and $-2$ is an element of $T$.
>
> (c) $T\times\{0,1\}=\{(-2,0),(-2,1),(4,0),(4,1)\}$.

### A.3

> [!Note] Solution
> (a) $S=\{1,2,3,4,6,12\}$.
>
> (b) $T\subseteq S$ is true. Consequently $T\in\mathcal P(S)$ is also true, because the elements of a power set are precisely the subsets of the original set.
>
> (c) $\mathcal P(T)=\{\varnothing,\{2\},\{3\},\{2,3\}\}$.

### A.4

> [!Note] Solution
> (a) $S=\{0,1,4\}$. Repeated outputs such as $(-2)^2=2^2$ are listed only once in a set.
>
> (b) $T\subset S$ is true because $T\subseteq S$ and $4\in S\setminus T$. The statement $2\in S$ is false.
>
> (c) $T\times S=\{(0,0),(0,1),(0,4),(1,0),(1,1),(1,4)\}$.

### A.5

> [!Note] Solution
> (a) $S=\{-2,-1,0,1,2\}$.
>
> (b) $T\subseteq S$ is true. The statement $\{0\}\in S$ is false: $0$ is an element of $S$, but the singleton set $\{0\}$ is not.
>
> (c) $\mathcal P(T)=\{\varnothing,\{-1\},\{1\},\{-1,1\}\}$.

## B. Set Operations and Venn Regions

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

> [!Note] Solution
> Shade $(A\setminus B)\cup C$, equivalently $(A\cap\overline B)\cup C$.

### B.2

> [!Note] Solution
> Shade $\overline A\cup B\cup C$.

### B.3

> [!Note] Solution
> An implication is false only when its hypothesis is true and its conclusion is false. Thus the required region is
> $\overline{A\cup B}\cup C$.

### B.4

> [!Note] Solution
> Rewrite $x\in A\to x\in B$ as $x\in\overline A\cup B$. The required region is $(\overline A\cup B)\cap C$.

### B.5

> [!Note] Solution
> A biconditional is true when its two sides have the same truth value. The region is
> $(A\cap B\cap\overline C)\cup\bigl(\overline A\cap(\overline B\cup C)\bigr)$.

## C. Relations as Subsets of Cartesian Products

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

> [!Note] Solution
> (a) $R=\{(1,1),(2,2),(3,3)\}$.
>
> (b) Both $\forall x\,\exists!y\,((x,y)\in R)$ and $\forall y\,\exists!x\,((x,y)\in R)$ are true.
>
> (c) This is a function. Every input has a different output and every element of $Y$ occurs, so it is both injective and surjective (bijective).

### C.2

> [!Note] Solution
> (a) $R=\{(1,1),(2,1),(2,2),(2,3),(3,2)\}$.
>
> (b) Both statements are true: every input has at least one output, and $x=2$ is related to every $y\in Y$.
>
> (c) This is not a function because input $2$ has three outputs.

### C.3

> [!Note] Solution
> (a) $R=\{(1,1),(1,2),(2,1),(3,1)\}$.
>
> (b) $\forall y\,\exists x\,((x,y)\in R)$ is false because no pair has second coordinate $3$. The statement $\exists y\,\forall x\,((x,y)\in R)$ is true, witnessed by $y=1$.
>
> (c) This is not a function because input $1$ has outputs $1$ and $2$.

### C.4

> [!Note] Solution
> (a) $R=\{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2)\}$.
>
> (b) $\forall x\,\exists!y\,((x,y)\in R)$ is false because every input has more than one output. The statement $\exists x\,\forall y\,((x,y)\in R)$ is true, witnessed by either $x=1$ or $x=2$.
>
> (c) This is not a function because, for example, input $1$ has three outputs.

### C.5

> [!Note] Solution
> (a) $R=\{(1,1),(1,2),(2,2),(2,3),(3,2)\}$.
>
> (b) $\forall y\,\exists!x\,((x,y)\in R)$ is false because $y=2$ has three corresponding inputs. The statement $\exists y\,\forall x\,((x,y)\in R)$ is true, witnessed by $y=2$.
>
> (c) This is not a function because inputs $1$ and $2$ each have more than one output.

## D. Functions, Images, and Preimages

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

> [!Note] Solution
> (a) $f(\{1,3,4\})=\{a,b,c\}$ and $f^{-1}(\{a,b\})=\{1,2,3\}$.
>
> (b) The function is surjective because every element of $B$ is an output. It is not injective because $f(2)=f(3)=b$.

### D.2

> [!Note] Solution
> (a) $g(\{-1,0,2\})=\{4,5,7\}$ and $g^{-1}(\{4,7\})=\{-1,2\}$.
>
> (b) The function is bijective. If $g(m)=g(n)$, then $m+5=n+5$, so $m=n$; hence it is injective. Given any $y\in\mathbb Z$, choosing $n=y-5\in\mathbb Z$ gives $g(n)=y$; hence it is surjective.

### D.3

> [!Note] Solution
> (a) $h(\{-2,-1,0,2\})=\{0,1,4\}$ and $h^{-1}(\{0,1,4\})=\{-2,-1,0,1,2\}$.
>
> (b) The function is neither injective nor surjective. It is not injective because $h(1)=h(-1)=1$. It is not surjective because no negative integer is an output.

### D.4

> [!Note] Solution
> (a) $k(\{-1,0,1\})=\{-2,0,2\}$ and $k^{-1}(\{-2,0,4\})=\{-1,0,2\}$.
>
> (b) The function is injective: $2m=2n$ implies $m=n$. It is not surjective because no odd integer is an output.

### D.5

> [!Note] Solution
> (a) $q(\{0,2,3\})=\{0,4,9\}$ and $q^{-1}(\{1,16\})=\{1,4\}$.
>
> (b) The function is bijective. Nonnegative inputs with equal squares are equal, so $q$ is injective. Every element of the declared codomain is $m^2=q(m)$ for an allowed input $m\in\mathbb N_0$, so $q$ is surjective. Restricting the domain removes the collision between $m$ and $-m$; declaring the perfect squares as the codomain removes nonsquares that otherwise would have no preimage.

## E. Prove or Refute a Set/Function Claim

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

> [!Note] Solution
> The claim is true. For an arbitrary $y\in Y$,
> $$
> y\in f(U\cup V)
> \iff y=f(x)\text{ for some }x\in U\cup V
> \iff y\in f(U)\text{ or }y\in f(V)
> \iff y\in f(U)\cup f(V).
> $$
> The two sets therefore have exactly the same elements.

### E.2

> [!Note] Solution
> The claim is false. Let $X=\{1,2\}$, $Y=\{a\}$, define $f(1)=f(2)=a$, and take $U=\{1\}$ and $V=\{2\}$. Then $U\cap V=\varnothing$, so $f(U\cap V)=\varnothing$. But $f(U)=f(V)=\{a\}$, so $f(U)\cap f(V)=\{a\}$.

### E.3

> [!Note] Solution
> The claim is true. For an arbitrary $x\in X$,
> $$
> x\in f^{-1}(P\cap Q)
> \iff f(x)\in P\cap Q
> \iff f(x)\in P\text{ and }f(x)\in Q
> \iff x\in f^{-1}(P)\cap f^{-1}(Q).
> $$
> Hence the two preimages are equal.

### E.4

> [!Note] Solution
> The claim is true. For an arbitrary ordered pair $(x,y)$,
> $$
> (x,y)\in(A\cup B)\times C
> \iff (x\in A\text{ or }x\in B)\text{ and }y\in C
> \iff (x,y)\in A\times C\text{ or }(x,y)\in B\times C.
> $$
> The final condition is equivalent to $(x,y)\in(A\times C)\cup(B\times C)$.

### E.5

> [!Note] Solution
> The claim is false. Let $A=\{1\}$, $B=\varnothing$, and $C=\{1\}$. Then
> $A\cup B=\{1\}=A\cup C$, but $B\ne C$. Union with $A$ can hide a difference consisting only of elements already in $A$.

> [!TIP]- More Resources
> [Full COMP 2300 resource page](https://cs.du.edu/~ftl/2300/resources/)
