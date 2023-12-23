#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            ans = max(ans, profit)
        return int(ans)
        
# @lc code=end

