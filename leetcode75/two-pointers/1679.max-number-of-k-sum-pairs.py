#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

from typing import List


# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_pair = nums[left] + nums[right]
            if sum_pair == k:
                count += 1
                left += 1
                right -= 1
            elif sum_pair > k:
                right -= 1
            else:
                left += 1

        return count


# @lc code=end
