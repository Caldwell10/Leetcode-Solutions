
"""
150. Evaluate Reverse Polish Notation (Leetcode)

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The input is always valid.

Example:
Input: ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
            return stack[0]