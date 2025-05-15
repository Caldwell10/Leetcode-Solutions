from typing import List
"""
Problem Description:
There are n cars going to the same destination along a one-lane road. 
The destination is `target` miles away.

You are given two integer arrays `position` and `speed`, both of length n, 
where `position[i]` is the position of the ith car and `speed[i]` is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it 
and drive bumper to bumper at the same speed. 

The faster car will slow down to match the speed of the slower car ahead of it once they meet.

A **car fleet** is some non-empty set of cars driving at the same speed in the same direction.

Return the number of car fleets that will arrive at the destination.
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed)
        pair = [[p, s] for p, s in zip(position, speed)]
        # Sort cars by their starting position in descending order
        stack = []

        # Loop through each car starting from the closest to the target
        for p, s in sorted(pair)[::-1]:
            # Compute the time to reach the target and append it correctly
            stack.append((target - p) / s)

            # If the current car is faster (less time to reach) than the one before it,
            # it will be absorbed into the same fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The remaining cars in the stack are distinct fleets
        return len(stack)
