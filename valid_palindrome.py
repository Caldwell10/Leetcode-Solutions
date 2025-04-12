"""
Determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True

Example 2:
Input: s = "race a car"
Output: False

Example 3:
Input: s = " "
Output: True

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create two pointers
        left, right = 0, len(s) - 1

        while left < right:  # Compare when pointers meet
            while left < right and not s[left].isalnum():  # Skip non-alphanumeric chars
                left += 1
            while left < right and not s[right].isalnum():  # Skip non-alphanumeric chars
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False  # If mismatch, it's not a palindrome

            left += 1  # Move left pointer forward
            right -= 1  # Move right pointer backward

        return True  # If no mismatches, it's a palindrome
