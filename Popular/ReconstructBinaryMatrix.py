class ReconstructBinaryMatrix:

    # Greedy Solution
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reconstructMatrix(self, upper: int, lower: int, colsum: [int]) -> [[int]]:
      
      # Initiate Result
      result = []
      
      # Edge Case Handling
      if sum(colsum) > upper + lower:
        return result
      
      # Initiate upper and lower result matrix
      upMat = [-1] * len(colsum)
      botMat = [-1] * len(colsum)
      
      # First iteration through colSum to fill in 2 and 0
      for i in range(len(colsum)):
        
        # If 2, both need to be 1
        if colsum[i] == 2:
          upMat[i] = 1
          botMat[i] = 1
          
          # Lower count of upp er and lower
          upper -= 1
          lower -= 1
        
        # If 0, both need to be 0
        elif colsum[i] == 0:
          upMat[i] = 0
          botMat[i] = 0
          
        else:
          continue
      
      # Go through 2nd iteration
      for i in range(len(colsum)):
        
        # If 1, 
        if colsum[i] == 1:
          
          # If both are filled up
          if upper == 0 and lower == 0:
            return []
          
          # fill in upper first
          if upper != 0 and upMat[i] == -1:
            
            upMat[i] = 1
            upper -= 1
            
            botMat[i] = 0
          
          # then fill in lower
          else:
            
            botMat[i] = 1
            lower -= 1
            
            upMat[i] = 0
      
      if upper != 0 or lower != 0:
        return []
      
      return [upMat, botMat]