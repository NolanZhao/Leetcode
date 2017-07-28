"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(a, b):
            return int(b + a) - int(a + b)

        nums = sorted([str(x) for x in nums], cmp=compare)
        ans = ''.join(nums).lstrip('0')
        return ans or '0'


s = Solution()
num_list =  [3, 30, 34, 5, 9]
print s.largestNumber(num_list)