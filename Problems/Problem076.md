## Largest Exponential

[<font color='gray'>Problem 76</font>](https://projecteuler.net/problem76 "Click to jump")

### Description

It is possible to write five as a sum in exactly six different ways:

$$
\begin{aligned}
&4 + 1\\
&3 + 2\\
&3 + 1 + 1\\
&2 + 2 + 1\\
&2 + 1 + 1 + 1\\
&1 + 1 + 1 + 1 + 1
\end{aligned}
$$

How many different ways can one hundred be written as a sum of at least two positive integers?

### Analysis and Description

Obviously, we need to perform the dynamic programming, and the problem is how to build the transition equition?

It will not be easy to construct a relation between $dp_n$ and $dp_{n-1}$ becasue $n=(n-k)+k$ should not be forgot. The problem is complex because not only $n$ can be separated, but also $k$ for $1\le k\lt n$. In order to consider all situations, limit the max addend $k$ and consider each case, then increase $k$ gradually.

Take $5$ as an example.

1. When `k=1`, `dp[1] = dp[2] =...= dp[5] = 1`
2. When `k=2`, `dp[2] += dp[2-2] = 2`
`dp[3] += dp[3-2] = 2`
`dp[4] += dp[4-2] = 3`
`dp[5] += dp[5-2] = 3`
3. When `k=3`, `dp[3] += dp[3-3] = 3`
`dp[4] += dp[4-3] = 4`
`dp[5] += dp[5-3] = 5`
4. When `k=4`,`dp[4] += dp[4-4] = 5`
`dp[5] += dp[5-4] = 6`
5. When `k=5`, `dp[5] += dp[5-5] = 7`

And minus one to abandon the case $5+0$, and we have there are $6$ ways for $5$.

Then we have a workable transition equation

$$
dp_n = dp_n+dp_{n-i}
$$

Be careful that the transition equation should be updated while $n$ increasing. So the program should have a nested for loop.

```python 
def count_partitions(n:int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1
    for j in range(1, n+1):
        for i in range(j, n+1):
            dp[i] += dp[i - j]
    return dp[n] - 1

print(count_partitions(100))
```

And the result is `190569291`.