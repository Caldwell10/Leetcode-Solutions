

"""
13. Roman to Integer (LeetCode)

Given a Roman numeral, convert it to an integer.

Roman numerals are based on the following mappings:
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

When a smaller numeral appears before a larger one, it is subtracted.
When it appears after, it is added.

Example:
Input: "MCMXCIV"
Output: 1994
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result





