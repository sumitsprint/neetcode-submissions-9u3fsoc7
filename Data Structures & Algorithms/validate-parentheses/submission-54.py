class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        st = []

        for c in s:
            if c in pairs:
                if not st:
                    return False
                if st and st[-1] != pairs[c]:
                    return False
                elif st and st[-1] == pairs[c]:
                    st.pop()
            else:
                st.append(c)            
            
        return not st

