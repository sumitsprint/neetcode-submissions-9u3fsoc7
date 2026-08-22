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
                top = st.pop() if st else "#"

                if top != pairs[c]:
                    return False
            else:
                st.append(c)
        return not st                




        