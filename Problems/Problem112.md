## Bouncy Numbers

[<font color='gray'>Problem 112</font>](https://projecteuler.net/problem=112 "Click to jump")

### Description

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, $134468$.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, $66420$.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, $155349$.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand ($525$) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches $50\%$ is $538$.

Surprisingly, bouncy numbers become more and more common and by the time we reach $21780$ the proportion of bouncy numbers is equal to $90\%$.

Find the least number for which the proportion of bouncy numbers is exactly $99\%$.

### Analysis and Solution

A practical approach is to iteratively determine whether numbers are bouncy while tracking the proportional growth at each step. The initial step is to create a function that determines if a number is bouncy.

```python
def is_bouncy(n: int) -> bool:
    s = str(n)
    
    if len(s) < 3:
        return False
    
    digits = [int(c) for c in s]
    has_increasing = False
    has_decreasing = False
    
    for i in range(1, len(digits)):
        prev, curr = digits[i-1], digits[i]
        
        if curr > prev:
            has_increasing = True
        elif curr < prev:
            has_decreasing = True
        
        if has_increasing and has_decreasing:
            return True
    
    return False
```

To determine the least number where the bouncy number proportion reaches a specified threshold, the function should accept a target percentage as input and return the corresponding integer. Given that the bouncy ratio monotonically increases, we can sequentially iterate through numbers using a linear search approach.

```python
def find_the_least_number(target_ratio:float) -> int:

    bouncy_count = 0
    number = 0
    
    while True:
        number += 1
        if is_bouncy(number):
            bouncy_count += 1
            
        current_ratio = bouncy_count / number
        
        if abs(current_ratio - target_ratio) < 1e-9 or current_ratio > target_ratio:
            return number

print(find_the_least_number(0.99))
```

The result is `1587000`.