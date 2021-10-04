class CoinChange:

    # Top-Down Memoized Recursive DP Solution
    # Time Complexity: O(amount * no. of coins)
    # Space Complexity: O(amount);
    def memoCoinChange(self, coins: [int], amount: int) -> int:
      
      # Edge Case
      if amount == 0:
        return 0
      
      # Setup Memo table
      memo = {}
      
      # Define helper function
      def count(n):

        # DP return
        if n in memo:
          return memo[n]
        
        # If amount exceeds 0, return inf:
        if n < 0:
          return float('inf')
        
        # If reaches 0, start counting
        if n == 0:
          memo[0] = 0
          return memo[0]
        
        # Setup minCount
        minCount = float('inf')
        
        # Try all possible coins
        for coin in coins:
          
          # Calculate number of coins for smaller changes
          # Mininum no. of coin is either itself or smaller denom + 1
          calcSmaller = count(n-coin)
          minCount = min(calcSmaller + 1, minCount)
          
        # Record value
        memo[n] = minCount
        
        return memo[n]
      
      # Start recursion
      count(amount)
      
      # If cannot be broken down, return -1
      if memo[amount] == float('inf'):
        return -1
      
      # Else, return value
      return memo[amount]

    def bottomUpCoinChange(self, coins: [int], amount: int) -> int:
      
      # Edge Case
      if amount == 0:
        return 0
      
      # Setup Memo table
      memo = [float('inf') for i in range(amount+1)]
      
      # Initialise Memo table where amount == 0
      memo[0] = 0
      
      # Fill-up table until we reach amount
      for coinVal in range(1, amount+1):
        for coin in coins:
          
          if coinVal - coin >= 0:
            memo[coinVal] = min(memo[coinVal], memo[coinVal-coin] + 1)
      
      # Edge case where no change can be made
      if memo[coinVal] == float('inf'):
        return -1
      
      # Else, return value
      return memo[amount]