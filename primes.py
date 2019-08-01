#!/bin/python3
import re
from itertools import chain, repeat
from get_primes import get_primes
from get_fabonacci import get_fabonacci

if __name__ == '__main__':

    prompts = chain(["Please give matrix dimension in this format (<width>x<height>: "],
                    repeat("Not in this format <width>x<height>! Try again: "))
    replies = map(input, prompts)
    regex = re.compile(r'^\d*x\d*$')
    matrix_dimensions = next(filter(regex.match, replies))

    pf_options = {'P', 'F'}
    prompts = chain(["Should I use (P)rime numbers or (F)ibonacci numbers?:"],
                    repeat("Please enter P or F! Try again: "))
    replies = map(input, prompts)
    prime_or_fab = next(filter(pf_options.__contains__, replies))

    the_operator = {'M', 'A'}
    prompts = chain(["Multiplication (*) or Addition (+):"],
                    repeat("Please enter M or A Try again: "))
    replies = map(input, prompts)
    the_operation = next(filter(the_operator.__contains__, replies))

    dimensions = [int(dim) for dim in matrix_dimensions.split("x")]

    the_numbers = []
    if prime_or_fab == "P":
        the_numbers = get_primes(max(dimensions))
    elif prime_or_fab == "F":
        the_numbers = get_fabonacci(max(dimensions))

    for i in range(0, dimensions[1]):
        for j in range(0, dimensions[0]):
            if the_operation == "A":
                print(str(the_numbers[i] + the_numbers[j]).rjust(2), end=" ")
            elif the_operation == "M":
                print(str(the_numbers[i] * the_numbers[j]).rjust(2), end=" ")

        print("")
