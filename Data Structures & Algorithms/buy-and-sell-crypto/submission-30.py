class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mip = prices[0]
        max_p = 0
        
        for i in range(1, len(prices)):
            mip = min(mip, prices[i])
            p = prices[i] - mip
            max_p = max(p, max_p)
        return max_p        
                
