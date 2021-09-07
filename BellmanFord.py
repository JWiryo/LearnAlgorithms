# graph = [[0,1,1], [1,2,1],[2,3,1]], n = 4, k = 1 -> 4
class BellmanFord:

  def BellmanFord(self, graph, n, k):

    # Initialise Distances Array
    distMemo = [float("inf") for i in range(n)]
    ## Initialise Origin Distance = 0
    distMemo[k] = 0
    
    # Perform Bellman-Ford for n-1 iterations
    for _ in range(n-1):
        
        # Iterate through the edges
        for edge in graph:
            
            source = edge[0]
            target = edge[1]
            weight = edge[2]
            
            # Compute new weight
            newDist = distMemo[source] + weight

            # Check if new weight is less than memoized weight
            if newDist < distMemo[target]:
                distMemo[target] = newDist
            else:
                continue
    
    return distMemo