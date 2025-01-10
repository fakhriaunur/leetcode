#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = defaultdict(lambda: 0)
        ans = 0

        for curr_word in words:
            for j in range(len(curr_word)):
                prev_word = curr_word[:j] + curr_word[j + 1 :]
                dp[curr_word] = max(dp[curr_word], dp[prev_word] + 1)

            ans = max(ans, dp[curr_word])

        return ans


# @lc code=end
