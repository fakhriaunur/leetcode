def prime_sieve(n: int) -> list[int]:
    primes = [True] * (n + 1)

    primes[0] = False
    primes[1] = False

    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + i, i):
                primes[j] = False

    return [i for i, _ in enumerate(primes)]
    # return list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(primes))))
