"""
    Problems:
        Count the number of prime numbers less than a non-negative integer
    Lessons Learned:
        - Sieve of Eratosthenes
        - Quick prime test
"""

import sure
from math import sqrt, floor


class Solution:
    def is_prime(self, n):
        if n < 2:
            return False

        if n == 2 or n == 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        i = 2
        while i <= floor(sqrt(n)):
            if primes[i]:
                j = 2
                while i * j < n:
                    non_prime = i * j
                    if primes[non_prime]:
                        primes[non_prime] = False
                    j += 1
            i += 1
        return sum(primes)


solution = Solution()
solution.countPrimes(0).should.equal(0)
solution.countPrimes(1).should.equal(0)
solution.countPrimes(2).should.equal(0)
solution.countPrimes(3).should.equal(1)
solution.countPrimes(10).should.equal(4)
solution.countPrimes(999983).should.equal(78497)

print('ok')