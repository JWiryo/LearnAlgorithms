
class MatrixTraversal:
  # Up, Right, Down, Left
  directions = [[-1,0], \
                [0,1], \
                [1,0], \
                [0,-1] 
              ]
  
  # Udemy Implementation of BFS
  def arrBFS(self, matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    # Setup visited and result list
    seen = [[False for i in range(cols)] for j in range(rows)]
    result = []

    queue = [] #queue can get really large
    queue.append([0,0]) # Start from node at Row 2 and Col 2

    # Iterative loop
    while queue:
      
      # Pop item from queue
      current = queue.pop(0)
      curRow = current[0]
      curCol = current[1]

      if curRow < 0 or curCol < 0 or curRow >= len(matrix) or curCol >= len(matrix[0]) or seen[curRow][curCol]:
        # If any of this happens, skip the next session within the while loop
        continue
      
      # Update Visited List
      seen[curRow][curCol] = True
      # Update Result List
      result.append(matrix[curRow][curCol])

      # Attempt all directions
      for i in range(len(self.directions)):

        # Get current direction
        dir = self.directions[i]

        queue.append([curRow + dir[0], curCol + dir[1]])
      
    return result

  def arrDFS(self, matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Setup visited and result list
    seen = [[False for i in range(cols)] for j in range(rows)]
    result = []

    # Initialise Recursion from 0,0
    self.__dfs(matrix, 0, 0, seen, result)

    return result

  ## Private DFS Method
  def __dfs(self, matrix, row, col, seen_arr, result_arr):
    
    # Out of Bounds Condition and Seen == True Condition
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen_arr[row][col]:
      return
    
    # Update Results List
    result_arr.append(matrix[row][col])
    # Update Visited list
    seen_arr[row][col] = True

    # Recursive calls; attempt all directions
    for i in range(len(self.directions)):

      # Get current direction
      dir = self.directions[i]

      # Recursive
      self.__dfs(matrix, row + dir[0], col + dir[1], seen_arr, result_arr)


# # Personal Implementation of BFS
  def personalArrBFS(self, matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    # Setup visited and result list
    seen = [[False for i in range(cols)] for j in range(rows)]
    result = []

    queue = [] #queue can get really large
    queue.append([0,0]) # Start from node at Row 0 and Col 0

    # Iterative loop
    while queue:
      
      # Pop item from queue
      current = queue.pop(0)
      curRow = current[0]
      curCol = current[1]

      # Add element to result
      result.append(matrix[curRow][curCol])

      # Change seen at current node to True
      seen[curRow][curCol] = True

      for i in range(len(self.directions)):
          
        # Get current direction
        dir = self.directions[i]

        # Try all possible directions and add to queue
        if (curRow + dir[0] >= 0 and curRow + dir[0] < len(matrix))\
        and curCol + dir[1] >= 0 and curCol + dir[1] < len(matrix[0])\
        and not seen[curRow + dir[0]][curCol + dir[1]]:

          # Add node to queue
          queue.append([curRow + dir[0], curCol + dir[1]])

          # Change seen at next node to True
          seen[curRow + dir[0]][curCol + dir[1]] = True
      
    return result


    

  
