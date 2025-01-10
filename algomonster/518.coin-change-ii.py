#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

from typing import List


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        # dp[0] = 1

        for x in coins:
            for i in range(x, amount + 1):
                dp[i] += dp[i - x]

        # print(dp)
        return dp[amount]


# @lc code=end
