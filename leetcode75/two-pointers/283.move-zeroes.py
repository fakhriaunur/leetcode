#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

from typing import List


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

                slow += 1


# @lc code=end
