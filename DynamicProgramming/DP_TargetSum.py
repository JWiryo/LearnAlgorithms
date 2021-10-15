class TargetSum:

    # Top-Down Memoized Recursive DP Solution
    # Time Complexity: O(2^N)
    # Space Complexity: O(N)
    def findTargetSumWays(self, nums: [int], target: int) -> int:
    
      # Initialise currentSum
      currentSum = 0
      
      # Initialise memo
      memo = {}
      
      # Define helper function
      def helper(index, currentSum):
        
        # Memo Return
        if (index, currentSum) in memo:
          return memo[(index, currentSum)]
        
        # Base Case
        if index == len(nums) and currentSum == target:
          return 1
        elif index == len(nums) and currentSum != target:
          return 0
          
        # Positive Sum
        positiveSum = currentSum + nums[index]
        positiveCount = helper(index + 1, positiveSum)
        
        # Negative Sum
        negativeSum = currentSum - nums[index]
        negativeCount = helper(index + 1, negativeSum)
        
        # Calculate currentCount
        currentCount = positiveCount + negativeCount
        memo[(index, currentSum)] = currentCount
        
        return currentCount
        
      
      # Initialise recursion
      helper(0,currentSum)
      
      return memo[(0,0)]