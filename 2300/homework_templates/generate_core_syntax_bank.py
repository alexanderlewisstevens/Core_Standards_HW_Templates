#!/usr/bin/env python3
"""Generate balanced T/F/N syntax-and-definition practice for all seven Cores.

Each Core has twenty concept families. Every family contains a true
proposition, a false proposition, and an item that is not a complete,
well-formed proposition under the stated conventions.

INSTRUCTOR-ONLY SOURCE: this generator contains answer labels, explanations,
and minimal repairs. Do not distribute or publish it with student materials.
"""

from __future__ import annotations

import hashlib
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


HERE = Path(__file__).resolve().parent
STUDENT_TEX = HERE / "core_definition_true_false_bank.tex"
KEY_TEX = HERE / "core_definition_true_false_key.tex"


@dataclass(frozen=True)
class Version:
    answer: str
    body: str
    explanation: str
    repair: str = ""


@dataclass(frozen=True)
class Family:
    category: str
    versions: dict[str, Version]


@dataclass(frozen=True)
class Core:
    name: str
    context: str
    families: tuple[Family, ...]


def family(
    category: str,
    true_body: str,
    true_why: str,
    false_body: str,
    false_why: str,
    n_body: str,
    n_why: str,
    n_repair: str,
) -> Family:
    return Family(
        category,
        {
            "T": Version("T", true_body, true_why),
            "F": Version("F", false_body, false_why),
            "N": Version("N", n_body, n_why, n_repair),
        },
    )


