#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = right = 1
        ans = [0] * n
        
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans
        
# @lc code=end

