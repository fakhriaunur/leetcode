#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        def dfs(current: int) -> int:
            if current == 1:
                return 0

            ans = current
            divisor = 2

            while divisor * divisor <= current:
                if current % divisor == 0:
                    ans = min(ans, dfs(current // divisor) + divisor)

                divisor += 1

            return ans

        return dfs(n)


# @lc code=end
