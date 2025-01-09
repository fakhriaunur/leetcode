#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if str1[r - 1] == str2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:
                    prev_top = dp[r - 1][c]
                    prev_left = dp[r][c - 1]
                    dp[r][c] = max(prev_top, prev_left)

        common = []

        r, c = m, n
        while r > 0 or c > 0:
            if r == 0:
                c -= 1
                common.append(str2[c])

            elif c == 0:
                r -= 1
                common.append(str1[r])

            else:
                if dp[r][c] == dp[r - 1][c]:
                    r -= 1
                    common.append(str1[r])

                elif dp[r][c] == dp[r][c - 1]:
                    c -= 1
                    common.append(str2[c])

                else:
                    r -= 1
                    c -= 1
                    common.append(str1[r])

        # for r in dp:
        #     print(r)
        return "".join(common[::-1])


# @lc code=end
