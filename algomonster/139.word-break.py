#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        word_set = set(wordDict)

        def dfs(start_index: int) -> bool:
            if start_index in memo:
                return memo[start_index]

            if start_index == len(s):
                return True

            ans = False

            for word in word_set:
                n = len(word)
                if s[start_index:].startswith(word):
                    if dfs(start_index + n):
                        ans = True

            memo[start_index] = ans
            return ans

        return dfs(0)


# @lc code=end
