## Summation of Primes

[<font color='gray'>Problem 10</font>](https://projecteuler.net/problem=10 "Click to jump")

### Description

The sum of the primes below $10$ is $2+3+5+7=17$.

Find the sum of all the primes below two million.

### Analysis and Solution

A common idea is to perform a foor-loop from 2 to the end and judge whether the number is prime. But it will be inefficient while limit a boundary. Here, we perform sieve of Eratosthenes algorithm to get all primes first, and add them.

```python
def sieve_eratosthenes(n :int):
    if n < 2:
        return []
    primes = [2] if n >= 2 else []
    if n < 3:
        return primes
    # Calculate the size of the sieve for odd numbers starting from 3
    m = (n - 3) // 2 + 1
    sieve = [True] * m
    # Iterate over each odd number (represented by their index)
    for i in range(m):
        current_p = 3 + 2 * i
        if current_p * current_p > n:
            break
        if sieve[i]:
            # Mark multiples starting from current_p^2, stepping by 2*current_p
            start = current_p * current_p
            step = 2 * current_p
            for j in range(start, n + 1, step):
                idx = (j - 3) // 2
                if idx < m:
                    sieve[idx] = False
    # Collect the primes
    primes += [3 + 2 * i for i in range(m) if sieve[i] and (3 + 2 * i) <= n]
    return primes

print(sum(sieve_eratosthenes(2*10**6)))
```

And the result is `142913828922`.