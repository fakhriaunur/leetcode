#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

from typing import List


# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)

        # p = s//2 := max possible weight
        p = s >> 1
        dp = [0] * (p + 1)

        for x in stones:
            for i in range(p, x - 1, -1):
                dp[i] = max(dp[i], dp[i - x] + x)

        # print(dp)
        return s - dp[p] * 2


# @lc code=end
