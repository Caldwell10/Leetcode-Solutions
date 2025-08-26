"""
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i are at (i, ai) and (i, 0).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Constraints:
- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4
"""
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(area, res)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res







