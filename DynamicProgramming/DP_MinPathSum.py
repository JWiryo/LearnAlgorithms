class MinimumPathSum:

# Top-Down Recursive Solution
# Time Complexity: O(2^M*N)
# Space Complexity: O(2^M*N)

    def bruteForceMinPathSum(self, grid: [[int]]) -> int:
        
        # Movement List -> Down, Right
        moves = [[1,0], [0,1]]
        
        # Setup variables
        m = len(grid)
        n = len(grid[0])
        
        def findPath(row, col, valSum):
            
            # Boundary checks
            if row < 0 or row >= m or col < 0 or col >= n:
                return 9999
            
            # Bottom-Right-most grid
            if row == m-1 and col == n-1:
                valSum += grid[row][col]
                return valSum
            
            # Add current value
            valSum += grid[row][col]
            
            # Next movements
            downMove = moves[0]
            rightMove = moves[1]
                
            # Return minimum for down and right
            return min(findPath(row + downMove[0], col + downMove[1], valSum), findPath(row + rightMove[0], col + rightMove[1], valSum))
        
        # initialise Recursion
        minSum = findPath(0,0,0)
        
        return minSum

# Top-Down Recursive DP Solution
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

    def memoizedMinPathSum(self, grid: [[int]]) -> int:
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        
        # Initiate Memo
        memo = {}
        
        # Movement List -> Down, Right
        moves = [[1,0], [0,1]]
        
        # Setup variables
        m = len(grid)
        n = len(grid[0])
        
        
        def findPath(row, col):
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            # Boundary checks
            if row < 0 or row >= m or col < 0 or col >= n:
                return float('inf')
            
            # Bottom-Right-most grid / end goal
            if row == m-1 and col == n-1:
                
                # Return its own value
                return grid[row][col]
            
            # Get current value
            curVal = grid[row][col]
            
            # Next movements
            downMove = moves[0]
            rightMove = moves[1]
                
            # Return minimum for down and right
            # Reminder to always add up the curVal in recursion during comparison (if there is comparison)
            memo[(row,col)] = min(findPath(row + downMove[0], col + downMove[1]) + curVal, findPath(row + rightMove[0], col + rightMove[1]) + curVal)
            return memo[(row,col)]
        
        # initialise Recursion
        findPath(0, 0)
        
        return memo[(0,0)]
            
            
                
                
            
        