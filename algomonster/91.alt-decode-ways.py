#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        prev_count = 0
        curr_count = 1

        for i in range(len(s)):
            next_count = 0

            if s[i] != "0":
                next_count = curr_count

            if (
                i > 0
                and s[i - 1] != "0"
                and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6"))
            ):
                next_count += prev_count

            prev_count, curr_count = (
                curr_count,
                next_count,
            )

        return curr_count


# @lc code=end
