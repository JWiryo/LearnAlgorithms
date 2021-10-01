class MinimumKnightMoves:

    # Symmetry Trick for this problem:
    # Technically, this problem is symmetrical in nature, regardless of x or y being positive or negative, going from 0,0 to the target in the minimum of steps is identical, we can limit our search to the positive quadrants of x and y and would still be achieved. Instead of trying all 8 moves, we could move only on the positive side and perform DFS on that side.

    # Level-Order BFS Solution
    # Time Complexity: O(Max(2|x|, 2|y|)^2); Due to nature of BFS, will try all cells in the circle, in the chessboard case it kind of looks like a square where 2x or 2y = length of square
    # Space Complexity: O(Max(|x|, |y|)^2 + Max(|x|, |y|)); Set will contain all visited cells
    def minKnightMoves(self, x: int, y: int) -> int:
      
      # Setup moves
      ## Clockwise, Up Right Down Left
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
      
      # Setup Variables
      steps = 0
      
      # Setup visited node
      visited = set()
      
      # Setup queue
      queue = []
      queue.append([0,0])
      
      # Perform BFS by level
      while queue:
        
        # Get current level
        level = len(queue)
        
        # Iterate by Level
        for _ in range(level):
          # Pop coordinate
          coord = queue.pop(0)
          curX = coord[0]
          curY = coord[1]

          # Stop if reached goal
          if curX == x and curY == y:
            return steps

          # Try all possible directions
          for move in moves:

            # Get new X and new Y
            newX = curX + move[0]
            newY = curY + move[1]
            
            # If next coordinate is in visited, skip:
            if (newX, newY) in visited:
              continue

            # Else, Append to queue and visited
            queue.append([newX, newY])
            visited.add((newX,newY))

        # Increment count
        steps += 1
      
      return steps