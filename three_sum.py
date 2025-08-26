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
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                left, right = i + 1, len(nums) - 1

                while left < right:
                    threeSum = num + nums[left] + nums[right]

                    if threeSum > 0:
                        right -= 1
                    elif threeSum < 0:
                        left += 1
                    else:
                        res.append([num, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:  # left pointer to never pass right pointer
                            left += 1

            return res