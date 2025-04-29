"""
567. Permutation in String (Leetcode)

Given two strings s1 and s2, return true if s2 contains a permutation of s1.

In other words, return true if one of s1's permutations is the substring of s2.

Example:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # cant have permutation if s1 is longer

        s1_count = Counter(s1)   #frequency map of s1
        window_count = Counter(s2[:len(s1)])  # first window where s2 is the same length as s1

        if s1_count == window_count: # First window match
            return True

        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            left_char = s2[i - len(s1)] # character leaving the window
            new_char = s2[i] # character entering the window

            window_count[new_char] +=1 #Add new character
            window_count[left_char] -=1 # remove old character

            if window_count[left_char] == 0:# clean up to keep map small in case the leaving character if sully gone
                del window_count[left_char]

            if window_count ==s1_count: # check for match
                return True

        return False









