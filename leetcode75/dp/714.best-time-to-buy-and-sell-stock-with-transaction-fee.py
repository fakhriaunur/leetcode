#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f0 = 0
        f1 = -prices[0]

        for i in range(1, len(prices)):
            f0, f1 = (
                max(f0, f1 + prices[i] - fee),
                max(f1, f0 - prices[i]),
            )

        return max(f0, f1)


# @lc code=end
