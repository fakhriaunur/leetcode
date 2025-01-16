#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

from typing import List


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res: List[int] = [0] * n
        stack: List[int] = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day_idx = stack.pop()
                res[prev_day_idx] = i - prev_day_idx

            stack.append(i)

        return res


# @lc code=end
