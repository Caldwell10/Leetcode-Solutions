"""
Given an integer array nums and an integer k, return the k most frequent elements.

The test cases are generated such that the answer is always unique.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: The two most frequent elements are 1 and 2.
"""
from typing import List



    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            freq = [[] for i in range(len(nums) + 1)]

            # populate values in associated key
            for n in nums:
                count[n] = 1 + count.get(n, 0)

            for n, c in count.items():  # access key value pairs
                freq[c].append(n)

            res = []
            for i in range(len(freq) - 1, 0, -1):
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res






