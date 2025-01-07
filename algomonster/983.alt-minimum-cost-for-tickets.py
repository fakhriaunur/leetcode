#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

from bisect import bisect_left
from functools import lru_cache
from typing import List


# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def min_cost_from_day(index: int) -> int:
            if index >= len(days):
                return 0

            result = float("inf")

            for cost, valid_dur in zip(costs, [1, 7, 30]):
                next_index = bisect_left(days, days[index] + valid_dur)
                total_cost = cost + min_cost_from_day(next_index)
                result = min(result, total_cost)

            return int(result)

        return min_cost_from_day(0)


# @lc code=end
