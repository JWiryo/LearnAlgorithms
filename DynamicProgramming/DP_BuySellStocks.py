class BuySellStocks:

    # Brute Force Solution
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)
    def bruteForceMaxProfit(self, prices: [int]) -> int:
        
        # Initialize Memo
        memo = [0 for i in range(len(prices))]
        memo[0] = 0
        
        for day in range(len(prices)-1):
            
            # Assume buying at that day
            buy = prices[day]
            
            nextDay = day + 1
            while nextDay < len(prices):
                
                profit = prices[nextDay] - buy
                if profit > memo[day]:
                    memo[day] = profit
                
                nextDay += 1
        
        maxProfit = max(memo)
        return maxProfit


    # DP Optimized Solution [Kadane's Algorithm]
    # Time Complexity: O(N)
    # Space Complexity: O(1)

    def kadaneMaxProfit(self, prices: [int]) -> int:
        
        # Initialize Variables
        maxProfit = 0
        minPrice = prices[0]
        
        # Iterate through every price other than the first
        for price in prices[1:]:
            
            # Update maxProfit if currentProfit more than previous maxProfit
            currentProfit = price - minPrice
            maxProfit = max(maxProfit, currentProfit)
            
            # Update minPrice if the current price is cheaper than previouus 
            minPrice = min(minPrice, price)
            
        return maxProfit