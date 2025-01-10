#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        n = len(s)

        # dp := segmentation possibilities
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))

        # print(dp)
        return dp[n]


# @lc code=end
