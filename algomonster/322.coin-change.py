#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

from typing import List


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        dp = [0] + [MAX] * amount

        for x in coins:
            # i := curr amount
            for i in range(x, amount + 1):
                dp[i] = min(dp[i], dp[i - x] + 1)

        # print(dp)
        return -1 if dp[amount] == MAX else int(dp[amount])


# @lc code=end
