class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}': '{',
            ']': '['
        }
        st = []

        for c in s:
            if c in pairs:
                t = st.pop() if st else "#"
                if pairs[c] != t:
                    return False

            else:
                st.append(c)        


            
        
            

            
        return not st                






            
        