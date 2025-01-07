#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

from typing import List


# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n)

        dp[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            points, bp = questions[i]

            solved = points + (dp[i + bp + 1] if (i + bp + 1 < n) else 0)
            skipped = dp[i + 1]

            dp[i] = max(solved, skipped)

        # print(dp)
        return dp[0]


# @lc code=end
