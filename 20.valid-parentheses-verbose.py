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
        
        for c in s:
            if c in '{[(':
                stk.append(c)
            else:
                if not stk:
                    return False
                
                chars_pair = stk.pop() + c
                if chars_pair not in valid_pairs:
                    return False
        
        return not stk
        
# @lc code=end

