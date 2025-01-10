#
# @lc app=leetcode id=1671 lang=python3
#
# [1671] Minimum Number of Removals to Make Mountain Array
#

from typing import List


# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # left and right lis
        dp_left = [1] * n
        dp_right = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_left[i] = max(dp_left[i], dp_left[j] + 1)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    dp_right[i] = max(dp_right[i], dp_right[j] + 1)

        max_bitonic_len = max(
            (left + right - 1)
            for left, right in zip(dp_left, dp_right)
            if left > 1 and right > 1
        )

        # print(dp_left)
        # print(dp_right)
        return n - max_bitonic_len


# @lc code=end
