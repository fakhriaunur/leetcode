#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

from itertools import pairwise
from typing import List


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get_neighbors(r: int, c: int):
            dirs = pairwise([-1, 0, 1, 0, -1])

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    yield nr, nc

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for nr, nc in get_neighbors(r, c):
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        atlantic_visited = set()
        pacific_visited = set()
        num_rows = len(heights)
        num_cols = len(heights[0])
        res = []

        # for r in range(num_rows):
        #     dfs(r, 0, pacific_visited)
        #     dfs(r, num_cols - 1, atlantic_visited)
        # for c in range(num_cols):
        #     dfs(0, c, pacific_visited)
        #     dfs(num_rows - 1, c, atlantic_visited)

        for r in range(num_rows):
            for c in range(num_cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific_visited)
                if r == num_rows - 1 or c == num_cols - 1:
                    dfs(r, c, atlantic_visited)

        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) in atlantic_visited and (r, c) in pacific_visited:
                    res.append((r, c))

        return res

        # return [
        #     (row, col)
        #     for row in range(num_rows)
        #     for col in range(num_cols)
        #     if (row, col) in pacific_visited and (row, col) in atlantic_visited
        # ]


# @lc code=end