CORES: tuple[Core, ...] = (
    Core(
        "Logic",
        r"$p$ and $r$ are true; $q$ is false. Variables range over "
        r"$\mathbb Z$. $P(n)$ means \emph{$n$ is even}, $Q(n)$ means "
        r"\emph{$n>0$}, and $R(a,b)$ means \emph{$a<b$}. $P,Q$ are unary "
        r"predicates and $R$ is binary.",
        (
            family("Formation", r"$p$", "The assigned truth value of $p$ is true.",
                   r"$q$", "The assigned truth value of $q$ is false.",
                   r"$p\land$", "The binary connective is missing its right operand.",
                   r"$p\land q$"),
            family("Formation", r"$\neg q$", "Negation reverses the false value of $q$.",
                   r"$\neg p$", "Negation reverses the true value of $p$.",
                   r"$\neg$", "Negation has no operand.",
                   r"$\neg p$"),
            family("Formation", r"$p\land r$", "Both conjuncts are true.",
                   r"$p\land q$", "The second conjunct is false.",
                   r"$p\,q$", "Juxtaposing two proposition symbols is not a formation rule.",
                   r"$p\land q$"),
            family("Formation", r"$q\lor r$", "At least one disjunct is true.",
                   r"$q\lor q$", "Both disjuncts are false.",
                   r"$\lor q$", "The binary connective is missing its left operand.",
                   r"$p\lor q$"),
            family("Semantics", r"$q\to p$", "A false antecedent makes the conditional true.",
                   r"$p\to q$", "A true antecedent and false consequent make it false.",
                   r"$p\to$", "The conditional is missing its consequent.",
                   r"$p\to q$"),
            family("Semantics", r"$p\leftrightarrow r$", "The two sides have the same truth value.",
                   r"$p\leftrightarrow q$", "The two sides have different truth values.",
                   r"$p\leftrightarrow\land q$", "The conjunction has no left operand.",
                   r"$p\leftrightarrow(p\land q)$"),
            family("Equivalence", r"$p\lor\neg p$ is a tautology.",
                   "Excluded middle is true under every valuation.",
                   r"$p\land\neg p$ is a tautology.",
                   "A proposition and its negation cannot both be true.",
                   r"$p\lor\neg$ is a tautology.",
                   "The negation sign has no operand.",
                   r"$p\lor\neg p$ is a tautology."),
            family("Equivalence", r"$p\to q\equiv\neg p\lor q$.",
                   "This is the material-implication equivalence.",
                   r"$p\to q\equiv p\land q$.",
                   "The expressions differ when $p$ is false.",
                   r"$p\to q\equiv$.",
                   "The equivalence symbol is missing its right formula.",
                   r"$p\to q\equiv\neg p\lor q$."),
            family("Equivalence", r"$\neg(p\land q)\equiv\neg p\lor\neg q$.",
                   "This is De Morgan's law for conjunction.",
                   r"$\neg(p\lor q)\equiv\neg p\lor\neg q$.",
                   "The correct right side uses a conjunction.",
                   r"$\neg(p\land)\equiv\neg p$.",
                   "The conjunction inside the parentheses is incomplete.",
                   r"$\neg(p\land q)\equiv\neg p\lor\neg q$."),
            family("Semantics", r"A truth table for $p,q$ has $4$ rows.",
                   r"Two independent truth values give $2^2=4$ rows.",
                   r"A truth table for $p,q$ has $8$ rows.",
                   r"Eight rows are needed for three atomic propositions, not two.",
                   r"A truth table for $p,q$ has $2^{\Box}$ rows.",
                   "The box is an unfilled exponent placeholder, not a number.",
                   r"A truth table for $p,q$ has $2^2$ rows."),
            family("Arity/type", r"$P(2)$.", "Two is even.",
                   r"$P(3)$.", "Three is not even.",
                   r"$P$.", "A unary predicate symbol without an argument is not a proposition.",
                   r"$P(2)$."),
            family("Arity/type", r"$R(1,2)$.", "The inequality $1<2$ is true.",
                   r"$R(2,1)$.", "The inequality $2<1$ is false.",
                   r"$R(1)$.", "The binary predicate $R$ has only one argument.",
                   r"$R(1,2)$."),
            family("Binding/scope", r"$\forall n\,[P(n)\lor\neg P(n)]$.",
                   "For every integer, a proposition or its negation is true.",
                   r"$\forall n\,P(n)$.", "Not every integer is even.",
                   r"$\forall\,P(n)$.", "The universal quantifier does not bind a variable.",
                   r"$\forall n\,P(n)$."),
            family("Binding/scope", r"$\exists n\,[P(n)\land Q(n)]$.",
                   "Two is an even positive witness.",
                   r"$\exists n\,[P(n)\land\neg P(n)]$.",
                   "No integer can satisfy a predicate and its negation.",
                   r"$\exists n$.", "The quantifier has no formula in its scope.",
                   r"$\exists n\,P(n)$."),
            family("Binding/scope", r"$\neg\forall n\,P(n)\equiv\exists n\,\neg P(n)$.",
                   "Negating a universal produces an existential with a negated predicate.",
                   r"$\neg\exists n\,P(n)\equiv\exists n\,\neg P(n)$.",
                   "The quantifier on the right must be universal.",
                   r"$\neg\forall\,P(n)$.",
                   "The quantifier does not bind a variable.",
                   r"$\neg\forall n\,P(n)$."),
            family("Binding/scope", r"$\forall a\,\exists b\,R(a,b)$.",
                   "For any integer $a$, choose $b=a+1$.",
                   r"$\exists b\,\forall a\,R(a,b)$.",
                   "No integer is greater than every integer.",
                   r"$\forall a\,\exists\,R(a,b)$.",
                   "The existential quantifier does not bind a variable.",
                   r"$\forall a\,\exists b\,R(a,b)$."),
            family("Proposition/term", r"$\forall x\,[P(x)\lor\neg P(x)]$.",
                   "All variables are bound and excluded middle applies.",
                   r"$\forall x\,[P(x)\land\neg P(x)]$.",
                   "No integer makes a predicate and its negation both true.",
                   r"$P(x)$.", "The open formula has a free variable and no fixed truth value.",
                   r"$P(2)$ or $\forall x\,P(x)$."),
            family("Inference", r"$p,\ p\to r\ \therefore r$ is valid.",
                   "This is modus ponens.",
                   r"$r,\ p\to r\ \therefore p$ is valid.",
                   "This is affirming the consequent.",
                   r"$p,\ p\to\ \therefore r$ is valid.",
                   "The conditional premise is incomplete.",
                   r"$p,\ p\to r\ \therefore r$."),
            family("Inference", r"$p\to q,\ \neg q\ \therefore\neg p$ is valid.",
                   "This is modus tollens.",
                   r"$p\lor q,\ \neg p\ \therefore\neg q$ is valid.",
                   r"Disjunctive syllogism concludes $q$, not $\neg q$.",
                   r"$p\lor,\ \neg p\ \therefore q$ is valid.",
                   "The disjunction is missing its right operand.",
                   r"$p\lor q,\ \neg p\ \therefore q$."),
            family("Proposition/term", r"$1<2$.", "This closed inequality is true.",
                   r"$2<1$.", "This closed inequality is false.",
                   r"$1+2$.", "This is a numerical term, not a proposition.",
                   r"$1+2=3$."),
        ),
    ),
    Core(
        "Arguments",
        r"$p,q,r$ denote propositions. A displayed argument lists premises "
        r"before $\therefore$ and one conclusion after it. "
        r"$\Gamma\models C$ means every valuation satisfying all premises in "
        r"$\Gamma$ also satisfies $C$.",
        (
            family("Valid form", r"$p,\ p\to q\ \therefore q$ is valid.",
                   "This is modus ponens.",
                   r"$q,\ p\to q\ \therefore p$ is valid.",
                   "This is affirming the consequent.",
                   r"$p,\ p\to q\ \therefore$ is valid.",
                   "The argument has no conclusion.",
                   r"$p,\ p\to q\ \therefore q$."),
            family("Valid form", r"$p\to q,\ \neg q\ \therefore\neg p$ is valid.",
                   "This is modus tollens.",
                   r"$p\to q,\ \neg p\ \therefore\neg q$ is valid.",
                   "This is denying the antecedent.",
                   r"$p\to,\ \neg q\ \therefore\neg p$ is valid.",
                   "The conditional premise is incomplete.",
                   r"$p\to q,\ \neg q\ \therefore\neg p$."),
            family("Valid form", r"$p\lor q,\ \neg p\ \therefore q$ is valid.",
                   "This is disjunctive syllogism.",
                   r"$p\lor q,\ p\ \therefore\neg q$ is valid.",
                   "An inclusive disjunction permits both disjuncts to be true.",
                   r"$p\lor,\ \neg p\ \therefore q$ is valid.",
                   "The disjunction is missing an operand.",
                   r"$p\lor q,\ \neg p\ \therefore q$."),
            family("Valid form", r"$p\to q,\ q\to r\ \therefore p\to r$ is valid.",
                   "This is hypothetical syllogism.",
                   r"$p\to q,\ r\to q\ \therefore p\to r$ is valid.",
                   "The shared consequent does not link $p$ to $r$.",
                   r"$p\to q,\ q\to\ \therefore p\to r$ is valid.",
                   "The second premise is incomplete.",
                   r"$p\to q,\ q\to r\ \therefore p\to r$."),
            family("Valid form", r"$p,\ q\ \therefore p\land q$ is valid.",
                   "Conjunction combines two established propositions.",
                   r"$p\ \therefore p\land q$ is valid.",
                   "The premise provides no support for $q$.",
                   r"$p,\ q\ \therefore p\land$ is valid.",
                   "The conclusion is missing a conjunct.",
                   r"$p,\ q\ \therefore p\land q$."),
            family("Valid form", r"$p\ \therefore p\lor q$ is valid.",
                   "This is addition.",
                   r"$p\lor q\ \therefore p$ is valid.",
                   "A disjunction does not identify which disjunct is true.",
                   r"$p\ \therefore\lor q$ is valid.",
                   "The conclusion's disjunction has no left operand.",
                   r"$p\ \therefore p\lor q$."),
            family("Validity/soundness", "A sound argument is valid and has true premises.",
                   "That is the definition of soundness.",
                   "A valid argument must have true premises.",
                   "Validity concerns truth preservation, not the actual truth of premises.",
                   r"Soundness $=$ valid $\land$.",
                   "The conjunction has no right-hand condition.",
                   r"Soundness $=$ valid $\land$ true premises."),
            family("Validity/soundness",
                   "A countermodel to validity makes every premise true and the conclusion false.",
                   "Such a valuation directly violates truth preservation.",
                   "A countermodel makes one premise false and the conclusion true.",
                   "That valuation does not demonstrate invalidity.",
                   r"$\Gamma\models$.",
                   "Semantic entailment is missing its conclusion.",
                   r"$\Gamma\models C$."),
            family("Validity/soundness",
                   "An invalid argument can have a true conclusion.",
                   "Validity concerns the inferential connection, not conclusion truth alone.",
                   "A true conclusion makes every argument for it valid.",
                   "A conclusion may be accidentally true.",
                   r"true $\therefore$.",
                   "The conclusion after the therefore sign is missing.",
                   r"$p\ \therefore p$."),
            family("Consistency", r"$p$ and $\neg p$ are inconsistent.",
                   "No valuation makes both true.",
                   r"$p$ and $p\lor q$ are inconsistent.",
                   "Any valuation with $p$ true satisfies both.",
                   r"$p$ and $\neg$ are inconsistent.",
                   "The second expression is not a complete proposition.",
                   r"$p$ and $\neg p$ are inconsistent."),
            family("Assumptions",
                   "A necessary assumption must hold for the stated support to work.",
                   "Removing a necessary assumption breaks the inferential link.",
                   "A necessary assumption is merely an unrelated true statement.",
                   "Relevance to the inferential link is essential.",
                   r"premise $\because$.",
                   "The because marker is missing the supporting proposition.",
                   r"$q$ because $p$."),
            family("Flaws",
                   "A circular argument uses its conclusion as support for itself.",
                   "That is the defining defect of circular reasoning.",
                   "An argument becomes noncircular whenever its conclusion is true.",
                   "Truth of the conclusion does not remove circular support.",
                   r"$p\therefore$ because $p$.",
                   "The displayed argument is missing its conclusion.",
                   r"$p\therefore p$."),
            family("Causal reasoning",
                   "A correlation alone does not establish which variable causes the other.",
                   "Alternative causes and reverse direction remain possible.",
                   "A correlation by itself proves a causal mechanism.",
                   "Association is not sufficient evidence of mechanism.",
                   r"cause$(p,q,$.",
                   "The function-like notation has an unmatched delimiter and missing argument.",
                   r"$\operatorname{cause}(p,q)$."),
            family("Generalization",
                   "A representative sample is relevant to a population generalization.",
                   "Representativeness affects how well the sample supports the claim.",
                   "Sample size and selection method never affect a generalization.",
                   "Both can materially affect its strength.",
                   r"sample $\subseteq$.",
                   "The subset relation is missing the population on the right.",
                   r"sample $\subseteq$ population."),
            family("Conditionals",
                   r"In $p\to q$, $q$ is necessary for $p$.",
                   "If $p$ occurs, $q$ must occur.",
                   r"In $p\to q$, $q$ is sufficient for $p$.",
                   "The conditional does not say that $q$ guarantees $p$.",
                   r"In $p\to$, the consequent is necessary for $p$.",
                   "The conditional has no consequent.",
                   r"In $p\to q$, $q$ is necessary for $p$."),
            family("Strengthen",
                   "A strengthening answer adds support to the conclusion relative to the premises.",
                   "That is the task of a strengthen question.",
                   "A strengthening answer must independently prove the conclusion.",
                   "Additional support need not amount to a proof.",
                   r"premises $\uparrow$ conclusion $\because$.",
                   "The support marker is missing a supporting claim.",
                   r"premises support conclusion."),
            family("Weaken",
                   "A weakening answer may expose an alternative explanation.",
                   "An alternative explanation can reduce causal support.",
                   "A weakening answer must establish the exact negation of the conclusion.",
                   "Reducing support is enough; refutation is not required.",
                   r"alternative $\lor$.",
                   "The disjunction has no second alternative.",
                   r"alternative A $\lor$ alternative B."),
            family("Must be true",
                   "A must-be-true answer follows from all the supplied facts.",
                   "It must hold in every case allowed by those facts.",
                   "A statement that is merely compatible with the facts must be true.",
                   "Compatibility is weaker than entailment.",
                   r"facts $\models$.",
                   "The entailment symbol is missing the proposed conclusion.",
                   r"facts $\models C$."),
            family("Comparison",
                   "A point-at-issue answer states something one speaker accepts and the other rejects.",
                   "That is a genuine disagreement.",
                   "Different examples guarantee that two speakers disagree.",
                   "They may use different examples while accepting the same claim.",
                   r"speaker A $\leftrightarrow$.",
                   "The biconditional is missing its right-hand statement.",
                   r"speaker A accepts $p$; speaker B rejects $p$."),
            family("Argument structure",
                   "Parallel arguments can share a logical form while discussing different topics.",
                   "Logical form abstracts away from subject matter.",
                   "Parallel reasoning requires the same nouns in both arguments.",
                   "Matching topic words does not determine inferential structure.",
                   r"$p+q\ \therefore r$.",
                   "Arithmetic addition is not defined for proposition symbols here.",
                   r"$p\land q\ \therefore r$."),
        ),
    ),
    Core(
        "Sets",
        r"$U=\{1,2,3,4\}$, $A=\{1,2\}$, $B=\{2,3\}$, and $C=A$. "
        r"Complements are relative to $U$. Let $f:A\to U$ satisfy "
        r"$f(1)=2$, $f(2)=4$, and let $R=\{(1,1),(2,2)\}$ be a relation on $A$.",
        (
            family("Membership", r"$1\in A$.", "One is listed as an element of $A$.",
                   r"$3\in A$.", "Three is not an element of $A$.",
                   r"$1\in$.", "Membership is missing the set on the right.",
                   r"$1\in A$."),
            family("Subset", r"$A\subseteq U$.", "Every element of $A$ lies in $U$.",
                   r"$B\subseteq A$.", "Three belongs to $B$ but not to $A$.",
                   r"$A\subseteq$.", "The subset relation is missing its right operand.",
                   r"$A\subseteq U$."),
            family("Equality", r"$A=C$.", "The context defines $C$ to equal $A$.",
                   r"$A=B$.", "The sets have different elements.",
                   r"$A=\{1,2$.", "The set delimiter is not closed.",
                   r"$A=\{1,2\}$."),
            family("Empty set", r"$\varnothing\subseteq A$.",
                   "The empty set is a subset of every set.",
                   r"$\varnothing\in A$.", "Neither element of $A$ is the empty set.",
                   r"$\varnothing\subseteq$.", "The subset relation has no right operand.",
                   r"$\varnothing\subseteq A$."),
            family("Cardinality", r"$|A|=2$.", "The set $A$ has two elements.",
                   r"$|A|=3$.", "The set $A$ does not have three elements.",
                   r"$|A|=$.", "The equality has no right-hand value.",
                   r"$|A|=2$."),
            family("Union", r"$A\cup B=\{1,2,3\}$.",
                   "The union contains everything in either set.",
                   r"$A\cup B=\{2\}$.", "The display gives the intersection, not the union.",
                   r"$A\cup=\{1,2,3\}$.", "Union is missing its second set.",
                   r"$A\cup B=\{1,2,3\}$."),
            family("Intersection", r"$A\cap B=\{2\}$.",
                   "Two is the only shared element.",
                   r"$A\cap B=\{1,2,3\}$.", "The display gives the union.",
                   r"$A\cap\in B$.", "Intersection is missing a set and membership is missing an element.",
                   r"$A\cap B=\{2\}$."),
            family("Difference", r"$A\setminus B=\{1\}$.",
                   "One is in $A$ but not $B$.",
                   r"$A\setminus B=\{2\}$.", "Two lies in both sets and is removed.",
                   r"$A\setminus$.", "Set difference is missing its second set.",
                   r"$A\setminus B$."),
            family("Complement", r"$A^c=\{3,4\}$.", "These are the elements of $U$ outside $A$.",
                   r"$A^c=\{1,2\}$.", "That set is $A$, not its complement.",
                   r"$(A\cup)^c$.", "The union inside the parentheses is incomplete.",
                   r"$(A\cup B)^c$."),
            family("Set laws", r"$(A\cup B)^c=A^c\cap B^c$.",
                   "This is De Morgan's law for sets.",
                   r"$(A\cup B)^c=A^c\cup B^c$.",
                   "The operation on the right must switch to intersection.",
                   r"$(A\cup B)^c=A^c\cap$.",
                   "The intersection is missing its second set.",
                   r"$(A\cup B)^c=A^c\cap B^c$."),
            family("Power set", r"$|\mathcal P(A)|=4$.",
                   r"A two-element set has $2^2=4$ subsets.",
                   r"$|\mathcal P(A)|=2$.", "The power set contains more than the singleton subsets.",
                   r"$\mathcal P()=A$.", "The power-set operator has no set argument.",
                   r"$\mathcal P(A)$."),
            family("Power set", r"$\varnothing\in\mathcal P(A)$.",
                   "The empty set is a subset of $A$.",
                   r"$\{3\}\in\mathcal P(A)$.", "The set $\{3\}$ is not a subset of $A$.",
                   r"$\mathcal P(A)\in$.", "Membership is missing the set on the right.",
                   r"$\varnothing\in\mathcal P(A)$."),
            family("Ordered pairs", r"$(1,2)\ne(2,1)$.",
                   "Ordered pairs are equal only when corresponding entries agree.",
                   r"$(1,2)=(2,1)$.", "The first coordinates differ.",
                   r"$(1,)\in A\times B$.", "The ordered pair is missing its second coordinate.",
                   r"$(1,2)\in A\times B$."),
            family("Cartesian product", r"$|A\times B|=4$.",
                   r"There are $2\cdot2=4$ ordered pairs.",
                   r"$|A\times B|=2$.", "The cardinalities multiply.",
                   r"$A\times\in B$.", "The product is missing a set and membership is missing an element.",
                   r"$A\times B$."),
            family("Relations", r"$R$ is reflexive on $A$.",
                   "Both $(1,1)$ and $(2,2)$ belong to $R$.",
                   r"$R$ is irreflexive on $A$.", "Every element is related to itself.",
                   r"$1R$.", "The binary relation notation is missing a second element.",
                   r"$1R1$."),
            family("Relations", r"$R$ is symmetric on $A$.",
                   "Every pair in $R$ is diagonal and reverses to itself.",
                   r"$\{(1,2)\}$ is symmetric on $A$.",
                   "Its reverse pair $(2,1)$ is missing.",
                   r"$(1,2)\in R\Rightarrow(2,)\in R$.",
                   "The second ordered pair is incomplete.",
                   r"$(1,2)\in R\Rightarrow(2,1)\in R$."),
            family("Functions", r"$f(1)=2$.", "This value is specified in the context.",
                   r"$f(2)=2$.", "The context specifies $f(2)=4$.",
                   r"$f(1,2)=4$.", "The function $f$ has one input, not two.",
                   r"$f(2)=4$."),
            family("Functions", r"$f$ is injective.",
                   "Its two distinct inputs have distinct outputs.",
                   r"$f$ is surjective onto $U$.", "The values $1$ and $3$ are not outputs.",
                   r"$f(A)=2\land$.", "The conjunction is incomplete, and $f(A)$ is not defined by the stated elementwise notation.",
                   r"$f(1)=2$."),
            family("Binding/type", r"$\forall x\in A,\ x\in U$.",
                   "Every element of $A$ lies in $U$.",
                   r"$\forall x\in U,\ x\in A$.", "Three and four are counterexamples.",
                   r"$x\in A$.", "The variable $x$ is neither assigned nor bound.",
                   r"$\forall x\in A,\ x\in U$."),
            family("Proposition/term", r"$2\in A\cap B$.", "Two is in both sets.",
                   r"$1\in A\cap B$.", "One is not in $B$.",
                   r"$A\cap B$.", "This is a set-valued term, not a proposition.",
                   r"$A\cap B=\{2\}$."),
        ),
    ),
    Core(
        "Proofs",
        r"Variables range over $\mathbb Z$ when bound. $P$ and $Q$ denote "
        r"propositions, and $P(n)$ denotes a proposition about an integer $n$. "
        r"A formula with an unbound variable is not a complete proposition.",
        (
            family("Direct proof",
                   r"A direct proof of $P\to Q$ may assume $P$ and derive $Q$.",
                   "That is the standard direct-proof structure.",
                   r"A direct proof of $P\to Q$ may assume $Q$ and derive $P$.",
                   "That proves the converse, not the stated conditional.",
                   r"Assume $P$; therefore.",
                   "The proof fragment has no derived conclusion.",
                   r"Assume $P$; therefore $Q$."),
            family("Contrapositive",
                   r"Proving $\neg Q\to\neg P$ proves $P\to Q$.",
                   "A conditional is logically equivalent to its contrapositive.",
                   r"Proving $Q\to P$ proves $P\to Q$.",
                   "The converse need not be equivalent to the original.",
                   r"$\neg Q\to\neg$.",
                   "The conditional's consequent is incomplete.",
                   r"$\neg Q\to\neg P$."),
            family("Contradiction",
                   r"To prove $P$ by contradiction, one may assume $\neg P$ and derive $\bot$.",
                   "A contradiction rules out the negation of the goal.",
                   r"To prove $P$ by contradiction, assume $P$ and stop.",
                   "Restating the goal does not derive a contradiction.",
                   r"$\neg P\Rightarrow$.",
                   "The implication has no conclusion.",
                   r"$\neg P\Rightarrow\bot$."),
            family("Cases",
                   "A proof by cases must cover every possibility allowed by the hypotheses.",
                   "Otherwise the uncovered cases remain unproved.",
                   "A proof by cases is complete after one convenient case.",
                   "One case does not establish a general result.",
                   r"case 1 $\lor$.",
                   "The disjunction of cases is incomplete.",
                   r"case 1 $\lor$ case 2."),
            family("Biconditional",
                   r"To prove $P\leftrightarrow Q$, it is enough to prove $P\to Q$ and $Q\to P$.",
                   "The two directions establish equivalence.",
                   r"To prove $P\leftrightarrow Q$, it is enough to prove only $P\to Q$.",
                   "One direction does not establish a biconditional.",
                   r"$P\leftrightarrow$.",
                   "The biconditional is missing its right formula.",
                   r"$P\leftrightarrow Q$."),
            family("Universal proof",
                   "A proof of a universal statement may begin with an arbitrary object in the domain.",
                   "The argument must not depend on a special choice.",
                   "A proof of a universal statement may choose only an object with a convenient extra property.",
                   "That proves at most a special case.",
                   r"Let $n=$ be arbitrary.",
                   "The equality is incomplete.",
                   r"Let $n\in\mathbb Z$ be arbitrary."),
            family("Existential proof",
                   r"To prove $\exists n\,P(n)$, one valid witness is sufficient.",
                   "An existential claim asks for at least one example.",
                   r"To prove $\exists n\,P(n)$, one must prove $P(n)$ for every integer.",
                   "That is stronger than an existential claim.",
                   r"$\exists\,P(n)$.",
                   "The existential quantifier does not bind a variable.",
                   r"$\exists n\,P(n)$."),
            family("Instantiation",
                   r"From $\forall n\,P(n)$, one may infer $P(7)$.",
                   "Universal instantiation permits any object in the domain.",
                   r"From $\exists n\,P(n)$, one may infer $P(7)$ without further information.",
                   "The existential witness need not be the preferred object.",
                   r"From $\forall n$, infer $P(7)$.",
                   "The universal premise has no formula in its scope.",
                   r"From $\forall n\,P(n)$, infer $P(7)$."),
            family("Instantiation",
                   r"From $\exists n\,P(n)$, one may introduce a fresh symbol $c$ with $P(c)$.",
                   "The fresh symbol denotes some unspecified witness.",
                   r"From $\exists n\,P(n)$, one may treat the witness as every integer.",
                   "An existential witness does not represent all objects.",
                   r"Let $c$ witness $\exists n$.",
                   "The existential statement is missing its predicate.",
                   r"Let $c$ witness $\exists n\,P(n)$."),
            family("Counterexample",
                   r"One integer $c$ with $\neg P(c)$ disproves $\forall n\,P(n)$.",
                   "A universal claim fails at any counterexample.",
                   r"One integer $c$ with $P(c)$ disproves $\forall n\,P(n)$.",
                   "A confirming example does not refute the universal.",
                   r"$c$ is a counterexample to.",
                   "The universal claim being refuted is missing.",
                   r"$c$ is a counterexample to $\forall n\,P(n)$."),
            family("Definitions", r"$6=2(3)$ proves that $6$ is even.",
                   "It exhibits the required integer multiplier.",
                   r"$9=2(4)$ proves that $9$ is even.",
                   "The displayed equality is false and gives no witness.",
                   r"$2k$.", "This is an integer-valued term, not a proposition.",
                   r"$6=2(3)$."),
            family("Definitions", r"$9=2(4)+1$ proves that $9$ is odd.",
                   "It has the required form with an integer witness.",
                   r"$6=2(3)+1$ proves that $6$ is odd.",
                   "The displayed equality is false.",
                   r"$2k+1$.", "This is an integer-valued term, not a proposition.",
                   r"$9=2(4)+1$."),
            family("Definitions", r"$\frac{3}{4}$ is rational.",
                   "It is a quotient of integers with nonzero denominator.",
                   r"$\sqrt2$ is rational.",
                   "The square root of two is irrational.",
                   r"$\frac{3}{0}$ is rational.",
                   "Division by zero is undefined, so the displayed term is not defined.",
                   r"$\frac{3}{4}$ is rational."),
            family("Definitions", r"$4\mid20$.", "Twenty equals $4(5)$.",
                   r"$6\mid20$.", "No integer multiplied by six equals twenty.",
                   r"$4\mid$.", "Divisibility is missing its right operand.",
                   r"$4\mid20$."),
            family("Parity", "The sum of two even integers is even.",
                   r"If $a=2j$ and $b=2k$, then $a+b=2(j+k)$.",
                   "The sum of two odd integers is odd.",
                   r"If $a=2j+1$ and $b=2k+1$, then $a+b=2(j+k+1)$ is even.",
                   r"even $+$ odd $=$.",
                   "The equality has no parity class on the right.",
                   r"even $+$ odd $=$ odd."),
            family("Parity", "The product of two odd integers is odd.",
                   r"$(2j+1)(2k+1)=2(2jk+j+k)+1$.",
                   "The product of an even integer and an odd integer is odd.",
                   "The even factor makes the product even.",
                   r"odd $\cdot$.",
                   "Multiplication is missing its second factor.",
                   r"odd $\cdot$ odd $=$ odd."),
            family("Proof language", "A theorem is a statement established by proof.",
                   "That is the role of a theorem.",
                   "A conjecture is already established by proof.",
                   "A conjecture is a proposed statement not yet proved.",
                   r"theorem $\Rightarrow$.",
                   "The implication has no conclusion.",
                   r"theorem $\Rightarrow$ proved statement."),
            family("Conditionals",
                   r"In $P\to Q$, $Q$ is necessary for $P$.",
                   "If $P$ holds, $Q$ must follow.",
                   r"In $P\to Q$, $Q$ is sufficient for $P$.",
                   "The conditional does not allow the converse inference.",
                   r"In $P\to$, the consequent is necessary.",
                   "The conditional has no consequent.",
                   r"In $P\to Q$, $Q$ is necessary for $P$."),
            family("Proof validity",
                   "Using the desired conclusion as an unproved premise is circular.",
                   "The conclusion cannot serve as its own independent support.",
                   "A proof is complete when its final claim merely repeats an unsupported first claim.",
                   "Repetition without justification is not a derivation.",
                   r"$P\because P\therefore$.",
                   "The therefore marker has no conclusion.",
                   r"$P\because P\therefore P$."),
            family("Binding/type",
                   r"$\forall n\in\mathbb Z,\ n^2\ge0$.",
                   "Every integer square is nonnegative.",
                   r"$\forall n\in\mathbb Z,\ n^2<0$.",
                   "No integer square is negative.",
                   r"$n^2\ge0$.",
                   "The variable $n$ is free and has not been assigned.",
                   r"$\forall n\in\mathbb Z,\ n^2\ge0$."),
        ),
    ),
    Core(
        "Divisibility",
        r"Let $a,b,c$ be arbitrary integers and let $m\ge2$ be a fixed integer. "
        r"All other variables are integers when quantified or assigned. In $a\mid b$, the left integer "
        r"divides the right integer. In $a\equiv_m b$, the modulus satisfies "
        r"$m\ge2$. A base-$b$ numeral may use only digits $0,\ldots,b-1$.",
        (
            family("Divisibility", r"$3\mid12$.", "Twelve equals $3(4)$.",
                   r"$5\mid12$.", "Twelve is not an integer multiple of five.",
                   r"$3\mid$.", "Divisibility is missing its right operand.",
                   r"$3\mid12$."),
            family("Definition", r"$4\mid20\iff\exists k\in\mathbb Z,\ 20=4k$.",
                   "This is the definition of divisibility.",
                   r"$6\mid20\iff\exists k\in\mathbb Z,\ 20=5k$.",
                   "The left side is false while the right side has witness $k=4$.",
                   r"$20=4k$.", "The variable $k$ is free and has not been assigned.",
                   r"$\exists k\in\mathbb Z,\ 20=4k$."),
            family("Zero", r"$7\mid0$.", "Zero equals $7(0)$.",
                   r"$0\mid7$.", "No integer multiplied by zero equals seven.",
                   r"$0\mid$.", "Divisibility is missing its right operand.",
                   r"$0\mid0$."),
            family("Divisibility laws",
                   r"If $a\mid b$ and $b\mid c$, then $a\mid c$.",
                   "Substituting the two integer-multiple equations proves transitivity.",
                   r"If $a\mid b$, then $b\mid a$.",
                   "Divisibility is not generally symmetric.",
                   r"$a\mid b\mid$.", "The chained display is missing its final integer.",
                   r"$a\mid b$ and $b\mid c$."),
            family("Linear combinations",
                   r"If $a\mid b$ and $a\mid c$, then $a\mid(3b-2c)$.",
                   "Any integer linear combination remains divisible by $a$.",
                   r"If $a\mid b$, then $a\mid(b+1)$.",
                   "Adding one need not preserve divisibility.",
                   r"$a\mid(3b-)$.", "The linear combination is incomplete.",
                   r"$a\mid(3b-2c)$."),
            family("Greatest common divisor", r"$\gcd(12,18)=6$.",
                   "Six is their greatest positive common divisor.",
                   r"$\gcd(12,18)=12$.", "Twelve does not divide eighteen.",
                   r"$\gcd(12,)$.", "The binary gcd operation is missing an argument.",
                   r"$\gcd(12,18)$."),
            family("Coprimality", r"$\gcd(8,15)=1$.", "The two integers are coprime.",
                   r"$\gcd(8,12)=1$.", "Their gcd is four.",
                   r"$\gcd(,15)=1$.", "The first gcd argument is missing.",
                   r"$\gcd(8,15)=1$."),
            family("Division algorithm",
                   r"$23=5(4)+3$ with $0\le3<5$.",
                   "This is the valid quotient-remainder representation.",
                   r"$23=5(3)+8$ with $0\le8<5$.",
                   "The remainder condition is false.",
                   r"$23=5q+r$.", "The variables $q$ and $r$ are free.",
                   r"$\exists q,r\in\mathbb Z:\ 23=5q+r$ and $0\le r<5$."),
            family("Remainders", r"$23\bmod 5=3$.", "Twenty-three leaves remainder three upon division by five.",
                   r"$23\bmod 5=5$.", "A remainder modulo five must be below five.",
                   r"$23\bmod$.", "The modulus is missing.",
                   r"$23\bmod 5$."),
            family("Congruence", r"$17\equiv_5 2$.", "Their difference is fifteen, divisible by five.",
                   r"$17\equiv_5 3$.", "Their difference is fourteen, not divisible by five.",
                   r"$17\equiv_5$.", "Congruence is missing its right operand.",
                   r"$17\equiv_5 2$."),
            family("Congruence", r"$a\equiv_m b\iff m\mid(a-b)$.",
                   "This is the definition of congruence modulo $m$.",
                   r"$a\equiv_m b\iff a\mid(m-b)$.",
                   "The divisibility relation in the definition is reversed and altered.",
                   r"$a\equiv b$.", "The modulus required by the stated notation is missing.",
                   r"$a\equiv_m b$."),
            family("Congruence laws",
                   r"$a\equiv_m b\Rightarrow a+c\equiv_m b+c$.",
                   "Adding the same integer preserves the difference.",
                   r"$a\equiv_m b\Rightarrow a+c\equiv_m b$.",
                   "Adding $c$ to only one side need not preserve congruence.",
                   r"$a+c\equiv_m$.", "Congruence is missing its right operand.",
                   r"$a+c\equiv_m b+c$."),
            family("Congruence laws",
                   r"$a\equiv_m b\Rightarrow ac\equiv_m bc$.",
                   "Multiplying the divisible difference by $c$ preserves divisibility.",
                   r"$a\equiv_m b\Rightarrow ac\equiv_m b$.",
                   "Multiplying only one side need not preserve congruence.",
                   r"$ac\equiv_m bc\land$.", "The conjunction is incomplete.",
                   r"$ac\equiv_m bc$."),
            family("Cancellation",
                   r"If $ac\equiv_m bc$ and $\gcd(c,m)=1$, then $a\equiv_m b$.",
                   "A factor coprime to the modulus can be cancelled.",
                   r"If $ac\equiv_m bc$, then $a\equiv_m b$ without any condition on $c$.",
                   r"For example, $2\cdot1\equiv_4 2\cdot3$ but $1\not\equiv_4 3$.",
                   r"$\gcd(c,m)=\Rightarrow a\equiv_m b$.",
                   "The gcd equality is missing its value.",
                   r"$\gcd(c,m)=1\Rightarrow a\equiv_m b$."),
            family("Parity", r"$14$ is even.", r"$14=2(7)$.",
                   r"$14$ is odd.", "Fourteen has the even form, not the odd form.",
                   r"$14=2k+1$.", "The variable $k$ is free and unassigned.",
                   r"$\exists k\in\mathbb Z,\ 14=2k$."),
            family("Primes", r"$13$ is prime.", "Its only positive divisors are one and thirteen.",
                   r"$15$ is prime.", "Three and five are nontrivial divisors.",
                   r"$1$ is prime because.", "The explanation is syntactically incomplete.",
                   r"$13$ is prime because its only positive divisors are $1$ and $13$."),
            family("Base notation", r"$(101)_2=5$.", r"$1\cdot2^2+0\cdot2+1=5$.",
                   r"$(101)_2=6$.", "The place-value sum is five.",
                   r"$(102)_2=6$.", "Digit two is not permitted in base two.",
                   r"$(110)_2=6$."),
            family("Base notation", r"$(210)_3=21$.", r"$2\cdot3^2+1\cdot3=21$.",
                   r"$(210)_3=19$.", "The place-value sum is twenty-one.",
                   r"$(31)_3=10$.", "Digit three is not permitted in base three.",
                   r"$(101)_3=10$."),
            family("Repeated division",
                   r"$202=2(101)+0$ is a valid first binary-conversion step.",
                   "The equality holds and the remainder is zero.",
                   r"$202=2(100)+2$ is a valid first binary-conversion step.",
                   "The remainder must be zero or one.",
                   r"$202=2()+0$.", "The quotient is missing.",
                   r"$202=2(101)+0$."),
            family("Place value",
                   r"$(10)_b(10)_b=(100)_b$ for every base $b\ge2$.",
                   r"Both sides equal $b^2$.",
                   r"$(10)_b(10)_b=(1000)_b$ for every base $b\ge2$.",
                   r"The right side equals $b^3$, not $b^2$.",
                   r"$(10)_1(10)_1=(100)_1$.",
                   "Base one is not positional notation under the stated convention.",
                   r"$(10)_2(10)_2=(100)_2$."),
        ),
    ),
    Core(
        "Induction",
        r"$P(n)$ is a proposition indexed by integers $n\ge1$. In an induction "
        r"step, $k$ is a fixed but arbitrary integer in the stated range. "
        r"Also let $a_1=2$ and $a_{n+1}=a_n+3$ for $n\ge1$.",
        (
            family("Base case",
                   r"For a theorem beginning at $n=1$, the base case is $P(1)$.",
                   "The base must match the theorem's first index.",
                   r"For a theorem beginning at $n=1$, the base case is necessarily $P(0)$.",
                   "Zero lies outside the stated starting range.",
                   r"The base case is $P()$.",
                   "The unary predicate has no argument.",
                   r"The base case is $P(1)$."),
            family("Induction hypothesis",
                   r"The induction hypothesis assumes $P(k)$ for an arbitrary $k\ge1$.",
                   "It supplies the current case for proving the next one.",
                   r"The induction hypothesis assumes $P(k+1)$ in order to prove $P(k+1)$.",
                   "That is circular.",
                   r"Assume $P(k)\land$.",
                   "The conjunction is incomplete.",
                   r"Assume $P(k)$."),
            family("Induction step",
                   r"The induction step proves $P(k)\to P(k+1)$.",
                   "It establishes that truth passes to the next index.",
                   r"The induction step proves only $P(k)\to P(k)$.",
                   "That does not advance to a new case.",
                   r"$P(k)\to P()$.",
                   "The predicate in the consequent has no argument.",
                   r"$P(k)\to P(k+1)$."),
            family("Induction principle",
                   r"$P(1)$ and $\forall k\ge1\,[P(k)\to P(k+1)]$ imply $\forall n\ge1\,P(n)$.",
                   "This is the principle of ordinary induction.",
                   r"$P(1)$ alone implies $\forall n\ge1\,P(n)$.",
                   "A base case does not propagate without an induction step.",
                   r"$P(1)\land\forall k\ge1\Rightarrow\forall n\,P(n)$.",
                   "The universal quantifier over $k$ has no formula in its scope.",
                   r"$P(1)\land\forall k\ge1\,[P(k)\to P(k+1)]$."),
            family("Induction logic",
                   "Checking several initial cases does not prove every later case.",
                   "A finite list lacks the propagation argument.",
                   r"Checking $P(1),P(2),P(3)$ proves $\forall n\ge1\,P(n)$.",
                   "Later cases remain unproved.",
                   r"$P(1),P(2),P(3)\therefore$.",
                   "The displayed argument has no conclusion.",
                   r"$P(1),P(2),P(3)\therefore P(1)\land P(2)\land P(3)$."),
            family("Arbitrary index",
                   "The induction step must work for an arbitrary allowed value of $k$.",
                   "A special choice would establish only a special transition.",
                   r"Proving $P(7)\to P(8)$ establishes the complete induction step for every $k$.",
                   "It verifies only one transition.",
                   r"Let $k=$ be arbitrary.",
                   "The equality is incomplete.",
                   r"Let $k\ge1$ be arbitrary."),
            family("Strong induction",
                   r"Strong induction may assume $P(1),\ldots,P(k)$ to prove $P(k+1)$.",
                   "It makes all earlier cases available.",
                   r"Strong induction assumes $P(k+1)$ to prove $P(k+1)$.",
                   "That is circular.",
                   r"Assume $P(1),\ldots,$.",
                   "The list of assumed cases has no endpoint.",
                   r"Assume $P(1),\ldots,P(k)$."),
            family("Strong induction",
                   r"Ordinary and strong induction can prove the same class of statements.",
                   "They are equivalent proof principles.",
                   r"Strong induction is valid only when ordinary induction fails.",
                   "It is a convenient formulation, not a stronger logic.",
                   r"$P(1)\land\cdots\land P(k)\to$.",
                   "The conditional has no consequent.",
                   r"$P(1)\land\cdots\land P(k)\to P(k+1)$."),
            family("Base coverage",
                   "A recurrence using two preceding terms may require two initial cases.",
                   "The induction step may need both earlier values.",
                   "Every induction proof has exactly one base case.",
                   "The number of required starting cases depends on the statement and step.",
                   r"Base cases: $P(1),$.",
                   "The list ends after a comma.",
                   r"Base cases: $P(1),P(2)$."),
            family("Recurrences",
                   "A recurrence defines later terms using earlier terms.",
                   "That is the defining role of a recurrence.",
                   "A recurrence alone always determines a unique sequence without initial values.",
                   "Different initial values can produce different sequences.",
                   r"$a_{n+1}=a_n+$.",
                   "The right side is incomplete.",
                   r"$a_{n+1}=a_n+3$."),
            family("Initial conditions",
                   r"The recurrence $a_{n+1}=a_n+3$ and $a_1=2$ determine a unique sequence.",
                   "The recurrence and starting value determine each later term.",
                   r"The recurrence $a_{n+1}=a_n+3$ determines one unique sequence without $a_1$.",
                   "Each possible starting value gives a different sequence.",
                   r"$a_1=$.",
                   "The initial-value equality is incomplete.",
                   r"$a_1=2$."),
            family("Sequence values", r"$a_4=11$.",
                   "The sequence is $2,5,8,11,\ldots$.",
                   r"$a_4=8$.", "Eight is the third term.",
                   r"$a_{4}+$.", "This is an incomplete arithmetic term, not a proposition.",
                   r"$a_4=11$."),
            family("Closed forms", r"$a_n=3n-1$ for every $n\ge1$.",
                   "It matches $a_1=2$ and increases by three.",
                   r"$a_n=3n+1$ for every $n\ge1$.",
                   "At $n=1$ it gives four instead of two.",
                   r"$a_n=3n-1$.", "The variable $n$ is free in this standalone formula.",
                   r"$\forall n\ge1,\ a_n=3n-1$."),
            family("Induction algebra",
                   "In a sum proof, the induction hypothesis may replace the partial sum through $k$.",
                   "That is the hypothesis's permitted use.",
                   "The induction hypothesis may replace a different expression that it does not mention.",
                   "Substitution requires an established equality for that expression.",
                   r"$1+\cdots+k=$.",
                   "The equality is missing its right-hand expression.",
                   r"$1+\cdots+k=\frac{k(k+1)}2$."),
            family("Summation identity",
                   r"$\forall n\ge1,\ 1+\cdots+n=\frac{n(n+1)}2$.",
                   "This is the standard arithmetic-series identity.",
                   r"$\forall n\ge1,\ 1+\cdots+n=\frac{n(n-1)}2$.",
                   "At $n=1$ the right side is zero.",
                   r"$1+\cdots+n=\frac{n(n+1)}2$.",
                   "The variable $n$ is free in this standalone formula.",
                   r"$\forall n\ge1,\ 1+\cdots+n=\frac{n(n+1)}2$."),
            family("Inequalities",
                   r"$2^n\ge n+1$ for every integer $n\ge0$.",
                   "The statement has a valid base and induction step.",
                   r"$2^n<n$ for every integer $n\ge1$.",
                   "The claim already fails at $n=1$.",
                   r"$2^n\ge$.", "The inequality is missing its right-hand expression.",
                   r"$2^n\ge n+1$."),
            family("Implication use",
                   r"From $P(k)$ and $P(k)\to P(k+1)$, one may infer $P(k+1)$.",
                   "This is modus ponens inside the induction proof.",
                   r"From $P(k+1)$ and $P(k)\to P(k+1)$, one may infer $P(k)$.",
                   "That is affirming the consequent.",
                   r"$P(k),\ P(k)\to\ \therefore P(k+1)$.",
                   "The conditional premise is incomplete.",
                   r"$P(k),\ P(k)\to P(k+1)\ \therefore P(k+1)$."),
            family("Circularity",
                   r"Assuming $P(k)$ is allowed while proving $P(k)\to P(k+1)$.",
                   "It is the antecedent of the conditional being proved.",
                   r"Assuming $P(k+1)$ is allowed while proving $P(k+1)$.",
                   "That assumes the desired next case.",
                   r"Assume $P(k+1)$ because.",
                   "The justification after because is missing.",
                   r"Assume $P(k)$ as the induction hypothesis."),
            family("Starting index",
                   r"A theorem stated for $n\ge4$ should begin its induction at $n=4$.",
                   "The base case must start where the theorem starts.",
                   r"A theorem stated for $n\ge4$ is proved by checking only $n=1$.",
                   "That base lies outside the claimed range.",
                   r"$n\ge$.", "The lower bound is missing.",
                   r"$n\ge4$."),
            family("Proposition/term",
                   r"$P(1)\lor\neg P(1)$.",
                   "Excluded middle makes this proposition true.",
                   r"$P(1)\land\neg P(1)$.",
                   "A proposition and its negation cannot both hold.",
                   r"$P(k)+1$.",
                   "Arithmetic addition is not defined for a proposition.",
                   r"$a_k+1$ or $P(k+1)$."),
        ),
    ),
    Core(
        "Counting",
        r"Let $X=\{a,b\}$, $Y=\{b,c,d\}$, $n=5$, and $r=2$. "
        r"For probability, a fair die has sample space "
        r"$\Omega=\{1,2,3,4,5,6\}$ with events $E=\{2,4,6\}$ and "
        r"$F=\{4,5,6\}$. Let $Z$ be the number shown.",
        (
            family("Sum rule",
                   "If two disjoint cases have $3$ and $4$ outcomes, together they have $7$ outcomes.",
                   "Disjoint alternatives are added.",
                   "If two disjoint cases have $3$ and $4$ outcomes, together they have $12$ outcomes.",
                   "Multiplication is for successive choices, not alternative cases.",
                   r"$3+=$.", "The sum and equality are incomplete.",
                   r"$3+4=7$."),
            family("Product rule",
                   "A two-stage process with $3$ choices and then $4$ choices has $12$ outcomes.",
                   "Successive independent choice counts multiply.",
                   "A two-stage process with $3$ choices and then $4$ choices has $7$ outcomes.",
                   "Seven would add alternatives rather than combine stages.",
                   r"$3\cdot$.", "Multiplication is missing its second factor.",
                   r"$3\cdot4=12$."),
            family("Inclusion-exclusion", r"$|X\cup Y|=4$.",
                   "The union is $\{a,b,c,d\}$.",
                   r"$|X\cup Y|=5$.", "The shared element $b$ must not be counted twice.",
                   r"$|X\cup|=4$.", "Union is missing its second set.",
                   r"$|X\cup Y|=4$."),
            family("Pigeonhole principle",
                   "Placing $7$ objects into $6$ boxes forces some box to receive at least two objects.",
                   "There are more objects than boxes.",
                   "Placing $6$ objects into $6$ boxes forces some box to receive at least two objects.",
                   "One object can be placed in each box.",
                   r"$7\to6\therefore$.", "The argument has no conclusion.",
                   r"$7$ objects in $6$ boxes $\therefore$ a repeated box."),
            family("Factorials", r"$5!=120$.", r"$5\cdot4\cdot3\cdot2\cdot1=120$.",
                   r"$5!=25$.", "Factorial is not repeated addition or squaring.",
                   r"$X!$.", "Factorial is not defined for the set $X$ under these conventions.",
                   r"$|X|!=2$."),
            family("Permutations", r"$P(5,2)=20$.",
                   r"There are $5\cdot4=20$ ordered selections.",
                   r"$P(5,2)=10$.", "Ten counts unordered selections.",
                   r"$P(5,)=20$.", "The number selected is missing.",
                   r"$P(5,2)=20$."),
            family("Combinations", r"$\binom52=10$.",
                   "There are ten unordered pairs from five objects.",
                   r"$\binom52=20$.", "Twenty counts ordered selections.",
                   r"$\binom{\,}{2}=10$.", "The population size is missing.",
                   r"$\binom52=10$."),
            family("Combinations", r"$\binom52=\binom53$.",
                   "Choosing two to include is equivalent to choosing three to exclude.",
                   r"$\binom52=\binom54$.", "The values are ten and five.",
                   r"$\binom5X=10$.", "The lower argument must be an integer, not the set $X$.",
                   r"$\binom52=10$."),
            family("Strings", r"There are $2^5=32$ bit strings of length $5$.",
                   "Each of five positions has two choices.",
                   r"There are $5!=120$ bit strings of length $5$.",
                   "Bits may repeat, so permutations are not the correct model.",
                   r"$2^{\Box}=32$.", "The box is an unfilled exponent placeholder, not a number.",
                   r"$2^5=32$."),
            family("Repetition",
                   "Five choices made twice with repetition produce $5^2=25$ sequences.",
                   "Each of the two positions has five choices.",
                   "Five choices made twice with repetition produce $P(5,2)$ sequences.",
                   "The permutation formula forbids repetition.",
                   r"$5^{\Box}$ sequences.", "The box is an unfilled sequence-length placeholder.",
                   r"$5^2$ sequences."),
            family("Repeated objects",
                   r"The word LEVEL has $\frac{5!}{2!\,2!}=30$ distinct arrangements.",
                   "The two Ls and two Es are indistinguishable within their groups.",
                   r"The word LEVEL has $5!=120$ distinct arrangements.",
                   "That count treats repeated letters as distinct.",
                   r"$\frac{5!}{2!\,}$.", "The denominator is incomplete.",
                   r"$\frac{5!}{2!\,2!}=30$."),
            family("Order",
                   r"Selecting a two-person committee from five people is counted by $\binom52$.",
                   "Committee membership is unordered.",
                   r"Assigning president and secretary from five people is counted by $\binom52$.",
                   "The offices make the selection ordered.",
                   r"committee$(5,)$.", "The requested committee size is missing.",
                   r"$\binom52$ committees."),
            family("Probability type", r"$E\subseteq\Omega$.",
                   "An event is a subset of the sample space.",
                   r"$7\in\Omega$.", "Seven is not a possible die outcome.",
                   r"$E\in 4$.", "Membership requires a set on the right.",
                   r"$4\in E$."),
            family("Classical probability", r"$\Pr(E)=\frac12$.",
                   "Three of six equally likely outcomes are even.",
                   r"$\Pr(E)=\frac13$.", "The favorable-to-total ratio is $3/6$.",
                   r"$\Pr(2)=\frac16$.",
                   "Probability is applied to events; the outcome should be written as a singleton event.",
                   r"$\Pr(\{2\})=\frac16$."),
            family("Complements", r"$\Pr(E^c)=1-\Pr(E)$.",
                   "An event and its complement partition the sample space.",
                   r"$\Pr(E^c)=\Pr(E)+1$.", "The complement rule subtracts from one.",
                   r"$\Pr({}^c)=1$.", "The event being complemented is missing.",
                   r"$\Pr(E^c)=1-\Pr(E)$."),
            family("Addition rule",
                   r"$\Pr(E\cup F)=\Pr(E)+\Pr(F)-\Pr(E\cap F)$.",
                   "The intersection corrects double counting.",
                   r"$\Pr(E\cup F)=\Pr(E)+\Pr(F)$.",
                   "The events overlap at outcomes four and six.",
                   r"$\Pr(E\cup)=1$.", "Union is missing its second event.",
                   r"$\Pr(E\cup F)$."),
            family("Disjointness", r"$\{1\}$ and $\{2\}$ are disjoint events.",
                   "Their intersection is empty.",
                   r"$E$ and $F$ are disjoint events.", "They share outcomes four and six.",
                   r"$E\cap$ is empty.", "Intersection is missing its second event.",
                   r"$E\cap F$ is nonempty."),
            family("Independence",
                   r"$\Pr(E\cap F)=\frac13$.",
                   "The intersection is $\{4,6\}$, two of six outcomes.",
                   r"$E$ and $F$ are independent.",
                   r"$\Pr(E\cap F)=1/3$ but $\Pr(E)\Pr(F)=1/4$.",
                   r"$\Pr(E)\Pr()=\Pr(E\cap F)$.",
                   "The second probability has no event argument.",
                   r"$\Pr(E)\Pr(F)=\Pr(E\cap F)$."),
            family("Conditional probability", r"$\Pr(E\mid F)=\frac23$.",
                   "Two of the three outcomes in $F$ are even.",
                   r"$\Pr(E\mid F)=\frac12$.", "Conditioning restricts the denominator to $F$.",
                   r"$\Pr(E\mid\varnothing)$.",
                   "Conditional probability is undefined when the conditioning event has probability zero.",
                   r"$\Pr(E\mid F)$."),
            family("Expected value", r"$\mathbb E[Z]=3.5$.",
                   "The mean of the six equally likely die values is $21/6$.",
                   r"$\mathbb E[Z]=3$.", "The arithmetic mean is three and one half.",
                   r"$\mathbb E[E]$.",
                   "The expectation operator is defined here for the random variable $Z$, not the event $E$.",
                   r"$\mathbb E[Z]$."),
        ),
    ),
)


