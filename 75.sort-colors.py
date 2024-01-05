#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_zero_index = -1
        next_two_index = len(nums)
        current_index = 0
        
        while current_index < next_two_index:
            if nums[current_index] == 0:
                next_zero_index += 1
                nums[next_zero_index], nums[current_index] = nums[current_index], nums[next_zero_index]
                current_index += 1
            elif nums[current_index] == 2:
                next_two_index -= 1
                nums[next_two_index], nums[current_index] = nums[current_index], nums[next_two_index]
            else:
                current_index += 1
# @lc code=end

