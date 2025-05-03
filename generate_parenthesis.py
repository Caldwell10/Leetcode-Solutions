"""
22. Generate Parentheses (Leetcode)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""



from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        only add open parenthesis if open < n
        only add a closing parenthesis if closed < open
        only valid IFF open == closed  == n
        """
        stack = [] # holds our parenthesis
        result = [] # list to hold valid parenthesis combinations

        def backtrack(openN, closedN):
            if openN == closedN == n: # base case
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

            backtrack(0,0)
            return result



