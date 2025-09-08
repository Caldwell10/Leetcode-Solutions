"""
3. Longest Substring Without Repeating Characters (LeetCode)

Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # left pointer
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:  # duplicate
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)

        return result

