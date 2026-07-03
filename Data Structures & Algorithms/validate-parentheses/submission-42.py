class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {

            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            if c in pairs:
                top_element = stack.pop() if stack else "#"
                if top_element != pairs[c]:
                    return False

                
                    

            else:
                stack.append(c)
        return not stack                    


        