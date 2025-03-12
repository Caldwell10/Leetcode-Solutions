"""
Determine if a 9x9 Sudoku board is valid.

A Sudoku board is valid if:
- Each row contains unique numbers (1-9).
- Each column contains unique numbers (1-9).
- Each 3x3 sub-box contains unique numbers (1-9).

The board may contain "." indicating empty cells.

Example:
Input:
board =
[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: True
"""

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                boxes_index = (i //3) * 3 + (j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[boxes_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[boxes_index].add(num)

        return True