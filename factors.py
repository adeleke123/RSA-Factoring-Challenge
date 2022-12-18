#/usr/bin/env python3

import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, n//i)
    return (n, 1)

def main():
    # Open the file and read each line
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line)
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()
