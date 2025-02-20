"""
LeetCode Problem 1: Two Sum
Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, return [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):  # Loop through array with index and value
            comp = target - num  # Calculate the complement

            # Check if the complement is already in the dictionary
            if comp in complement:
                # If found, return the index of the complement and the current index
                return [complement[comp], i]

            # If not found, store the current number's index
            complement[num] = i

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Should print [0, 1]
