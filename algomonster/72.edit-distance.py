#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            dp[r][0] = r

        for c in range(1, n + 1):
            dp[0][c] = c

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    inserting = dp[r][c - 1] + 1
                    deleting = dp[r - 1][c] + 1
                    replacing = dp[r - 1][c - 1] + 1
                    dp[r][c] = min(inserting, deleting, replacing)

        # print(dp)
        return dp[m][n]


# @lc code=end
