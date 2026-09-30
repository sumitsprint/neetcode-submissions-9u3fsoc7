class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        arr = list(s)
        for i, c in enumerate(arr):
            if c == "(":
                st.append(i)
            elif c == ')':
                if not st:
                    arr[i] = ""

                else:
                    st.pop()
        while st:
            arr[st.pop()] = ""

        return "".join(arr)    

                    

            










            

        