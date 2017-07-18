class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                j += 1
        return j+1


a = Solution()
n = [1, 1, 2, 3, 3, 3, 4, 5]
print a.removeDuplicates(n)
print n[:5]