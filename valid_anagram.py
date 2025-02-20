
"""
LeetCode Problem 242: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

s = "racecar"
t = "carrace"

def isAnagram(s: str, t: str) -> bool:
     if len(s) != len(t):
         return False

     count = {}

     for char in s:
         count[char] = count.get(char, 0) + 1

     for char in t:
        if char not in count or count[char]== 0:
            return False
        count[char]-=1

     return True

print(isAnagram(s, t))
