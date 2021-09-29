class UniquePathsII:

    # Brute Force Recursive Solution
    # Time Complexity: O(2^(M+N))
    # Space Complexity: O(M+N)
    def bruteForceUniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
      
      # Setup moves (Right and Down)
      moves = [[0,1], [1,0]]
      
      # Setup m and n
      m = len(obstacleGrid)
      n = len(obstacleGrid[0])
      
      # Global count variable
      self.count = 0
      
      # Define helper function
      def findPath(row, col):
        
        # Boundary Cases and obstacle case
        if row < 0 or row >= m or col < 0 or col >= n or obstacleGrid[row][col] == 1:
          return 0
        
        # Goal case
        if row == m-1 and col == n-1:
          self.count += 1
          return
        
        # Next Moves
        rightMove = moves[0]
        downMove = moves[1]
        
        # Perform Next Moves
        findPath(row + rightMove[0], col + rightMove[1])
        findPath(row + downMove[0], col + downMove[1])
      
      # Initialise Base Recursion
      findPath(0,0)
      
      return self.count

    def memoUniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
      
      # Setup moves (Right and Down)
      moves = [[0,1], [1,0]]
      
      # Setup m and n
      m = len(obstacleGrid)
      n = len(obstacleGrid[0])
      
       # Edge Case
      if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 0:
        return 1
      elif len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 1:
        return 0
      elif obstacleGrid[0][0] == 1:
        return 0
      
      # Setup Memoization Map
      memo = {}
      
      # Define helper function
      def findPath(row, col):
        
        if (row,col) in memo:
          return memo[(row,col)]
        
        # Boundary Cases and obstacle case
        if row < 0 or row >= m or col < 0 or col >= n or obstacleGrid[row][col] == 1:
          return 0
        
        # Goal case
        if row == m-1 and col == n-1:
          
          # Add value when reaching 1
          return 1
        
        # Next Moves
        rightMove = moves[0]
        downMove = moves[1]
        
        # Perform Next Moves
        memo[(row,col)] = findPath(row + rightMove[0], col + rightMove[1]) + findPath(row + downMove[0], col + downMove[1])
        return memo[(row,col)]
      
      # Initialise Base Recursion
      findPath(0,0)
      
      return memo[(0,0)]