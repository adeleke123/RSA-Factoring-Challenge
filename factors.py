#/usr/bin/env python3

import sys

def factorize(n):
    for i in range(2, n+1):
        if n % i == 0:
            return (i, n//i)

# Read the numbers from the file
with open(sys.argv[1], 'r') as f:
    numbers = f.read().splitlines()

# Factorize each number and output the result
for n in numbers:
    n = int(n)
    p, q = factorize(n)
    print(f'{n}={p}*{q}')

