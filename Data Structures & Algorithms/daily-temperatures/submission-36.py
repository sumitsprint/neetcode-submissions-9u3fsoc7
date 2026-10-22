class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temp)

        for i in range(len(temp)):
            while st and temp[st[-1]] < temp[i]:
                w = st.pop()
                ans[w] = i - w
            st.append(i)
        return ans        

        