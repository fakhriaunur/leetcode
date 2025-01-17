#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

from typing import List


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i & i - 1] + 1

        return dp


# @lc code=end
