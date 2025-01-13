#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

from bisect import bisect_left
from typing import List


# @lc code=start
class BinaryIndexedTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree_array = [0] * (size + 1)

    def update(self, index: int, value: int):
        while index <= self.size:
            self.tree_array[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        sum = 0

        while index:
            sum += self.tree_array[index]
            index -= index & -index

        return sum


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        unique_sorted_ratings = sorted(set(rating))
        mapping_size = len(unique_sorted_ratings)

        tree_smaller = BinaryIndexedTree(mapping_size)
        tree_greater = BinaryIndexedTree(mapping_size)

        for value in rating:
            index = bisect_left(unique_sorted_ratings, value) + 1
            tree_greater.update(index, 1)

        total_soldiers = len(rating)
        teams_count = 0

        for i, value in enumerate(rating):
            index = bisect_left(unique_sorted_ratings, value) + 1
            tree_smaller.update(index, 1)
            tree_greater.update(index, -1)

            left_smaller = tree_smaller.query(index - 1)
            right_greater = total_soldiers - i - 1 - tree_greater.query(index)

            teams_count += left_smaller * right_greater
            teams_count += (i - left_smaller) * (total_soldiers - i - 1 - right_greater)

        return teams_count


# @lc code=end
