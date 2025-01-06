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
        prev_step = curr_step = 0

        for i in range(2, n + 1):
            prev_step, curr_step = (
                curr_step,
                min(prev_step + cost[i - 2], curr_step + cost[i - 1]),
            )

        return curr_step


# @lc code=end
