class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        len_h = len(haystack)
        len_n = len(needle)

        if len_h < len_n:
            return -1

        for i in range(len_h - len_n + 1):
            j = 0
            while j < len(needle):
                if haystack[j + i] != needle[j]:
                    break
                j += 1
            if j == len_n:
                return i
        return -1


a = Solution()
s = "HelloWorld"
t = "oW"
m = a.strStr(s, t)
print s[m:m+len(t)]