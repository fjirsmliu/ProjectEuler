## Sieve of Eratosthenes

[Wikipeida](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.

To find all the prime numbers less than or equal to a given integer $n$ by Eratosthenes' method:

1. Create a list of consecutive integers from $2$ through $n: (2, 3, 4, ..., n)$.
2. Initially, let $p$ equal $2$, the smallest prime number.
3. Enumerate the multiples of $p$ by counting in increments of $p$ from $2p$ to $n$, and mark them in the list (these will be $2p, 3p, 4p, \cdots$; the $p$ itself should not be marked).
4. Find the smallest number in the list greater than $p$ that is not marked. If there was no such number, stop. Otherwise, let $p$ now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below $n$.

The main idea here is that every value given to $p$ will be prime, because if it were composite it would be marked as a multiple of some other, smaller prime. Note that some of the numbers may be marked more than once (e.g., $15$ will be marked both for $3$ and $5$).

- As a refinement, it is sufficient to mark the numbers in step 3 starting from $p^2$, as all the smaller multiples of $p$ will have already been marked at that point. This means that the algorithm is allowed to terminate in step 4 when $p^2$ is greater than $n$.
- Another refinement is to initially list **odd numbers only**, $(3, 5, ..., n)$, and count in increments of $2p$ in step 3, thus marking only odd multiples of $p$. This actually appears in the original algorithm. This can be generalized with wheel factorization, forming the initial list only from numbers coprime with the first few primes and not just from odds (i.e., numbers coprime with $2$), and counting in the correspondingly adjusted increments so that only such multiples of $p$ are generated that are coprime with those small primes, in the first place.

### Pseudocode

```
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.
```

The time complexity of this algorithm is $\Theta(n\log\log n)$.

### Program

```python
def sieve_eratosthenes(n:int):
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

```