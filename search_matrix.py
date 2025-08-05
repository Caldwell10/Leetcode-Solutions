""" Binary Search in 2D Matrix

A Python implementation of a binary search algorithm to find a target in a sorted 2D matrix.

## Problem Description

Given an `m x n` matrix where each row is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row, determine if the target exists.

sol.searchMatrix([[1, 3, 5], [7, 9, 11]], 9)  # returns True
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        up, down = 0, ROWS - 1

        # first binary to find potential row
        while up <= down:
            row = (up + down) // 2
            if target > matrix[row][-1]:
                up = row + 1
            elif target < matrix[row][0]:
                down = row - 1
            else:
                break

        # handle if target is not in matrix
        if not (up <= down):
            return False

        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False





