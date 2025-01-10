#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        # num of ways
        dp = [1] + [0] * target

        for i in range(1, n + 1):
            # curr num of ways
            curr_dp = [0] * (target + 1)
            # j := sum value
            for j in range(1, min(i * k, target) + 1):
                # h := face value
                for h in range(1, min(k, j) + 1):
                    curr_dp[j] = (curr_dp[j] + dp[j - h]) % MOD

            dp = curr_dp

        # print(dp)
        return dp[target]

        # s = sum([n * x for x in range(1, k + 1)])

        # dp = [[0] * (s // 2 + 1) for _ in range(n + 1)]

        # dp[0][0] = 1

        # for  i in range(1, n + 1):
        #     for j in range(s//2 + 1):

        # return dp[n][s//2]


# @lc code=end
