import itertools

prod = 0
for i,j in itertools.product(range(1, 101), repeat=2):
    if i!=j:
        prod += i*j

print(prod)
