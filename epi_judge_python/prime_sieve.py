from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    Primes = []
    is_prime = [False, False] + [True] * (n - 1)
    # Primes[0...p] is all the primes smaller or equal to p
    for p in range(2, n + 1):
        if (is_prime[p]):
            Primes.append(p)
            # i is mutliple of p and rnage [p, n+1) is_prime[i] is false if i is not a prime
            for i in range(p, n + 1, p):                # C++ for (int i = p; i <= n + 1; i += p)
                is_prime[i] = False
    return Primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