def stable_rng(label: str) -> random.Random:
    digest = hashlib.sha256(f"comp2300-syntax-bank-v2:{label}".encode()).digest()
    return random.Random(int.from_bytes(digest[:16], "big"))


CORE_NOTATION_GUIDES: dict[str, str] = {
    "Logic": (
        r"$\neg p$: not $p$; $p\land q$: $p$ and $q$; $p\lor q$: $p$ or $q$; "
        r"$p\to q$: if $p$, then $q$; $p\leftrightarrow q$: $p$ exactly when $q$; "
        r"$\forall$: for every; $\exists$: there exists; $\therefore$: therefore."
    ),
    "Arguments": (
        r"$\neg$: not; $\land$: and; $\lor$: inclusive or; $p\to q$: if $p$, then $q$; "
        r"$\Gamma\models C$: $C$ follows from premises $\Gamma$; $\therefore$: therefore."
    ),
    "Sets": (
        r"$x\in A$: $x$ is an element of $A$; $A\subseteq B$: every $A$-element is in $B$; "
        r"$\cup$: in either set; $\cap$: in both; $A\setminus B$: in $A$ but not $B$; "
        r"$A^c$: outside $A$; $\mathcal P(A)$: the set of all subsets of $A$."
    ),
    "Proofs": (
        r"$\forall$: for every; $\exists$: there exists; $P\to Q$: if $P$, then $Q$; "
        r"$P\leftrightarrow Q$: both directions; a \emph{witness} proves an existential; "
        r"a \emph{counterexample} disproves a universal."
    ),
    "Divisibility": (
        r"$a\mid b$: $a$ divides $b$; $a\nmid b$: $a$ does not divide $b$; "
        r"$a\equiv b\pmod m$: $a$ and $b$ have the same remainder modulo $m$; "
        r"$\gcd(a,b)$: greatest common divisor; $(d_k\cdots d_0)_b$: a base-$b$ numeral."
    ),
    "Induction": (
        r"$P(k)$: the statement at index $k$; $P(k)\to P(k+1)$: the induction step; "
        r"$a_n$: the $n$th sequence term; $\sum$: add the indexed terms; "
        r"strong induction may use all earlier established cases."
    ),
    "Counting": (
        r"$n!$: factorial; $P(n,r)$: ordered selections; $\binom nr$: unordered selections; "
        r"$|X|$: size of $X$; $\Pr(E)$: probability of event $E$; $E^c$: not $E$; "
        r"$\Pr(E\mid F)$: probability of $E$ given $F$; $\mathbb E[Z]$: expected value."
    ),
}


