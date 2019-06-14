# Math

# Find the smallest prime palindrome greater than or equal to N.
#
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
#
# For example, 2,3,5,7,11 and 13 are primes.
#
# Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.
#
# For example, 12321 is a palindrome.
#
#
#
# Example 1:
#
# Input: 6
# Output: 7
# Example 2:
#
# Input: 8
# Output: 11
# Example 3:
#
# Input: 13
# Output: 101
#
#
# Note:
#
# 1 <= N <= 10^8
# The answer is guaranteed to exist and be less than 2 * 10^8.

class Solution(object):
    def isPrime(self, n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        for i in range(1, 6):
            for root in range(10**(i - 1), 10 ** i):
                s = str(root)
                x = int(s + s[-2::-1])
                if x >= N and self.isPrime(x):
                    return x
            for root in range(10 ** (i - 1), 10 ** i):
                s = str(root)
                x = int(s + s[-1::-1])
                if x >= N and self.isPrime(x):
                    return x
