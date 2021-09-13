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