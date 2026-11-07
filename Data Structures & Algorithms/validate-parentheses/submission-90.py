class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {"}":"{", ")":"(", "]":"["}
        st = []
        

        for c in s:
            if c  in pairs:
                top = st.pop() if st else "#"
                if pairs[c] != top:
                    return False
            else:
                st.append(c)
        return not st                

