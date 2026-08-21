class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}': '{',
            ']': '['
        }
        st = []

        for c in s:
            if st and c in pairs:
                top_ele = st.pop() 

                if top_ele != pairs[c]:
                    return False

            elif not st and c in pairs:
                return False

            else:
                st.append(c)
        return not st                






            
        