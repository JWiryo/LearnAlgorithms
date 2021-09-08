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