class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for right in range(1,len(prices)):
            min_price = min(min_price, prices[right])
            cp = prices[right]  - min_price
            max_profit = max(max_profit, cp)
        return max_profit    

        