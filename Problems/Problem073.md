## Counting Fractions in a Range

[<font color='gray'>Problem 73</font>](https://projecteuler.net/problem=73 "Click to jump")

### Description

Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\gcd(n, d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:

$$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \mathbf{\frac 3 8, \frac 2 5, \frac 3 7}, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$

It can be seen that there are $3$ fractions between $\dfrac 1 3$ and $\dfrac 1 2$.

How many fractions lie between $\dfrac 1 3$ and $\dfrac 1 2$ in the sorted set of reduced proper fractions for $d \le 12\,000$?

### Analysis and Solution

For a fixed positive integer $d$, identify all positive integers $n$ that satisfy both of the following conditions:

1. $\gcd(n, d) = 1 $
2. $ \frac{1}{3} < \frac{n}{d} < \frac{1}{2} $, i.e. $\frac{d}{3}<n<\frac{d}{2}$

Then we have

```python
import math

def get_number_of_valid_n(d: int) -> int:
    return len([n for n in range(d//3 + 1, ((d+1)//2)) if math.gcd(n, d) == 1])
```

Finally, perform the linear search from $2$ through $12000$

```python
def find_number_of_fractions(target:int) -> int:
    count = 0

    for i in range(2, target+1):
        count += get_number_of_valid_n(i)

    return count

print(find_number_of_fractions(12000))
```

The result is `7295372`.
