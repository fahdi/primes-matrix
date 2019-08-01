#!/bin/python3

from itertools import chain, repeat

prompts = chain(["Enter a number: "], repeat("Not a number! Try again: "))
replies = map(input, prompts)
n = int(next(filter(str.isdigit, replies)))

primes = []

for possiblePrime in range(2, 1000):

    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)

    if len(primes) >= n:
        break

for i in range(0, n):
    for j in range(0, n):
        print(str(primes[i] + primes[j]).rjust(2), end=" ")
    print("")


