class CombinationSumII:

    # Backtracking Solution
    # Time Complexity: O(NLogN + 2^N) -> O(2^N)
    # Space Complexity: O(N)
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
      
      # Initiate result
      result = []
      
      # Sort Candidates
      candidates.sort()
      
      # Define backtracking helper function
      def backtrack(currentList, currentSum, idx):
        
        # Base Case
        if currentSum == target:
          
          # Copy list to result
          result.append(currentList[::])
          return
        
        elif currentSum > target:
          
          # Break off the loop
          return
        
        # Otherwise
        for i in range(idx, len(candidates)):
          
          # Duplicate check
          if i > idx and candidates[i] == candidates[i-1]:
            continue
          
          # Append to currentList
          currentList.append(candidates[i])
          currentSum += candidates[i]
          
          # DFS
          backtrack(currentList, currentSum, i+1)
          
          # Backtrack
          numToRemove = currentList.pop()
          currentSum -= numToRemove
      
      # Base recursion
      backtrack([], 0, 0)
      
      return result