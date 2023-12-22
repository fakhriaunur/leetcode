#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter: dict[str, int] = {}
        for c in s:
            if c not in s_counter:
                s_counter[c] = 1
            else:
                s_counter[c] += 1
        
        for c in t:
            if c not in s_counter:
                return False
            else:
                s_counter[c] -= 1
            
            if s_counter[c] < 0:
                return False
        
        return True
# @lc code=end

