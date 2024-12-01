class Solution:
    def isValid(self, s: str) -> bool:
        """
        Return True if all delimiters are properly matched; False otherwise.
        """
        
        # Define opening and closing delimiters
        lefty = "({["
        righty = ")}]"
        
        # Use a stack to track opening delimiters
        Stack = []  # or use ArrayStack if you have a custom stack implementation
        
        for c in s:
            if c in lefty:
                Stack.append(c)  # push left delimiter onto the stack
            elif c in righty:
                if not Stack:
                    return False  # stack is empty, no matching opening delimiter
                
                # Check if the last item in the stack matches the current closing delimiter
                if righty.index(c) != lefty.index(Stack.pop()):
                    return False  # mismatched delimiter
        
        # If the stack is empty, all delimiters were matched
        return len(Stack) == 0

s = "([{])"
solution = Solution()
print(solution.isValid(s))

#Page  248