#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ranks = defaultdict(int)

        for road in roads:
            a, b = road
            ranks[a] += 1
            ranks[b] += 1

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                new_rank = ranks[i] + ranks[j]
                if new_rank > max_rank:
                    max_rank = new_rank - (
                        1 if [i, j] in roads or [j, i] in roads else 0
                    )

        return max_rank


# @lc code=end
