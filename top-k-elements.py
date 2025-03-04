"""
Given an integer array nums and an integer k, return the k most frequent elements.

The test cases are generated such that the answer is always unique.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: The two most frequent elements are 1 and 2.
"""
import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all the occurrences in nums
        count = Counter(nums)

        return heapq.nlargest(k, count.keys, ckey=count.get)