CORE_STAGE_LABELS: dict[str, tuple[str, str, str, str]] = {
    "Logic": (
        "Build and read propositions",
        "Interpret connectives and equivalences",
        "Check predicates, types, and scope",
        "Read quantified claims and arguments",
    ),
    "Arguments": (
        "Recognize valid argument forms",
        "Separate validity, soundness, and consistency",
        "Read assumptions, flaws, and conditionals",
        "Test what the information supports",
    ),
    "Sets": (
        "Read membership, inclusion, and size",
        "Interpret set operations",
        "Read products and relations",
        "Read functions, variables, and types",
    ),
    "Proofs": (
        "Identify the proof strategy",
        "Read quantifiers, witnesses, and counterexamples",
        "Expand definitions inside proofs",
        "Audit proof language and logical structure",
    ),
    "Divisibility": (
        "Read divisibility from its definition",
        "Read gcd, quotients, and remainders",
        "Interpret modular congruence",
        "Read primes, bases, and place value",
    ),
    "Induction": (
        "Read the parts of an induction proof",
        "Track hypotheses and base coverage",
        "Read recurrences and closed forms",
        "Audit the algebra and proof logic",
    ),
    "Counting": (
        "Choose and read a counting rule",
        "Interpret counting notation and models",
        "Read events and probability rules",
        "Read dependence, conditioning, and expectation",
    ),
}


