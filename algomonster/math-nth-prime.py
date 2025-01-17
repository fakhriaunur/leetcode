from math import log


def nth_prime(n: int) -> int:
    # n(log(n) + log^^2(n)) for n >= 6, add 6 to cover the n < 6
    UPPER_BOUND = int(n * (log(n) + log(log(n)))) + 6
    primes = [True] * UPPER_BOUND
    primes[0] = primes[1] = False
    ans = 0
    prime_counts = 0

    for i in range(2, UPPER_BOUND):
        if primes[i]:
            prime_counts += 1

            if prime_counts == n:
                ans = i
                break

            for j in range(2 * i, UPPER_BOUND, i):
                primes[j] = False

    return ans


if __name__ == "__main__":
    n = int(input())
    res = nth_prime(n)
    print(res)
