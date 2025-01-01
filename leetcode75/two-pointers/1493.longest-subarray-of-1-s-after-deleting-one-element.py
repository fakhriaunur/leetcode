#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

from typing import List


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zero_count = 0
        longest_window = zero_count

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            right += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

            longest_window = max(longest_window, right - left - 1)

        return longest_window


# @lc code=end
