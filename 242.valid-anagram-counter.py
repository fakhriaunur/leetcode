#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        
        for c in t:
            s_counter[c] -= 1
            
            if s_counter[c] < 0:
                return False
        
        return True
# @lc code=end

