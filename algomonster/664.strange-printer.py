#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float("inf")] * n for _ in range(n)]

        # possible, but less neat
        # for i in range(n):
        #     dp[i][i] = 1

        for start in range(n - 1, -1, -1):
            dp[start][start] = 1
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    dp[start][end] = dp[start][end - 1]

                else:
                    for k in range(start, end):
                        dp[start][end] = min(
                            dp[start][end],
                            dp[start][k] + dp[k + 1][end],
                        )

        # for r in dp:
        #     print(r)
        return int(dp[0][-1])


# @lc code=end
