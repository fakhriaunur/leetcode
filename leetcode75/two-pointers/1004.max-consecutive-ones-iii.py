#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                k -= 1

            right += 1

            while k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1

            max_length = max(max_length, right - left)

        return max_length


# @lc code=end
