"""
Given a 1-indexed sorted array of integers, find two numbers that add up to the target.

You must return the indices of the two numbers (1-based indexing).

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: numbers[1] + numbers[2] = 2 + 7 = 9.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: numbers[1] + numbers[3] = 2 + 4 = 6.

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is **sorted in non-decreasing order**.
- **Exactly one solution exists.**
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left, right = 0, len(numbers) - 1

        while left < right:
            # Calculate the current sum
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # ✅ Return 1-based indices

            # If sum is too small, move left pointer forward
            elif current_sum < target:
                left += 1

            # If sum is too large, move right pointer backward
            else:
                right -= 1

        return []  # Should never reach here (problem guarantees exactly one solution)
