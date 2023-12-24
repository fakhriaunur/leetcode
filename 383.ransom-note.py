#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counter = Counter(magazine) 
        
        for c in ransomNote:
            mag_counter[c] -= 1
            
            if mag_counter[c] < 0:
                return False
        
        return True
# @lc code=end

