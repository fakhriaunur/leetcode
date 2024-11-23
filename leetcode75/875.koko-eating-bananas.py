#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k: int) -> bool:
            s = 0
            for pile in piles:
                s += (pile - 1 + k) // k
            print(s)
            # s = total_hours to eat all bananas from every piles
            # s = sum((pile + k - 1) // k for pile in piles)
            
            return s <= h
            
        left = 1
        right = max(piles)
        ans = -1
        
        while left <= right:
            # mid = left + (right - left) // 2
            # bitwise shitft right
            # mid = (left + right) >> 2
            mid = left + ((right - left) >> 1)
            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        
# @lc code=end

