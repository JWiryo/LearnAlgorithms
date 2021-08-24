
class MatrixTraversal:
  # Up, Right, Down, Left
  directions = [[-1,0], \
                [0,1], \
                [1,0], \
                [0,-1] 
              ]

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


    

  
