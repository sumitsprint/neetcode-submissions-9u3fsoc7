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
                else:
                    to_ele = st.pop() 

                    if to_ele != pairs[c]:
                        return False
            else:
                st.append(c)
        return not st                  
