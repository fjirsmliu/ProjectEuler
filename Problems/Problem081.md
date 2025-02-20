## Path Sum: Two Ways

[<font color='gray'>Problem 81</font>](https://projecteuler.net/problem=81 "Click to jump")

### Description

In the $5$ by $5$ matrix below, the minimal path sum from the top left to the bottom right, by **only moving to the right and down**, is indicated in bold red and is equal to $2427$.
<div class="center">

$$
\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum from the top left to the bottom right by only moving right and down in <a href="resources/documents/0081_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.

### Analysis and Solution

We don't need complex algorithm, just perform dynamic programming. And define `dp[i][j]` as the minimum path sum from `grid[0][0]` to `grid[i][j]`, and we have transition equition

$$dp_{i,j} = grid_{i,j}+\min\{dp_{i-1,j},dp_{i,j-1}\}$$

And we should get `dp[i][0]` and `dp[0][j]` first, then we can perform the transition equition

```python
import numpy as np


def min_path_sum(grid):

    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]


    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]

arr = np.loadtxt('0081_matrix.txt', delimiter=',')

print(min_path_sum(arr))
```

And the result is `427337`.