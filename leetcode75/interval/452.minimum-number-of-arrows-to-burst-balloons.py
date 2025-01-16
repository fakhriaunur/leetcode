#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

from typing import List


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        num_arrows = 0
        last_pos = -float("inf")

        for curr_start, curr_end in points:
            if curr_start > last_pos:
                num_arrows += 1
                last_pos = curr_end

        return num_arrows


# @lc code=end
