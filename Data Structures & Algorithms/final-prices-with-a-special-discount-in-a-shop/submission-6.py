class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        a = prices.copy()
        

        for i in range(len(prices)):

            while st and prices[st[-1]] >= prices[i]:

                
                j = st.pop()
                a[j] = prices[j] - prices[i]

            


            

            
            


            st.append(i)
        return a