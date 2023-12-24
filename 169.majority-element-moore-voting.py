#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_num = None
        
        for num in nums:
            if count == 0:
                majority_num = num
                count = 1
            else:
                count += 1 if num == majority_num else -1
        
        return majority_num
# @lc code=end

