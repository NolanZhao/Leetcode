# coding=utf-8
"""
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            if nums[mid] >= target:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)


a = Solution()
n = [1, 2, 3, 6, 7]
t = 4
print a.searchInsert(n, t)