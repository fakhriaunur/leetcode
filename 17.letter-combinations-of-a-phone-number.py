#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keypad = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combos = ['']
        
        for digit in digits:
            letters = keypad[int(digit) - 2]
            combos = [prefix + letter for prefix in combos for letter in letters]
        
        return combos
# @lc code=end

