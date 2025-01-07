#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

from functools import lru_cache
from typing import List


# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def get_points_at(index: int):
            if index >= len(questions):
                return 0

            points, bp = questions[index]

            solved = points + get_points_at(index + bp + 1)
            skipped = get_points_at(index + 1)

            return max(solved, skipped)

        return get_points_at(0)


# @lc code=end
