class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ("-", "+", "/", "*")

        for token in tokens:
            if token in op:
                right = st.pop()
                left = st.pop()

                if token == "-":
                    st.append(left - right)

                elif token == "+":
                    st.append(left + right)

                elif token == "/":
                    st.append(int(float(left) / right))   

                else:
                    st.append(left * right)     

            else:
                st.append(int(token))
        return st[-1]                

        