CORE_STAGE_CUES: dict[str, tuple[str, str, str, str]] = {
    "Logic": (
        "Locate every operator and all of its operands before assigning a truth value.",
        "Find the main connective first; then evaluate from the inside out.",
        "Check predicate arity, object types, and whether every variable is bound.",
        "Read quantifiers left to right, mark their scope, and separate premises from conclusions.",
    ),
    "Arguments": (
        "Separate the premises from the conclusion, then name the proposed inference pattern.",
        "Ask whether the premises could all be true while the conclusion is false.",
        "Identify exactly what the conclusion needs and what each premise actually supplies.",
        "Use only the stated information; distinguish support from proof and relevance from truth.",
    ),
    "Sets": (
        "Name the object on each side and distinguish membership from subset inclusion.",
        "Translate each operation into an element-by-element condition before computing.",
        "Check the type of every object: element, ordered pair, set, or relation.",
        "Bind every variable and distinguish a function value from a claim about the function.",
    ),
    "Proofs": (
        "State what may be assumed and what must be shown for the named strategy.",
        "Match universal claims with arbitrary objects and existential claims with witnesses.",
        "Expand the relevant definition before deciding whether a displayed line proves anything.",
        "Separate established facts from goals, conjectures, and incomplete proof language.",
    ),
    "Divisibility": (
        "Read $a\\mid b$ as an existential equation: $b=ak$ for some integer $k$.",
        "Identify the divisor, quotient, remainder, and required bounds before judging.",
        "Translate congruence into divisibility of a difference before using a law.",
        "Check domains, legal digits, and place values before performing arithmetic.",
    ),
    "Induction": (
        "Label the base case, hypothesis, and step; keep assumptions separate from goals.",
        "Track exactly which earlier cases are available and which starting cases are required.",
        "Substitute an index explicitly before comparing a recurrence with a closed form.",
        "Check the claimed range and verify that each algebraic line follows from the hypothesis.",
    ),
    "Counting": (
        "Decide whether stages are combined by addition or multiplication before calculating.",
        "Ask whether order and repetition matter, then match the notation to that model.",
        "Identify the sample space and event type before applying a probability rule.",
        "Check conditioning, dependence, and the type of the object inside each operator.",
    ),
}


