class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        maxSum = nums[0]
        minSum = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - minSum > maxSum:
                maxSum = sum - minSum
            if sum < minSum:
                minSum = sum
        return maxSum

a = Solution()
nums = [-2, 1, -3, 4, -1, 2]
# nums = [-2, 1, -3]
# nums = [1, 2, 3, 4, 5]
# [4,-1,2,1] has the largest sum = 6.
print a.maxSubArray(nums)