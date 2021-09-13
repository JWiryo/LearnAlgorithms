class KnightChess:

  # Dynamic Programming (Top-Down Brute Force Recursive)
  # Time Complexity: O(8^k)
  # Space Complexity: O(8^k)

  def bruteForceKnightProbability(self, n: int, k: int, row: int, column: int) -> float:
      
      # Clockwise, Up Right Down Left
      moves = [
          [-2,1],
          [-1,2],
          [1,2],
          [2,1],
          [2,-1],
          [1,-2],
          [-1,-2],
          [-2,-1]
      ]
      
      if k == 0:
          return 1
      elif n < 3:
          return 0
      
      def knight(curK, r, c):
          
          if r < 0 or r >= n or c < 0 or c >= n:
              return 0
          elif curK == 0:
              return 1
          
          total = 0
          
          for direction in moves:
              
              newRow = r + direction[0]
              newCol = c + direction[1]
              
              total += knight(curK-1, newRow, newCol)
          
          return total/8
              
      return knight(k, row, column)
  
  # Dynamic Programming (Top-Down Memoized Recursive)
  # Time Complexity: O(K*N^2)
  # Space Complexity: O(K*N^2)

  def memoizedKnightProbability(self, n: int, k: int, row: int, column: int) -> float:
      
      # Clockwise, Up Right Down Left
      moves = [
          [-2,1],
          [-1,2],
          [1,2],
          [2,1],
          [2,-1],
          [1,-2],
          [-1,-2],
          [-2,-1]
      ]
      
      memo = {}
      
      if k == 0:
          return 1
      elif n < 3:
          return 0
      
      def knight(curK, r, c):
          
          # Return Memoized result if available
          if (curK, r, c) in memo:
              return memo[(curK,r,c)]
          elif r < 0 or r >= n or c < 0 or c >= n:
              return 0
          elif curK == 0:
              return 1
          
          total = 0
          
          for direction in moves:
              
              newRow = r + direction[0]
              newCol = c + direction[1]
              
              total += knight(curK-1, newRow, newCol)
          
          # Save state of the board in Memo
          memo[(curK,r,c)] = total/8
          return memo[(curK,r,c)]
      
      memo[(k,row,column)] = knight(k, row, column)
      return memo[(k,row,column)]
  
  # Dynamic Programming (Bottom-Up Memoized)
  # Time Complexity: O(K*N^2)
  # Space Complexity: O(K*N^2)

  def bottomUpKnightProbability(self, n: int, k: int, row: int, column: int) -> float:
      
      # Clockwise, Up Right Down Left
      moves = [
          [-2,1],
          [-1,2],
          [1,2],
          [2,1],
          [2,-1],
          [1,-2],
          [-1,-2],
          [-2,-1]
      ]
      
      if k == 0:
          return 1
      elif n < 3:
          return 0
      
      # Initialize DP Grid
      memo = [[[0 for j in range(n)] for i in range(n)] for length in range(k+1)]
      
      # Initialize 1st value at k = 0
      memo[0][row][column] = 1
      
      # Iterate through each element in the matrix at each step at every direction and build up DP Table
      for step in range(1, k+1):
          for r in range(n):
              for c in range(n):
                  for direction in moves:

                      prevRow = r + direction[0]
                      prevCol = c + direction[1]
                      
                      #  Check Boundaries
                      if prevRow >= 0 and prevRow < n and prevCol >= 0 and prevCol < n:
                          
                          # Update table at each step
                          memo[step][r][c] += memo[step-1][prevRow][prevCol] / 8
      
      result = 0
      
      # Sum up result of all element in last table
      for i in range(n):
          for j in range(n):
              
              result += memo[k][i][j]
      
      return result
      
  # Dynamic Programming (Bottom-Up Memoized Optimized)
  # Time Complexity: O(K*N^2)
  # Space Complexity: O(2*N^2) -> Only save 2 grids
  
  def bottomUpOptimizedknightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
    # Clockwise, Up Right Down Left
    moves = [
        [-2,1],
        [-1,2],
        [1,2],
        [2,1],
        [2,-1],
        [1,-2],
        [-1,-2],
        [-2,-1]
    ]
    
    if k == 0:
        return 1
    elif n < 3:
        return 0
    
    # Initialize DP Grids
    prevMemo = [[0 for j in range(n)] for i in range(n)]
    curMemo = [[0 for j in range(n)] for i in range(n)]
    
    # Initialize 1st value at k = 0
    prevMemo[row][column] = 1
    
    # Iterate through each element in the matrix at each step at every direction and build up DP Table
    for step in range(1, k+1):
        for r in range(n):
            for c in range(n):
                for direction in moves:

                    prevRow = r + direction[0]
                    prevCol = c + direction[1]
                    
                    #  Check Boundaries
                    if prevRow >= 0 and prevRow < n and prevCol >= 0 and prevCol < n:
                        
                        curMemo[r][c] += prevMemo[prevRow][prevCol] / 8
        
        prevMemo = curMemo
        curMemo = [[0 for j in range(n)] for i in range(n)]
    
    result = 0
    
    # Sum up result of all element in last table
    for i in range(n):
        for j in range(n):
            
            result += prevMemo[i][j]
    
    return result
