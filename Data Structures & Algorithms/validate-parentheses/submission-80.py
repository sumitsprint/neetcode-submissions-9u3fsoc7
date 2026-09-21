class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        st = []

        for c in s:
            if c not in pairs:
                st.append(c)
            else:
                if st:
                    top = st.pop()
                    if top != pairs[c]:
                        return False
            # if st is empty            
                else:
                    return False        
        return not st                         