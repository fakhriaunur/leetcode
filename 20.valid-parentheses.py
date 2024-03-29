#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk: list[str] = []
        valid_pairs = {'{}', '[]', '()'}
        bracket_openings = {'{', '[', '('}
        
        for c in s:
            if c in bracket_openings:
                stk.append(c)
            elif not stk or stk.pop() + c not in valid_pairs:
                return False
        
        return not stk
        
# @lc code=end

