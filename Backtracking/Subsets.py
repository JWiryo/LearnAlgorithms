# Brute Force Recursive Solution
# Time Complexity: O(n*2^n); n = no. of integers; n * T(recurrence) because at each recurrence we perform a shallow copy which is O(N)
# Space Complexity: O(2^n); n = no. of integers

class Subset:
  def subsets(self, nums: [int]) -> [[int]]:
      
    result = []
    
    def powerSet(currentAnswer, idx):
        
      # Add to results
      result.append(currentAnswer[:])
      
      # Iterate through every num
      # Skip integers on left side
      for i in range(idx, len(nums)):
      
        # Add item to currentAnswer
        currentAnswer.append(nums[i])
        
        # Recurse
        # Here is the difference with Permutation, we don't want to reuse earlier integers
        powerSet(currentAnswer, i + 1)
        
        # Backtrack
        currentAnswer.pop()
    
    # Start recurse
    powerSet([], 0)
            
    return result  