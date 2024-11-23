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
        
        potions.sort()
        # res: List[int] = []
        
        # for spell in spells:
        #     first_index = bisect_left(potions, success / spell)
        #     res.append(len(potions) - first_index)
        
        # return res
        return [len(potions) - bisect_left(potions, success / spell) for spell in spells]
        
# @lc code=end

