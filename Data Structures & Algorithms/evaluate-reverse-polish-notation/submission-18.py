class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("-", "*", "/", "+")

        for c in tokens:
            if c not in operators:
                stack.append(int(c))

            else:
                right = stack.pop()    
                left = stack.pop()
                if c == "-":
                    stack.append(left - right)

                elif c == "+":
                    stack.append(left + right)

                elif c == "/":
                    stack.append(int(left / right))   

                elif c == "*":
                    stack.append(left * right)   
        return stack[0]              




        