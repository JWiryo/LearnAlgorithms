class CombinationSum:

    # Backtracking Solution
    # Time Complexity: O(N^((T/M) + 1); N = number of candidates, T = Target value, M = Minimal value of candidates
    # Space Complexity: O(T/M)
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
      
      # Initialise solution and decisionSpace array
      solution = []
      decisionSpace = candidates
      
      def combine(current, currentSum, decisionSpace, startIdx):
        
        # Base Case
        if currentSum == target:
          
          # Copy current list to solution
          solution.append(current[::])
          return
        
        # If currentSum is higher, just ignore
        elif currentSum > target:
          return
        
        # Iterate through decisionSpace
        # As this is combination, we want to reduce the decision space after trying that index
        for i in range(startIdx, len(decisionSpace)):
          
          # Add num to current list
          current.append(decisionSpace[i])
          
          # Calculate new Sum
          currentSum = sum(current)
          
          # Recurse
          combine(current, currentSum, decisionSpace, i)
          
          # Backtrack
          numToRemove = current.pop()
          currentSum -= numToRemove
          
      # Base Recursion
      combine([], 0, decisionSpace, 0)
      
      return solution
          