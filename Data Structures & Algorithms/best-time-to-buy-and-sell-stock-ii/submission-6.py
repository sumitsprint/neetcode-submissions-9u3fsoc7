class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices)):
            if i > 0: 
                if prices[i] > prices[i - 1]:
                    p += prices[i] - prices[i-1]
        return p                    
        