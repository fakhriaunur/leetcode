#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

from functools import reduce
from operator import xor
from typing import List


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


# @lc code=end
