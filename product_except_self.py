"""
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
- The product of all elements except nums[0] = 2 × 3 × 4 = 24
- The product of all elements except nums[1] = 1 × 3 × 4 = 12
- The product of all elements except nums[2] = 1 × 2 × 4 = 8
- The product of all elements except nums[3] = 1 × 2 × 3 = 6

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10⁵
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow-up: Can you solve the problem in O(n) time complexity and without using division?

"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # prefix pass
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix*=nums[i]

        # suffix pass
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i]*=suffix
            suffix*=nums[i]

        return output


