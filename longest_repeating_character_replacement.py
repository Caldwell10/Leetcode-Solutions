"""
424. Longest Repeating Character Replacement (LeetCode)

You are given a string s and an integer k. You can replace at most k characters in the string
so that the resulting substring contains only the same letter.

Return the length of the longest substring containing the same letter after performing at most k replacements.

Example:
Input: s = "AABABBA", k = 1
Output: 4
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # initialize count hashmap
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] = - 1
                l += 1
            res = max(res, (r - l + 1))

        return res

