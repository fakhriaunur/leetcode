#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [0] * (n)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            inc = dp[i - 2] + nums[i]
            exc = dp[i - 1]
            dp[i] = max(inc, exc)

        return dp[n - 1]


# @lc code=end
