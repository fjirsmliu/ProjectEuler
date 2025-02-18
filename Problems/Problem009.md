## Special Pythagorean Triplet

[<font color='gray'>Problem 9</font>](https://projecteuler.net/problem=9 "Click to jump")

### Description

A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,

$$a^2 + b^2 = c^2.$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. Find the product $abc$.

### Analysis and Solution

Notice that

$$
(m^2-n^2)^2+(2mn)^2=(m^2+n^2)^2
$$

Then

$$\begin{aligned}
a+b+c=&k(m^2-n^2+2mn+m^2+n^2)\\
=&2km(m+n)=2\times2^2\times5^3
\end{aligned}$$

Notice that $m+n>m$, then consider factors less than $\sqrt{500}\simeq22.4$. So verify $m$ in $\{2,4,5,10,20\}$. It's easy to find that when $m=20$, $n=5$, then we have

$$\begin{aligned}
abc=&2mn(m^4-n^4)=2\times2^2\times5^2\times(20^4-5^4)\\
=&2^3\times5^6\times(2^8-1)=31875000
\end{aligned}$$