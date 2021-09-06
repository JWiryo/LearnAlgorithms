# graph = [[0,1,1], [1,2,1],[2,3,1]], n = 4, k = 1 -> 4
class Dijkstra:

  def __init__(self, nodes):

    # Initialize Visited Nodes
    self.vistSet = [0 for i in range(nodes)]

    # Initialize INF value
    self.INF = 1000000

    # Initialize Distance Array
    self.distArray = [self.INF for i in range(nodes)]
    

  def dijkstra(self, graph, nodes, origin):

    # # Initialize Adjacency Matrix
    # adjMatrix = [[0 for j in range(nodes)] for i in range(nodes)]

    # # Fill up adjMatrix
    # for edge in graph:
    #   i = edge[0] - 1
    #   j = edge[1] - 1
    #   adjMatrix[i][j] = edge[2]

    # Initialize Adjacency List
    adjList = {}
    for edge in graph:
      if edge[0] not in graph:
        adjList[edge[0]] = [[edge[1], edge[2]]]
      else:
        adjList[edge[0]].append([edge[1], edge[2]])
    
    # Set Dist Array to INF except origin
    for idx in range(len(self.distArray)):
      if idx == origin:
        self.distArray[idx-1] = 0
      else:
        self.distArray[idx-1] = self.INF
    
    for node in range(nodes):
      
      # Find node with minimum Distance
      minNode = self.__findMinDist()

      # Set that node's visited status to True
      self.vistSet[minNode] = 1

      # Helper code due to my implementation of adjList
      if minNode in adjList.keys():

        for neighbour in adjList[minNode]:
          
          # Calculate path weight to neighbour
          pathWeight = self.distArray[minNode] + neighbour[1]

          # If less than neighbour's current Dist, update it
          if pathWeight < self.distArray[neighbour[0]]:
            self.distArray[neighbour[0]] = pathWeight
      else:
        continue
    
    return self.distArray

  
  def __findMinDist(self):

    # Set Initial Min Value
    min = self.INF

    # Loop through the distArray list for unvisited nodes
    for nodeIdx in range(len(self.distArray)):
      if self.distArray[nodeIdx] < min and self.vistSet[nodeIdx] == 0:
        min = self.distArray[nodeIdx]
        minIdx = nodeIdx
    
    return minIdx
    


    



    



    