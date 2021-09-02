from collections import defaultdict

class TopologicalSort:

  # For Directed Acyclic Graph
  def checkCycleTopologicalSort(self, adjList):

      # Create indegree List using defaultdict
      inDegree = defaultdict(int)
      for v, edges in enumerate(adjList):
          inDegree[v]
          for e in edges:
              inDegree[e] += 1
      
      print(inDegree)
      
      # Loop through inDegree
      stack = []
      for node in inDegree:
          if inDegree[node] == 0:
              stack.append(node)
      
      # Check for cycle
      cycleCount = 0
      while stack:
          curNode = stack.pop()
          cycleCount += 1
          
          # Get neighbours
          neighbours = adjList[curNode]
          for neighbour in neighbours:
              
              # Minus off neighbour's indegree value
              inDegree[neighbour] -= 1
              
              if inDegree[neighbour] == 0:
                  stack.append(neighbour)

      return cycleCount == len(adjList)
      
      
          
