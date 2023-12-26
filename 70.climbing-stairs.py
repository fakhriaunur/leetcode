#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        prev_step = 0
        curr_step = 1
        
        for _ in range(n):
            prev_step, curr_step = curr_step, prev_step + curr_step
        
        return curr_step
# @lc code=end

