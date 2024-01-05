#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1_step = 1
        prev2_step = 1
        
        for _ in range(2, n+1):
            dp = prev1_step + prev2_step
            prev2_step = prev1_step
            prev1_step = dp
        
        return prev1_step
# @lc code=end

