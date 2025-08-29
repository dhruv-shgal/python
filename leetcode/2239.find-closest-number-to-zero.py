#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        short=nums[0]
        for i in range(len(nums)):
            short=min(abs(nums[i]+0))
            return short
