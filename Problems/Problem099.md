## Largest Exponential

[<font color='gray'>Problem 99</font>](https://projecteuler.net/problem=99 "Click to jump")

### Description

Comparing two numbers written in index form like $2^{11}$ and $3^7$ is not difficult, as any calculator would confirm that $2^{11} = 2048 \lt 3^7 = 2187$.

However, confirming that $632382^{518061} \gt 519432^{525806}$ would be much more difficult, as both numbers contain over three million digits.

Using <a href="resources/documents/0099_base_exp.txt">base_exp.txt</a> (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

### Analysis and Solution

Notice that logarithmic functions are monotonic, which suggest that we can compare $b\lg a$ instead of $a^b$.

```python
import numpy as np


arr = np.loadtxt('0099_base_exp.txt', delimiter=',')

arr[:,0] = np.log(arr[:,0])
prod_row = np.prod(arr, axis=1)

max_serial = 0

for i in range(1, len(prod_row)):
    if prod_row[i] > prod_row[max_serial]:
        max_serial = i

print(max_serial+1)
```

And the result is `709`.