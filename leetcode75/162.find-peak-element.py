#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

from typing import List
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def feasible_ascend(k: int) -> bool:
            return nums[k] > nums[k + 1]
        
        # def feasible_direction(k: int) -> str:
        #     if nums[k] == nums[-1]:
        #         if nums[k] > nums[0]:
        #             return "left"
                
        #         if nums[k] < nums[0]:
        #             return "right"
            
        #     if nums[k] > nums[k + 1]:
        #         # descending slope, go left
        #         return "left"
            
        #     if nums[k] < nums[k + 1]:
        #         # ascending slope, go right
        #         return "right"
        #     # if nums[k] == nums[0]:
                
            
        #     return "right"
            
        if len(nums) == 1:
            return 0
            
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + ((right - left) >> 1)
            if feasible_ascend(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end

