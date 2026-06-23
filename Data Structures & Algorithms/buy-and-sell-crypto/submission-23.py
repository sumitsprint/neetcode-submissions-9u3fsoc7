class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        mp = prices[0]
        p = 0

        for right in range(1,len(prices)):
            mp = min(prices[right], mp )

            c = prices[right] - mp
            p = max(p, c )
            
        return p


            

        