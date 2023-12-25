#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set(nums)

        return len(nums) != len(distinct_nums)
        
# @lc code=end

