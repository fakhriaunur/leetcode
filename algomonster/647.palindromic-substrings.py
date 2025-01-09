#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        # palindrome lengths
        dp = [0] * n

        center = 0
        right_boundary = 0

        # palindromic substrings count
        ans = 0

        for i in range(1, n - 1):
            if right_boundary > i:
                dp[i] = min(right_boundary - i, dp[2 * center - i])
            else:
                dp[i] = 1

            while t[i + dp[i]] == t[i - dp[i]]:
                dp[i] += 1

            if i + dp[i] > right_boundary:
                right_boundary = i + dp[i]
                center = i

            ans += dp[i] // 2

        return ans


# @lc code=end
