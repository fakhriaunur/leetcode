#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#
from typing import List
from itertools import count
from collections import Counter
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def is_success(num: int) -> bool:
            return num >= success
            
        # spells = row
        # potions = column
        res: List[int] = []
        for i in range(len(spells)):
            succ_pairs: List[int] = []
            for j in range(len(potions)):
                pair = spells[i] * potions[j]
                if is_success(pair):
                    succ_pairs.append(pair)
                # print(succ_pairs)
            res.append(len(succ_pairs))
        
        return res
        
# @lc code=end

