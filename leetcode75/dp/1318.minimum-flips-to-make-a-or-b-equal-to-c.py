#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

from math import log2


# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips_count = 0
        log_a = int(log2(a))
        log_b = int(log2(b))
        log_c = int(log2(c))

        for i in range(max(log_a, log_b, log_c) + 1):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            if bit_a | bit_b != bit_c:
                flips_count += 2 if bit_a == 1 and bit_b == 1 else 1

        return flips_count


# @lc code=end
