class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        st = []

        for c in s:
            if c in pairs:
                t = st.pop() if st else "#"
                if t != pairs[c]:
                    return False
            else:
                st.append(c)
        return not st        




        