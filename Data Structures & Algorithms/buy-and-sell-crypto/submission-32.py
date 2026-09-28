class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        p = prices[0]

        for i in range(1,len(prices)):
            p = min(p, prices[i])
            pr = prices[i] - p
            mp = max(mp, pr)
            
            
            
        return mp        
    






        
        