def max_answer_run(answers: list[str]) -> int:
    best = current = 0
    previous = None
    for answer in answers:
        if answer == previous:
            current += 1
        else:
            previous = answer
            current = 1
        best = max(best, current)
    return best


def base_answer_sequence(core: Core) -> list[str]:
    """Return a balanced, non-patterned answer sequence for ordered families."""
    answers = list("T" * 6 + "F" * 7 + "N" * 7)
    rng = stable_rng(f"{core.name}:ordered-answer-sequence")
    for _ in range(1000):
        rng.shuffle(answers)
        if max_answer_run(answers) <= 2:
            return answers
    raise RuntimeError(f"Could not construct answer sequence for {core.name}")


def form_items(core: Core, form_index: int) -> list[tuple[int, Family, Version]]:
    labels = ("T", "F", "N")
    base_answers = base_answer_sequence(core)
    items = []
    for family_index, (item_family, base_answer) in enumerate(
        zip(core.families, base_answers), start=1
    ):
        answer = labels[(labels.index(base_answer) + form_index) % 3]
        items.append((family_index, item_family, item_family.versions[answer]))
    return items


PREAMBLE = r"""\documentclass[9pt]{extarticle}

% Generated by generate_core_syntax_bank.py. Edit the generator, not this file.
\usepackage[letterpaper,margin=0.55in,includehead,includefoot,
  headheight=15pt,headsep=6pt,footskip=18pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage{multicol}
\usepackage{fancyhdr}
\usepackage[hidelinks]{hyperref}

\definecolor{CoreNavy}{HTML}{18364A}
\definecolor{CoreTeal}{HTML}{176B6B}
\definecolor{CoreTint}{HTML}{EDF4F8}

\newif\ifanswers
\ifdefined\MAKEANSWERKEY
  \answerstrue
\else
  \answersfalse
\fi

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\columnsep}{0.25in}
\setlength{\columnseprule}{0.25pt}
\setlength{\emergencystretch}{1.2em}
\raggedbottom

\newcommand{\currentcore}{Core Practice}
\newcommand{\currentform}{}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textbf{COMP 2300}}
\fancyhead[C]{\textbf{\ifanswers Instructor Key\else Read --- Parse --- Judge\fi}}
\fancyhead[R]{\currentform}
\fancyfoot[L]{\ifanswers Answers, diagnoses, and minimal repairs\else Read it; parse it; then judge it.\fi}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{20 items}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.3pt}

\newcounter{tfitem}
\newcommand{\CoreForm}[5]{%
  \clearpage
  \renewcommand{\currentcore}{#1 Core}%
  \renewcommand{\currentform}{Form #2}%
  \setcounter{tfitem}{0}%
  {\color{CoreNavy}\Large\bfseries #1 Core: Reading \& Interpreting --- Form #2}\par
  \vspace{2pt}\color{CoreNavy}\rule{\linewidth}{0.8pt}\color{black}\par
  \vspace{3pt}
  \ifanswers\else
    \textbf{Name:} \rule{0.42\linewidth}{0.4pt}\hfill
    \textbf{Date:} \rule{0.22\linewidth}{0.4pt}\par
    \vspace{4pt}
  \fi
  \fcolorbox{CoreTeal}{CoreTint}{\parbox{0.965\linewidth}{%
    \ifanswers\scriptsize\else\footnotesize\fi
    \textbf{Given.} #3\par
    \vspace{2pt}
    \textbf{Say the symbols as words.} #4\par
    \vspace{2pt}
    \textbf{For every item:} (1) say the whole statement in words; (2) lightly
    box its main relation, connective, or claim and mark its inputs or scope;
    (3) check whether it is complete and well formed here; (4) only then apply
    the definitions and circle an answer. \textbf{Decision key: N} = not a
    truth-evaluable proposition as written (incomplete, undefined, free
    variable, type error, or arity error); \textbf{T/F} = a complete proposition
    that is true/false. \textbf{N is not F. Do not circle before you parse.}}}
  \vspace{5pt}
  \begin{multicols}{2}
  \raggedcolumns
  #5
  \end{multicols}
}

\newcommand{\StageHeader}[2]{%
  \par\noindent
  {\color{CoreNavy}\footnotesize\bfseries #1}\par\nopagebreak
  {\color{CoreTeal}\scriptsize\itshape Reading lens: #2}\par\nopagebreak
  \vspace{1.5pt}
}

\newcommand{\StudentItem}[1]{%
  \stepcounter{tfitem}%
  \par\noindent
  \hangindent=3.25em\hangafter=1
  \makebox[1.65em][r]{\textbf{\thetfitem.}}\hspace{0.25em}%
  \makebox[1.25em][c]{\textbf{T}}\hspace{0.10em}%
  \makebox[1.25em][c]{\textbf{F}}\hspace{0.10em}%
  \makebox[1.25em][c]{\textbf{N}}\hspace{0.30em}%
  #1%
  \par\vspace{5.5pt}
}

\newcommand{\KeyItem}[5]{%
  \stepcounter{tfitem}%
  \par\noindent
  \hangindent=3.25em\hangafter=1
  \makebox[1.65em][r]{\textbf{\thetfitem.}}\hspace{0.25em}%
  \makebox[1.25em][c]{\textbf{T}}\hspace{0.10em}%
  \makebox[1.25em][c]{\textbf{F}}\hspace{0.10em}%
  \makebox[1.25em][c]{\textbf{N}}\hspace{0.30em}%
  #5%
  \par\nobreak
  {\scriptsize\color{CoreTeal}\hspace*{3.25em}%
    \textbf{[#1 --- #2]} #3%
    \if\relax\detokenize{#4}\relax\else\
      \textit{Minimal repair:} #4%
    \fi
  }\par
}

\begin{document}
\ifanswers\small\else\fontsize{10.8}{13.0}\selectfont\fi
"""


