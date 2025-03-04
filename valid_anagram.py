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

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Count the frequency of each character in s
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Check the frequency of each character in t
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

# Test the solution
if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    print(isAnagram(s, t))  # Should print True
