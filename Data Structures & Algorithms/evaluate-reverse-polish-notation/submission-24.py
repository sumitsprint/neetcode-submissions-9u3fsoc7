class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ("+", "-", "/", "*")

        for c in tokens:
            if c not in op:
                st.append(int(c))

            else:
                right = st.pop()
                left =     st.pop()

                if c == "-":
                    st.append(left - right)

                elif c == "+":
                    st.append(left + right)

                elif c == "*":
                    st.append(left* right)
                else:
                    st.append(int(float(left) / right))
        return st[-1]                        
                    


        