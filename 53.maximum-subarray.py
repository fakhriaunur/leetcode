#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = local_max
        
        for num in nums[1:]:
            local_max = max(local_max, 0) + num
            global_max = max(global_max, local_max)
        
        return global_max
        
# @lc code=end

