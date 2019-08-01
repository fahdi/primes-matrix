#!/bin/python3

from itertools import chain, repeat
from get_primes import get_primes

if __name__ == '__main__':

    prompts = chain(["Enter a number: "], repeat("Not a number! Try again: "))
    replies = map(input, prompts)
    n = int(next(filter(str.isdigit, replies)))

    primes = get_primes(n)

    for i in range(0, n):
        for j in range(0, n):
            print(str(primes[i] + primes[j]).rjust(2), end=" ")
        print("")


# def hello_world(): return 'hello world'
