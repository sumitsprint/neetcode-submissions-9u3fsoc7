class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)  

        for i, c in enumerate(s):
            if c == ')':
                if st:
                    st.pop()
                else:
                    s[i] = ""

            elif c == '(':
                st.append(i)

        while st:
            s[st.pop()] = ""
        return "".join(s)           


                        

                    


                    
                    



