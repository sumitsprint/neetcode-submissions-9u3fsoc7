class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {

            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            #closing bracket
            if c in pairs:

                top_ele = stack.pop() if stack else "#"

                if top_ele != pairs[c]:
                    return False

            #opening bracket

            else:
                stack.append(c)
        return not stack                



        