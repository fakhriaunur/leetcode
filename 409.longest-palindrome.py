#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
### NOTE
# (v & 1) == (v % 2)
# (ans & 1 ^ 1) == (ans % 2 == 0)

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        ans = 0
        
        for v in s_counter.values():
            ans += v - (v & 1)
            ans += (ans & 1 ^ 1) and (v & 1)
        
        return ans
        
# @lc code=end