def tex_student_item(version: Version) -> str:
    """Render a student item without embedding its answer or explanation."""
    return rf"\StudentItem{{{version.body}}}"


def tex_key_item(
    family_index: int, item_family: Family, version: Version
) -> str:
    return (
        rf"\KeyItem{{{version.answer}}}{{F{family_index:02d}: {item_family.category}}}"
        rf"{{{version.explanation}}}{{{version.repair}}}{{{version.body}}}"
    )


def tex_form_body(
    core: Core,
    items: list[tuple[int, Family, Version]],
    *,
    instructor_key: bool,
) -> str:
    """Render four five-item reading stages, split cleanly across two columns."""
    stage_labels = CORE_STAGE_LABELS[core.name]
    stage_cues = CORE_STAGE_CUES[core.name]
    lines: list[str] = []
    for position, (family_index, item_family, version) in enumerate(items, start=1):
        if position in (1, 6, 11, 16):
            if position == 11:
                lines.append(r"\columnbreak")
            stage_index = (position - 1) // 5
            lines.append(
                rf"\StageHeader{{{stage_index + 1}. {stage_labels[stage_index]}}}"
                rf"{{{stage_cues[stage_index]}}}"
            )
        if instructor_key:
            lines.append(tex_key_item(family_index, item_family, version))
        else:
            lines.append(tex_student_item(version))
    return "\n".join(lines)


