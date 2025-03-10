## Triangular, Pentagonal, and Hexagonal

[<font color='gray'>Problem 45</font>](https://projecteuler.net/problem=45 "Click to jump")

### Description

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

$$\begin{aligned}
\text{Triangle}: T_n&=n(n+1)/2 &1, 3, 6, 10, 15, \dots\\
\text{Pentagonal}: P_n&=n(3n-1)/2 &1, 5, 12, 22, 35, \dots\\
\text{Hexagonal}: H_n&=n(2n-1) &1, 6, 15, 28, 45, \dots
\end{aligned}$$

It can be verified that $T_{285} = P_{165} = H_{143} = 40755$.

Find the next triangle number that is also pentagonal and hexagonal.

### Analysis and Solution

While $T_a=P_b=H_c$, it means that

$$ \frac{a(a+1)}{2}=\frac{b(3b-1)}{2}=c(2c-1) $$

Also,

$$ a(a+1) = b(3b-1) = 2c(2c-1) $$

Now, we can verify whether $b(3b-1)$ can be formed by $a(a+1)$ and $a$ should be ODD since $a+1=2c$.

```python
from math import sqrt

def is_triangle(b:int) -> bool:
    
    m = int(sqrt(n:=b*(3*b-1)))

    if m*(m+1) == n and (m&1!=0):
        return True
    else:
        return False

b = 166

while not(is_triangle(b)):
    b += 1

print(b, b*(3*b-1)//2)
```

The output is `31977 1533776805`, so we find that the result is $P_{31977}=1533776805$.
