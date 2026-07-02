class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for c in s:
            # If it's a closing bracket
            if c in pairs:
                # Pop the top element if stack is not empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the opening bracket doesn't match, it's invalid
                if pairs[c] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(c)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack