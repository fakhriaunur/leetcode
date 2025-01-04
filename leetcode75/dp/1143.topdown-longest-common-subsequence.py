#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @lru_cache(None)
        def lcs(m: int, n: int, memo: dict[tuple[int, int], int]) -> int:
            if (m, n) in memo:
                return memo[m, n]

            if m == 0 or n == 0:
                return 0

            res = 0

            if text1[m - 1] == text2[n - 1]:
                res = lcs(m - 1, n - 1, memo) + 1

            else:
                res = max(lcs(m - 1, n, memo), lcs(m, n - 1, memo))

            memo[m, n] = res
            return res

        m = len(text1)
        n = len(text2)

        memo = dict()

        return lcs(m, n, memo)


# @lc code=end
