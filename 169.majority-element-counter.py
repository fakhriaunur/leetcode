#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        
        for k, v in nums_counter.items():
            if v == max(nums_counter.values()):
                return k
        
        return -1
# @lc code=end

