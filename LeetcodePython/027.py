class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        A = nums
        elem = val
        j = len(A)-1
        for i in range(len(A)-1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1



a = Solution()
n = [2, 3, 3, 4, 6, 3, 4, 5, 6, 2, 2]
j = a.removeElement(n, 3)
print n[:j]