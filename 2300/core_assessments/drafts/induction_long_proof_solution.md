# Induction Core — Long-Proof Version Solution

> Private comparison draft. Do not publish or link for students unless this version is selected.

## (a) Pascal's identity

Starting from the right-hand side and using the factorial definition,

\[
\begin{aligned}
\binom{n-1}{k-1}+\binom{n-1}{k}
&=\frac{(n-1)!}{(k-1)!(n-k)!}
  +\frac{(n-1)!}{k!(n-k-1)!}\\
&=\frac{k(n-1)!}{k!(n-k)!}
  +\frac{(n-k)(n-1)!}{k!(n-k)!}\\
&=\frac{[k+(n-k)](n-1)!}{k!(n-k)!}\\
&=\frac{n!}{k!(n-k)!}\\
&=\binom{n}{k}.
\end{aligned}
\]

Thus

\[
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}.
\]

## (b) The binomial-sum identity

Let

\[
P(n):\qquad \sum_{k=0}^{n}\binom{n}{k}=2^n.
\]

**Base case.** When \(n=0\),

\[
\sum_{k=0}^{0}\binom{0}{k}=\binom00=1=2^0.
\]

**Induction hypothesis.** Fix \(m\ge0\) and assume

\[
\sum_{k=0}^{m}\binom{m}{k}=2^m.
\]

**Induction step.** Using the two endpoint terms separately and Pascal's
identity on the interior terms,

\[
\begin{aligned}
\sum_{k=0}^{m+1}\binom{m+1}{k}
&=\binom{m+1}{0}
  +\sum_{k=1}^{m}\binom{m+1}{k}
  +\binom{m+1}{m+1}\\
&=1+\sum_{k=1}^{m}
  \left(\binom{m}{k-1}+\binom{m}{k}\right)+1\\
&=\sum_{j=0}^{m}\binom{m}{j}
  +\sum_{k=0}^{m}\binom{m}{k}\\
&=2^m+2^m\\
&=2^{m+1}.
\end{aligned}
\]

In the third line, the first interior sum was reindexed with \(j=k-1\),
and the two endpoint terms complete the ranges. Therefore \(P(m+1)\) follows
from \(P(m)\). By mathematical induction, the identity holds for every
integer \(n\ge0\).
