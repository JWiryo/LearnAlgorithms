class SparseVector:
  
    # Time Complexity: O(N)
    def __init__(self, nums: [int]):
      
      # Initialise Hashmap
      self.vectorMap = {}
      
      # Fill in map
      for i in range(len(nums)):
        
        # If num not zero, fill in index as key and value as val
        if nums[i]:
          self.vectorMap[i] = nums[i]
        
    # Time Complexity: O(Min(V1,V2))
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
      
      # Initiate resultSum
      resultSum = 0
      
      # Select shorter vectorMap (Optimization)
      if len(self.vectorMap) <= len(vec.vectorMap):
        chosenVector = self.vectorMap
        nonChosenVector = vec.vectorMap
      else:
        chosenVector = vec.vectorMap
        nonChosenVector = self.vectorMap
      
      # Iterate through vector map keys
      for key in chosenVector.keys():
        
        # Check if both indexes are filled
        if key in nonChosenVector.keys():
          
          # Multiply
          resultSum += self.vectorMap[key] * vec.vectorMap[key]
      
      return resultSum