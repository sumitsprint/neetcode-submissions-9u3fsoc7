class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ("-", "+", "/", "*")
        st = []

        for token in tokens:
            if token in op:
                r = st.pop()
                l = st.pop()
                if token == "+":
                    st.append(l + r)
                elif token  == "-":
                    st.append(l - r)
                elif token == "*":
                    st.append(l * r)
                else:
                    st.append(int(float(l) / r))        

            else:
                st.append(int(token))
        return st[-1]        

        
        



        