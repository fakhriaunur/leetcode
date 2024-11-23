#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#
from bisect import bisect_left
from typing import List
from itertools import count
from collections import Counter
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def is_success(num: int) -> bool:
            return num >= success
        
        def valid_potion(spell: int, potion: int) -> bool:
            return spell * potion >= success
            
        def valid_potion_first_index(spell: int, sorted_potions: List[int]) -> int:
            left = 0
            right = len(sorted_potions) - 1
            ans = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if valid_potion(spell, sorted_potions[mid]):
                    # print(f"spell: {spell}, potion: {sorted_potions[mid]}")
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return ans
            
            
        # sorted_potions = sorted(potions)
        potions.sort()
        res: List[int] = []
        
        for i in range(len(spells)):
            index = valid_potion_first_index(spells[i], potions)
            # print(sorted_potions[index:])
            if index != -1:
                res.append(len(potions) - index)
            else:
                res.append(0)
        
        return res
        
# @lc code=end

