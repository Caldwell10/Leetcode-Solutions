"""
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2], [-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        results = []  # ✅ Store unique triplets

        # Fix `i` -> then implement the two-pointer solution
        for i in range(len(nums) - 2):  # ✅ `-2` because we need at least 3 elements
            if i > 0 and nums[i] == nums[i - 1]:  # ✅ Skip duplicate `i` values
                continue

            # ✅ Initialize Two Pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:  # ✅ Found a valid triplet
                    results.append([nums[i], nums[left], nums[right]])

                    # ✅ Skip duplicate `left` values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # ✅ Skip duplicate `right` values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # ✅ Move both pointers after processing a valid triplet
                    right -= 1

                elif total < 0:  # ✅ Need a larger sum → move `left`
                    left += 1
                else:  # ✅ Need a smaller sum → move `right`
                    right -= 1

        return results  # ✅ Return all unique triplets
