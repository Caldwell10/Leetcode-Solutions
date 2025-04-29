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
        count = {}         # Frequency map of characters
        result = 0         # Max window size found
        left = 0           # Left pointer of the sliding window
        maxf = 0           # Most frequent character count in the window

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            # If more than k characters need to be replaced
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

