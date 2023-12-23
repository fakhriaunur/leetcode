#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in sum_dict:
                return [sum_dict[y], i]
            else:
                sum_dict[x] = i
        
        return []
# @lc code=end

