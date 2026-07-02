class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        ch = (')','}',']')
        stack = []
        for c in s:
            if not stack:
                if c not in ch:
                    stack.append(c)
                else:
                    return False
            
            elif c in ch:
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        return not stack                     
                        
        