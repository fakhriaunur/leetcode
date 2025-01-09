#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

from functools import lru_cache
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix_sums = list(accumulate(nums, initial=0))

        def subarray_sum(i: int, j: int) -> int:
            return prefix_sums[j] - prefix_sums[i]

        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(index: int, rem_groups: int) -> float:
            if index == n:
                return 0.0

            if rem_groups == 1:
                return subarray_sum(index, -1) / (n - index)

            max_avg_sum = 0.0

            for j in range(index, n):
                curr_avg = subarray_sum(index, j + 1) / (j + 1 - index)
                total_avg_sum = curr_avg + dfs(j + 1, rem_groups - 1)
                max_avg_sum = max(max_avg_sum, total_avg_sum)

            return max_avg_sum

        # for r in dp:
        #     print(r)
        ans = dfs(0, k)
        dfs.cache_clear()

        return ans


# @lc code=end
