
"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_set = set()
        while True:
            a = list(str(n))
            s = 0
            for i in a:
                s += int(i) ** 2
            if s == 1:
                return True
            if s not in num_set:
                num_set.add(s)
            else:
                break
            n = s
        return False


class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_set = set()
        while True:
            n = sum([int(i)**2 for i in list(str(n))])
            if n == 1:
                return True
            if n not in num_set:
                num_set.add(n)
            else:
                return False
        return False


a = Solution2()
print a.isHappy(7)






