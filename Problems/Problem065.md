## Convergents of e

[<font color='gray'>Problem 65</font>](https://projecteuler.net/problem=65 "Click to jump")

### Description

The square root of $2$ can be written as an infinite continued fraction.

$\sqrt{2} = 1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + ...}}}}$

The infinite continued fraction can be written, $\sqrt{2} = [1; (2)]$, $(2)$ indicates that $2$ repeats <i>ad infinitum</i>. In a similar way, $\sqrt{23} = [4; (1, 3, 1, 8)]$.
It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for $\sqrt{2}$.

$$\begin{aligned}
&1 + \dfrac{1}{2} = \dfrac{3}{2} \\
&1 + \dfrac{1}{2 + \dfrac{1}{2}} = \dfrac{7}{5}\\
&1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}} = \dfrac{17}{12}\\
&1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}}} = \dfrac{41}{29}
\end{aligned}$$

Hence the sequence of the first ten convergents for $\sqrt{2}$ are:

$1, \dfrac{3}{2}, \dfrac{7}{5}, \dfrac{17}{12}, \dfrac{41}{29}, \dfrac{99}{70}, \dfrac{239}{169}, \dfrac{577}{408}, \dfrac{1393}{985}, \dfrac{3363}{2378}, ...$

What is most surprising is that the important mathematical constant,$e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...]$.

The first ten terms in the sequence of convergents for $e$ are:

$2, 3, \dfrac{8}{3}, \dfrac{11}{4}, \dfrac{19}{7}, \dfrac{87}{32}, \dfrac{106}{39}, \dfrac{193}{71}, \dfrac{1264}{465}, \dfrac{1457}{536}, ...$

The sum of digits in the numerator of the $10$<sup>th</sup> convergent is $1 + 4 + 5 + 7 = 17$.

Find the sum of digits in the numerator of the $100$<sup>th</sup> convergent of the continued fraction for $e$.

### Analysis and Solution

Here we need a useful lemma from [Wikipedia](https://en.wikipedia.org/wiki/Simple_continued_fraction#Infinite_continued_fractions_and_convergents), that is for an infinite continued fractions $[a_0;a_1,a_2,\cdots]$ and $[a_0;a_1,a_2,\cdots,a_n]=\dfrac{h_n}{k_n}$,

$$\begin{aligned}
h_n =& a_nh_{n-1} + h_{n-2}\\
k_n =& a_nk_{n-1} + k_{n-2}
\end{aligned}$$

Here I will give a proof using [mathmatical induction](https://en.wikipedia.org/wiki/Mathematical_induction)

**<font face= 'Times New Roman' size='4'> Proof </font>**

$$\begin{aligned}
[a_0;a_1,a_2,a_3] =& a_0 + \dfrac{1}{a_1 + \dfrac{1}{a_2 + \dfrac{1}{a_3}}}\\
=& a_0 + \dfrac{1}{a_1 + \dfrac{a_3}{a_2a_3+1}}\\
=& a_0 + \dfrac{a_2a_3+1}{a_1a_2a_3+a_1+a_3}\\
=& \dfrac{a_0a_1a_2a_3+a_0a_1+a_0a_3+a_2a_3+1}{a_3(a_1a_2+1)+a_1}\\
=& \dfrac{a_3(a_2(a_1a_0+1)+a_0)+(a_1a_0+1)}{a_3(a_2a_1+1)+a_1}
\end{aligned}$$

with

$$
h_2 = a_2(a_1a_0+1), k_2 = a_2a_1+1
$$

and

$$
h_1 = a_1a_0+1, k_1=a_1
$$

Assuming that the lemma holds for $n=k$, and when $n=k+1$,

$$\begin{aligned}
[a_0;a_1,\cdots,a_k,a_{k+1}]=&[a_0;a_1,\cdots,\dfrac{a_{k+1}a_k+1}{a_{k+1}}]\\
=&\dfrac{\dfrac{a_{k+1}a_k+1}{a_{k+1}}h_{k-1}+h_{k-2}}{\dfrac{a_{k+1}a_k+1}{a_{k+1}}k_{k-1}+k_{k-2}}
\end{aligned}$$

Then

$$\begin{aligned}
h_{k+1} =& (a_{k+1}a_k+1)h_{k-1} + a_{k+1}h_{k-2}\\
=& a_{k+1}(a_kh_{k-1} + h_{k-2})+h_{k-1}\\
=& a_{k+1}h_k + h_{k-1}
\end{aligned}$$

Similarily, we have $k_{k+1} = a_{k+1}k_k + k_{k-1}$

**<font face= 'Times New Roman' size='4'> Q.E.D. </font>**

Then for $\mathrm{e} = [2;1,2,1,1,4,1,\cdots,1,2k,1,\cdots]$, it can be easy to get

$$
a_n = \begin{cases}
1&n+1\neq0(\mathrm{mod} 3)\\
2k&n+1=3k
\end{cases}
$$

Initial conditions $h_1 = 3, h_2 = 8$ and $k_1 = 1, k_2=3$

```python
def a(n: int) -> int:
    if (n+1)%3 == 0:
        return (n+1)*2//3
    else:
        return 1
    
def h(n: int) -> int:
    if n == 1:
        return 3
    elif n == 2:
        return 8
    else:
        return a(n)*h(n-1) + h(n-2)

def k(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return a(n)*k(n-1) + k(n-2)

print(h(99))
```

Unfortunately, the program cost too much time. It seems that recursion cost too much while n is huge such as 99. Then we try to modify our definition of `h(n)`:

```python
def modified_h(n: int) -> int:
    if n == 1:
        return 3
    elif n == 2:
        return 8
    h_prev_prev, h_prev = 3, 8
    for i in range(3, n + 1):
        a_i = a(i)
        h_current = a_i * h_prev + h_prev_prev
        h_prev_prev, h_prev = h_prev, h_current
    return h_prev
```

Using dynamic processing, we update the `h_prev_prev` and `h_prev` for each `i`, and release the memory.

```python
print(sum(int(d) for d in str(modified_h(99))))
```

The result is 272.
