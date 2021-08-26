adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0]
];

class GraphTraversal:

  def adjListBFS(self, adjList):

      # Starting node
      node = 0

      # Initiate queue list
      queue = []
      queue.append(0)

      # Initiate visited dict
      visited = {}

      # Initiate result list
      result = []

      while queue:
        
        # Pop queue
        curNode = queue.pop(0)

        # Add value to result list
        result.append(curNode)

        # Change visited to true
        visited[curNode] = True

        for neighbour in adjList[curNode]:

          # Check if neighbour has been visited
          if neighbour not in visited:
            queue.append(neighbour)
          
      return result
  
  def adjMatrixBFS(self, adjMatrix):

      # Starting node
      node = 0

      # Initiate queue list
      queue = []
      queue.append(0)

      # Initiate visited dict
      visited = {}

      # Initiate result list
      result = []

      while queue:
        
        # Pop queue
        curNode = queue.pop(0)

        # Add value to result list
        result.append(curNode)

        # Change visited to true
        visited[curNode] = True

        for neighbourIdx in range(len(adjMatrix[curNode])):
            
          # Check if neighbour and if neighbour is visited
          if adjMatrix[curNode][neighbourIdx] > 0 and neighbourIdx not in visited:
            queue.append(neighbourIdx)       
          
      return result
