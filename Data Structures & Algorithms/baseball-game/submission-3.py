class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for o in operations:
            if o == "+":
                r = st[-1]
                l = st[-2]
                st.append(l + r)
            elif o == "D":
                n = st[-1]
                st.append(2*n)
            elif o == "C":
                st.pop()


            else:
                st.append(int(o))   
        return sum(st)         
        