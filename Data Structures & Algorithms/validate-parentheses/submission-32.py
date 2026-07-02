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

                if pairs[c] != top_element:
                    return False

            else:
                stack.append(c)
        return not stack                





        