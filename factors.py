import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, n // i)
    return (n, 1)

# Read numbers from the input file
with open(sys.argv[1], 'r') as f:
    numbers = [int(line.strip()) for line in f]

# Factorize each number and print the result
for n in numbers:
    p, q = factorize(n)
    print(f"{n}={p}*{q}")

