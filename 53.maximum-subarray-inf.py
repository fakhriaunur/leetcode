#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = -float('inf')
        global_max = local_max
        
        for num in nums:
            local_max = max(local_max, 0) + num
            global_max = max(global_max, local_max)
        
        return int(global_max)
        
# @lc code=end

