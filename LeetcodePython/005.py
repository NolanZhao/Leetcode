"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            str0 = self.get_palindrome(s, i, i)
            if len(str0) > len(ans):
                ans = str0

            str1 = self.get_palindrome(s, i, i + 1)
            if len(str1) > len(ans):
                ans = str1
        return ans

    def get_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]


s0 = Solution()
a = "abcbasanfaweinvweniv"
print s0.longestPalindrome(a)