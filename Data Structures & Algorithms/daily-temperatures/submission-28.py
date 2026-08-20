class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        st = []
        r =  [0] * len(t)

        for i in range(len(t)):
            while st  and t[i] > t[st[-1]]:
                r[st[-1]] = i - st[-1]
                st.pop()

            st.append(i)
        return r        
        