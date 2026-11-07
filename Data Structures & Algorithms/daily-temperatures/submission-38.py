class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temp)

        for i in range(len(temp)):
            while st and temp[i] > temp[st[-1]]:
                ans[st[-1]] = i - st[-1]
                st.pop()

            st.append(i)
        return ans        



        