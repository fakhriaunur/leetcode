#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

from typing import List


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < target or (total - target) % 2 != 0:
            return 0

        s = (total - target) // 2

        dp = [1] + [0] * s

        for x in nums:
            for i in range(s, x - 1, -1):
                dp[i] += dp[i - x]

        # print(dp)
        return dp[-1]


# @lc code=end
