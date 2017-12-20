"""
387
"""
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(list(s))
        for i in s:
            if counts[i] == 1:
                return s.index(i)
        return -1


a = Solution()
s = "leetcode"
print a.firstUniqChar(s)