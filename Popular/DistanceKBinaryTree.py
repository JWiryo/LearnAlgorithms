# Graph Solution
class DistanceKBinaryTree:

    # Time Complexity: O(N); N = number of nodes
    # Space Complexity: O(Log N + W); W = max num of neighbours at each level
    def distanceK(self, root, target, k: int) -> [int]:
      
      # Edge Case
      if k == 0:
        return [target.val]
      
      # Initiate adjList and visitedList
      adjList = {}
      visited = {}
      
      # Define helper buildGraph method
      def buildGraph(node, parent):
        
        # Base Case
        if not node:
          return
        
        # Insert current node to adjList
        nodeVal = node.val
        if nodeVal not in adjList:
          
          adjList[nodeVal] = []
          visited[nodeVal] = 0
          
        # Insert its neighbours
        if parent:
          adjList[nodeVal].append(parent.val)
        
        if node.left:
          adjList[nodeVal].append(node.left.val)
          buildGraph(node.left, node)
        
        if node.right:
          adjList[nodeVal].append(node.right.val)
          buildGraph(node.right, node)
        
        
      # Initialise build graph
      buildGraph(root, None)
      
      # Initiate queue
      queue = []
      fromTarget = 1
      
      # Fill up queue
      queue.extend(adjList[target.val])
      visited[target.val] = 1
      
      
      # Perform BFS
      while queue:
        
        level = len(queue)
        
        # Once reached the target distance
        if fromTarget == k:
          break
        
        # Iterate through each level
        for _ in range(level):
          
          # Get current node
          node = queue.pop(0)
          
          # Find its neighbour
          for neighbour in adjList[node]:
            
             # Check Visited
            if visited[neighbour] == 1:
              continue
            
            # Append neighbour
            queue.append(neighbour)
          
          # Update visited
          visited[node] = 1
        
        # Update distance from target
        fromTarget += 1
        
      return queue