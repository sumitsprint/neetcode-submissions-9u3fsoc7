class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['


        }
        
        stack = []

        for i in range(len(s)):
            if not stack:
                if s[i] in('(', '{', '['):
                    stack.append(s[i])
                else:
                    return False    

            elif s[i] in(')', '}', ']'):
                if stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False    


            else:
                stack.append(s[i])    
        return not stack


                    
