# Different Implementations of Dynamic Programming Problems
# Min Cost Stair Problem 
# Leetcode #746

class MinCostStair:

  # Dynamic Programming (Top-Down Brute Force Recursive)
  # Time Complexity: O(2^N)
  # Space Complexity: O(N) -> Maximum call stack is only a single branch down to the bottom of the binary tree even though we perform the call 2^n times
  def bruteForceMinCostClimbingStairs(self, cost) -> int:
        
    length = len(cost)
    
    def minCost(idx):
        
      if idx < 0:
          return 0
      elif idx == 0 or idx == 1:
          return cost[idx]
      
      return cost[idx] + min(minCost(idx-1), minCost(idx-2))
          
    return min(minCost(length-1), minCost(length-2))
  
# Dynamic Programming (Top-Down Memoized Recursive)
# Time Complexity: O(N) -> Only need to compute recursive case once
# Space Complexity: O(N) -> Maximum call stack is only a single branch down to the bottom of the binary tree

  def memoizedMinCostClimbingStairs(self, cost) -> int:
          
    length = len(cost)
    
    # Initialize Memoization dictionary
    memo = {}
    
    def minCost(idx):
        
        if idx < 0:
            return 0
        elif idx == 0 or idx == 1:
            return cost[idx]
        elif idx in memo:
            # Return Memoized Result
            return memo[idx]
        
        memo[idx] = cost[idx] + min(minCost(idx-1), minCost(idx-2))
        return memo[idx]
          
    return min(minCost(length-1), minCost(length-2))

# Dynamic Programming (Bottom-Up Iterative)
# Time Complexity: O(N) 
# Space Complexity: O(N) 

  def bottomUpMinCostClimbingStairs(self, cost) -> int:

    length = len(cost)
        
    # Initialize Memoization dictionary
    memo = {}
    
    memo[0] = cost[0]
    memo[1] = cost[1]
    
    for i in range(2, length):
        memo[i] = cost[i] + min(memo[i-1], memo[i-2])
    
    return min(memo[length-1], memo[length-2])
  
# Dynamic Programming (Bottom-Up Iterative)
# Time Complexity: O(N) 
# Space Complexity: O(1) - Only save last 2 variables instead of a whole scaling table

  def bottomUpOptimizedMinCostClimbingStairs(self, cost) -> int:

    length = len(cost)
        
    # Initialize Memoization dictionary
    memo = {}
    
    memo[0] = cost[0]
    memo[1] = cost[1]
    
    for i in range(2, length):
        memo[i] = cost[i] + min(memo[i-1], memo[i-2])
    
    return min(memo[length-1], memo[length-2])

    