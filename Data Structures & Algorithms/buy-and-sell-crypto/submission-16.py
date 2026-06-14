class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
            
        min_price = prices[0]
        max_profit = 0

        # Start from index 1 since index 0 is already our initial min_price
        for i in range(1, len(prices)):
            # Update the lowest purchase price seen so far
            min_price = min(min_price, prices[i])
            
            # Calculate profit if we were to sell at the current price
            current_profit = prices[i] - min_price
            
            # Update the maximum profit achieved so far
            max_profit = max(max_profit, current_profit)
            
        return max_profit  


        # minimum is minimum price seen so far and max profit is the profit achievable 
        #using only day 0 to i or minimum price seen so far


                     
        