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
        curr_combos = []
        combos = []
        
        def dfs(start_index: int, path: List[str], res: List[List[str]]) -> None:
            if start_index == len(digits):
                res.append(''.join(path))
                return
            
            next_number = digits[start_index]
            letters = keypad[int(next_number) - 2]
            
            for letter in letters:
                path.append(letter)
                dfs(start_index+1, path, res)
                path.pop()
        
        dfs(0, curr_combos, combos)
        
        return combos
# @lc code=end

