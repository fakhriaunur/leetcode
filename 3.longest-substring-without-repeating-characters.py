#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        max_length = 0
        left_ptr = 0
        
        for right_ptr, char in enumerate(s):
            while char in unique_chars:
                unique_chars.remove(s[left_ptr])
                left_ptr += 1
            
            unique_chars.add(char)
            max_length = max(max_length, right_ptr - left_ptr + 1)
        
        return max_length
        
# @lc code=end

