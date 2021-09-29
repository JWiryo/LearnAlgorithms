class SpiralMatrix:

    # Iterative Solution
    # Time Complexity: O(M*N)
    # Space Complexity: O(M*N)
    def spiralOrder(self, matrix: [[int]]) -> [int]:
      
      # Initialise m and n
      self.m = len(matrix)
      self.n = len(matrix[0])
      
      # Setup Visited matrix
      self.visited = [[0 for j in range(self.n)] for i in range(self.m)]
      
      # Setup counting variables
      steps = 0
      row = 0
      col = 0
      
      # Setup moves [right, down left up]
      moves = [[0,1], [1,0], [0,-1], [-1,0]]
      curMoveIdx = 0
      
      # Setup Solution
      solution = []
      
      # Setup Initial Case
      solution.append(matrix[row][col])
      steps += 1
      self.visited[row][col] = 1
      
      # Keep looping until all visited
      while steps != self.m * self.n:
        
        # Try Current Move (e.g: if right, keep going right)
        curMove = moves[curMoveIdx%4]
        
        # Keep going with current Move
        while self.__isValid(row + curMove[0], col + curMove[1]):
          
          # Update Row and Col
          row += curMove[0]
          col += curMove[1]
          
          # Add to result
          solution.append(matrix[row][col])
          
          # Update Step
          steps += 1

          # Update Visited
          self.visited[row][col] = 1
        
        # Else, change Move
        curMoveIdx += 1
        
      
      return solution
        
        
    def __isValid(self, row, col):
      
      # Boundary Case
      if row < 0 or row >= self.m or col < 0 or col >= self.n:
        return False
      
      # Visited Case
      if self.visited[row][col] == 1:
        return False
      
      return True