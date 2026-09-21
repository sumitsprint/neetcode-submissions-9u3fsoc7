class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        t = list(s)

        for i, c in enumerate(t):
            if c == "(":
                st.append(i)
            elif c == ")":
                if st:
                    st.pop()
                else:
                    t[i] = ""
        while st:
            t[st.pop()] = ""
        return "".join(t)                    