def validate() -> None:
    if len(CORES) != 7:
        raise RuntimeError(f"Expected seven Cores, found {len(CORES)}")
    core_names = {core.name for core in CORES}
    if set(CORE_NOTATION_GUIDES) != core_names:
        raise RuntimeError("Notation guides do not match the seven Cores")
    if set(CORE_STAGE_LABELS) != core_names:
        raise RuntimeError("Stage labels do not match the seven Cores")
    if set(CORE_STAGE_CUES) != core_names:
        raise RuntimeError("Stage cues do not match the seven Cores")
    for core in CORES:
        if len(core.families) != 20:
            raise RuntimeError(f"{core.name} has {len(core.families)} families, not 20")
        seen = set()
        totals: Counter[str] = Counter()
        for family_index, item_family in enumerate(core.families, start=1):
            if set(item_family.versions) != {"T", "F", "N"}:
                raise RuntimeError(
                    f"{core.name} family {family_index}: expected T/F/N versions"
                )
            for version in item_family.versions.values():
                fields = (version.body, version.explanation, version.repair)
                if any(any(ord(char) < 32 for char in field) for field in fields):
                    raise RuntimeError(
                        f"{core.name} family {family_index}: control character in source"
                    )
                if version.answer == "N" and not version.repair:
                    raise RuntimeError(
                        f"{core.name} family {family_index}: N version lacks a repair"
                    )
        for form_index in range(3):
            items = form_items(core, form_index)
            if [family_index for family_index, _, _ in items] != list(range(1, 21)):
                raise RuntimeError(f"{core.name} form {form_index}: families out of order")
            counts = Counter(version.answer for _, _, version in items)
            if sorted(counts.values()) != [6, 7, 7]:
                raise RuntimeError(f"{core.name} form {form_index}: unbalanced {counts}")
            if max_answer_run([version.answer for _, _, version in items]) > 2:
                raise RuntimeError(f"{core.name} form {form_index}: long answer run")
            totals.update(counts)
            for _, _, version in items:
                if version.body in seen:
                    raise RuntimeError(f"{core.name}: duplicate body {version.body}")
                seen.add(version.body)
        if totals != Counter({"T": 20, "F": 20, "N": 20}):
            raise RuntimeError(f"{core.name}: incorrect full-bank balance {totals}")


def write_tex() -> None:
    validate()
    student_lines = [
        "% STUDENT-SAFE SOURCE: this file contains no answer labels or explanations.\n"
        "% Generated by generate_core_syntax_bank.py. Edit the generator, not this file.\n"
        + PREAMBLE
    ]
    key_lines = [
        "% INSTRUCTOR-ONLY ANSWER KEY: do not distribute or publish with student materials.\n"
        "% Generated by generate_core_syntax_bank.py. Edit the generator, not this file.\n"
        "\\def\\MAKEANSWERKEY{1}\n"
        + PREAMBLE
    ]
    form_names = ("A", "B", "C")
    for core in CORES:
        for form_index, form_name in enumerate(form_names):
            items = form_items(core, form_index)
            student_body = tex_form_body(core, items, instructor_key=False)
            key_body = tex_form_body(core, items, instructor_key=True)
            notation_guide = CORE_NOTATION_GUIDES[core.name]
            student_lines.append(
                rf"\CoreForm{{{core.name}}}{{{form_name}}}"
                rf"{{{core.context}}}{{{notation_guide}}}{{"
                + "\n" + student_body + "\n}"
            )
            key_lines.append(
                rf"\CoreForm{{{core.name}}}{{{form_name}}}"
                rf"{{{core.context}}}{{{notation_guide}}}{{"
                + "\n" + key_body + "\n}"
            )
    student_lines.append("\n\\end{document}\n")
    key_lines.append("\n\\end{document}\n")
    STUDENT_TEX.write_text("\n".join(student_lines))
    KEY_TEX.write_text("\n".join(key_lines))


if __name__ == "__main__":
    write_tex()
    print(f"Wrote {STUDENT_TEX}")
    print(f"Wrote {KEY_TEX}")
