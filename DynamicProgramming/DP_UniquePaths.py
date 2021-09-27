# Brute Force Recursive DP Solution
# Time Complexity: O(2^(M+N))
# Space Complexity: O(M+N)

class UniquePaths:
  def bruteForceUniquePaths(self, m: int, n: int) -> int:
      
    # Movement List -> Down, Right
    moves = [[1,0], [0,1]]
    
    # Setup global count variable
    self.count = 0
    
    def findPath(row, col):
        
        # Boundary checks
        if row < 0 or row >= m or col < 0 or col >= n:
          return
        
        # Bottom-Right-most grid
        if row == m-1 and col == n-1:
          
          # Add count when path reaches finish line
          self.count += 1
        
        # Next movements
        downMove = moves[0]
        rightMove = moves[1]
            
        # Attempt paths for down and right
        findPath(row + downMove[0], col + downMove[1])
        findPath(row + rightMove[0], col + rightMove[1])
    
    # initialise Recursion
    minSum = findPath(0,0)
    
    return self.count

# Top-Down Recursive DP Solution
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

  def memoUniquePaths(self, m: int, n: int) -> int:
    
    if m == 1 and n == 1:
      return 1
    
    # Initialise Memo
    memo = {}
      
    # Movement List -> Down, Right
    moves = [[1,0], [0,1]]

    def findPath(row, col):
      
      if (row,col) in memo:
        return memo[(row,col)]

      # Boundary checks
      if row < 0 or row >= m or col < 0 or col >= n:
        return 0

      # Bottom-Right-most grid
      if row == m-1 and col == n-1:

        # Add count when path reaches finish line
        return 1

      # Next movements
      downMove = moves[0]
      rightMove = moves[1]

      # Attempt paths for down and right
      memo[(row,col)] = findPath(row + downMove[0], col + downMove[1]) + findPath(row + rightMove[0], col + rightMove[1])
      return memo[(row,col)]

    # initialise Recursion
    minSum = findPath(0,0)
    
    # Return memo[(0,0)] because we're building up the results from the bottom
    return memo[(0,0)]
        