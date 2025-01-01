#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        while s_idx < len(s) and t_idx < len(t):
            if t[t_idx] == s[s_idx]:
                s_idx += 1

            t_idx += 1

        return s_idx == len(s)


# @lc code=end
