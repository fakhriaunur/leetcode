#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

from typing import List


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0

        for num in nums:
            single_number ^= num

        return single_number


# @lc code=end
