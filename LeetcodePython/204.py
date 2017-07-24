"""
204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        isPrimer = [True] * n
        isPrimer[0] = isPrimer[1] = False
        for i in xrange(2, n):
            if isPrimer[i]:
                for j in xrange(i << 1, n, i):
                    isPrimer[j] = False
        cnt = filter(lambda x: x, isPrimer)
        return len(cnt)


a = Solution()
print a.countPrimes(50000)