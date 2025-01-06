#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

from typing import List


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            twos = dp[i - 2] + cost[i - 2]
            ones = dp[i - 1] + cost[i - 1]
            dp[i] = min(twos, ones)

        return dp[n]


# @lc code=end
