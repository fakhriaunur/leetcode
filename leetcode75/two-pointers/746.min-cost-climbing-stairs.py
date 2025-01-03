#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

from typing import List


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0

        for i in range(1, len(cost)):
            a, b = b, min(cost[i - 1] + a, cost[i] + b)

        return b


# @lc code=end
