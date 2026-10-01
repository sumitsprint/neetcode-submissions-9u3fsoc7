class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ("-", "*", "/", "+")

        for c in tokens:
            if c not in operators:
                st.append(int(c))
            else:
                
                if c == '+':
                    r = st.pop()
                    l = st.pop()
                   
                    st.append(int(l+r))

                elif c == '-':
                    r = st.pop()
                    l = st.pop()
                   
                    
                    st.append(int(l-r))

                elif c == '/':
                    r = st.pop()
                    l = st.pop()
                    
                    st.append(int(float(l)/r))

                else:
                    r = st.pop()
                    l = st.pop()
                    
                    st.append(int(l*r))
        return st[0]            
    
    



                        


        
        
        