## Path Sum: Three Ways

[<font color='gray'>Problem 82</font>](https://projecteuler.net/problem=82 "Click to jump")

### Description

<p class="small_notice">NOTE: This problem is a more challenging version of <a href="problem=81">Problem 81</a>.</p>

The minimal path sum in the $5$ by $5$ matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and **only moving up, down, and right**, is indicated in red and bold; the sum is equal to $994$.

$$
\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & 746 & 422 & 111\\
537 & 699 & 497 & 121 & 956\\
805 & 732 & 524 & 37 & 331
\end{pmatrix}
$$

Find the minimal path sum from the left column to the right column in <a href="resources/documents/0082_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.

### Analysis and Solution

This problem shares conceptual similarities with the [Problem 81](https://projecteuler.net/problem=81) (Path Sum: Two Ways), and therefore we can adapt its dynamic programming methodology to optimize our solution. The transition equation is

$$\begin{aligned}
dp_{i,j} = \begin{cases}
grid_{i,j}&j=0\\
grid_{i,j}+\min\{dp_{i-1,j},dp_{i,j-1},dp_{i,j+1}\} &j>0
\end{cases}
\end{aligned}$$

```python
import numpy as np


def min_path_sum(grid):
    
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = grid[i][0]


    for j in range(1, n):
        for i in range(m):
            if dp[i][j-1] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i][j-1] + grid[i][j]

            if i > 0 and dp[i-1][j] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
        

        for i in range(m-1, -1, -1):
            if i < m-1 and dp[i+1][j] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i+1][j] + grid[i][j]
    
    return min(row[-1] for row in dp)

arr = np.loadtxt('0082_matrix.txt', delimiter=',')

print(min_path_sum(arr))
```

The result is `260324`.