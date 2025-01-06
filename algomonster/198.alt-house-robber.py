#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        inc = 0
        exc = 0

        for value in nums:
            inc, exc = (
                exc + value,
                max(exc, inc),
            )

        return max(exc, inc)


# @lc code=end
