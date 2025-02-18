## Sum Square Difference

[<font color='gray'>Problem 6</font>](https://projecteuler.net/problem=6 "Click to jump")

### Description

The sum of the squares of the first ten natural numbers is,

$$1^2 + 2^2 + ... + 10^2 = 385.$$

The square of the sum of the first ten natural numbers is,

$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

### Analysis and Solution

Notice that

$$
\left(\sum k\right)^2-\sum k^2=\sum k^2+\sum_{m\ne n} mn-\sum k^2
$$

Then we have

```python
import itertools

prod = 0
for i,j in itertools.product(range(1, 101), repeat=2):
    if i!=j:
        prod += i*j

print(prod)
```

Result is `25164150`