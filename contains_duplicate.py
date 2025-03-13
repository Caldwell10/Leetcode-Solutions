"""
LeetCode 217: Contains Duplicate
Problem: Given an integer array nums, return true if any value appears at least twice.
Otherwise, return false.
Approach: Use a HashSet to track seen numbers.
  - If a number is already in the set, return True (duplicate found).
  - Otherwise, add the number to the set and continue.
  - If no duplicates are found, return False.

   Time Complexity: O(n) → We iterate through the array once, and set operations (add & lookup) take O(1) on average.
  Space Complexity: O(n) → In the worst case, all elements are unique and stored in the set.
"""
nums = [1,5,6,4,6]
def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicates(nums))
