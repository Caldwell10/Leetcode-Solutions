class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}" : "{"} # hashmap mapping each closing bracket to opening

        for char in s:
            if char in closeToOpen: # closing parenthesis since key is closing bracket
                if stack and stack[-1] == closeToOpen[char]: # if stack is not empty and value at the top of the stack is the matching open parenthesis
                    stack.pop() # remove opening bracket from stack
                else:
                    return False
            else:
                stack.append(char) # if character is not a closing bracket then it must be an opening bracket

        if stack:  # If there’s anything left in the stack at the end -> extra opening brackets that never got matched
            return False

        return True








