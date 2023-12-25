#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = -float('inf')
        max_sum = current_sum
        
        for num in nums:
            current_sum = max(current_sum, 0) + num
            max_sum = max(max_sum, current_sum)
        
        return int(max_sum)
        
# @lc code=end

