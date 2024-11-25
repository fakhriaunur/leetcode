#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        all_paths = []
        def dfs(start_index: int, path: List[str]): 
            if is_leaf(start_index):
                all_paths.append("".join(path))
                return
            for edge in get_edges(start_index):
                path.append(edge)
                dfs(start_index + 1, path)
                path.pop()
        
        
        def is_leaf(start_index: int) -> bool:
            return start_index == len(digits)
            
        def get_edges(start_index: int) -> List[str]:
            next_number = digits[start_index]
            return [letter for letter in mapping[next_number]]
        
        
        dfs(0, [])
        return all_paths
        
# @lc code=end

