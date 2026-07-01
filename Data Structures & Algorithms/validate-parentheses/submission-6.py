class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in range(len(s)):
            if  not stack: #empty stack
                if s[i] in ('(', '{', '['):

                    stack.append(s[i])
                else:
                    return False    

            elif s[i] in (')', '}', ']'):
                if stack[-1] != pairs[s[i]]:
                    return False
                else:
                    stack.pop()    

            elif s[i] in ('(', '{', '['):
                stack.append(s[i])
        return not stack           






            
                    
                

                









        