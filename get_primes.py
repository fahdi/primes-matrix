def get_primes(total):
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

        if len(primes) >= total:
            break

    return primes

print(get_primes(10))
