class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxP = 0

        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            profit = prices[i] - minprice
            
            maxP = max(maxP, profit)
        return maxP    


                     
        