
"""
155. Min Stack (Leetcode)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Example:
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
"""

class MinStack:
    def __init__(self):
        self.stack = [] # main stack
        self.minStack = [] # stack to track the least number after every iteration

        def push(self, val: int) -> None:
            self.stack.append(val)
            val = min(val, self.minStack[-1]) if self.minStack else val
            self.minStack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.minStack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.minStack[-1]


