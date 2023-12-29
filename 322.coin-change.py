#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [0] + [INF] * amount
        
        for coin in coins:
            for curr in range(coin, amount + 1):
                dp[curr] = min(dp[curr], dp[curr - coin] + 1)
        
        return -1 if dp[amount] == INF else int(dp[amount])
# @lc code=end

