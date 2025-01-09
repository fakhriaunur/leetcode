#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for right in range(1, n):
            for left in range(right - 1, -1, -1):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2

                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

        # for r in dp:
        #     print(r)
        return dp[0][-1]


# @lc code=end
