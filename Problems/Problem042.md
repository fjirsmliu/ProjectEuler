## Coded Triangle Numbers

[<font color='gray'>Problem 42</font>](https://projecteuler.net/problem=42 "Click to jump")

### Description

The $n$th term of the sequence of triangle numbers is given by, $t_n=\frac{1}{2}n(n+1)$; so the first ten triangle numbers are:

$$ 1,3,6,10,15,21,28,36,45,55 $$

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19+11+25=55$. If the word value is a triangle number then we shall call the word a triangle word.

Using [words.txt](https://projecteuler.net/resources/documents/0042_words.txt) (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

### Analysis and Description

Separate the word into letters, and sum the value of each letter, then check whether the value of the word is triangle number.

So how can we check a number is triangle?

According to the definition, a triangle number is formed by $\frac{n(n+1)}{2}$, so it's easy to get

```python
from math import sqrt

def is_triangle(n:int) -> bool:
    
    m = int(sqrt(2*n))

    if m*(m+1) == 2*n:
        return True
    else:
        return False
```

Then check the word

```python
def is_triangle_word(word:str) -> bool:
    value = sum([ord(c)-64 for c in word])

    return is_triangle(value)

with open("0042_words.txt", "r") as f:
    content = f.readline().strip()

    words = [word.strip('"') for word in content.split(',')]

count = 0

for word in words:
    if is_triangle_word(word):
        count += 1

print(count)
```

Here we notice that the ASCII code of letters are consequent and the words are given in big letters. So we can get the alphabetical position by minus `64`, which is the ASCII for the previous character of the first big letter 'A'.

And the result is `162`.