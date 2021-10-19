class PascalTriangle:

    # Bottom Up DP Solution
    # Time Complexity: O(R^2); R = number of rows
    # Space Complexity: O(R^2)
    def generate(self, numRows: int) -> [[int]]:
      
      # Edge Case
      if numRows == 1:
        return [[1]]
      
      # Initialise result array
      result = [[1]]
      
      # Iterate through numRows
      for i in range(1, numRows):
        
        # Initialise row
        row = []
        
        for j in range(i+1):
          
          # Edges
          if j == 0 or j == i:
            
            row.append(1)
          
          else:
            
            # Calculate the pascal sum
            pascal = result[i-1][j-1] + result[i-1][j]
            row.append(pascal)
        
        # Add to result
        result.append(row)
      
      return result