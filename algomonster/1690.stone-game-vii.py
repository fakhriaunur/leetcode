#
# @lc app=leetcode id=1690 lang=python3
#
# [1690] Stone Game VII
#

from functools import lru_cache
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0

            alice = s[right + 1] - s[left + 1] - dfs(left + 1, right)
            bob = s[right] - s[left] - dfs(left, right - 1)

            return max(alice, bob)

        n = len(stones)
        s = list(accumulate(stones, initial=0))
        ans = dfs(0, n - 1)
        dfs.cache_clear()

        return ans


# @lc code=end
