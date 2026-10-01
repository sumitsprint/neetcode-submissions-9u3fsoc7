class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ("-", "*", "/", "+")

        for c in tokens:
            if c not in operators:
                st.append(int(c))
            else:
                r = st.pop()
                l = st.pop()
                if c == '+':
                   
                    st.append(int(l+r))

                elif c == '-':
                   
                    
                    st.append(int(l-r))

                elif c == '/':
                    
                    st.append(int(float(l)/r))

                else:
                    
                    st.append(int(l*r))
        return st[0]            
    
    



                        


        
        
        