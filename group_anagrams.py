"""
Given an array of strings, group words that are anagrams of each other.

An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Explanation: Words that are anagrams are grouped together.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #initialize and empty dictionary that takes lists as values

        for word in strs:
            sorted_word ="".join(sorted(word)) # obtain key for each corresponding anagram
            anagrams[sorted_word].append(word) # use the key to map all its corresponding anagram values


        return list(anagrams.values())


