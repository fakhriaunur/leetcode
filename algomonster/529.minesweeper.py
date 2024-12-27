#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

from typing import List


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal(r, c):
            mine_count = 0
            for i in range(max(r - 1, 0), min(r + 2, rows)):
                for j in range(max(c - 1, 0), min(c + 2, cols)):
                    if board[i][j] == "M":
                        mine_count += 1

            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = "B"
                for i in range(max(r - 1, 0), min(r + 2, rows)):
                    for j in range(max(c - 1, 0), min(c + 2, cols)):
                        if board[i][j] == "E":
                            reveal(i, j)

        rows = len(board)
        cols = len(board[0])

        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            reveal(r, c)

        return board


# @lc code=end
