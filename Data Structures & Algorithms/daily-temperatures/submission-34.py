class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        n = len(temp)
        res = [0] * n

        for i, m in enumerate(temp):
            while st and m > temp[st[-1]]:
                res[st[-1]] =  i - st[-1]
                st.pop()

            st.append(i)
        return res        











        

        
        