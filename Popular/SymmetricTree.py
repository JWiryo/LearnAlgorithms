class SymmetricTree:

    # Level-Order Solution
    # Time Complexity: O(2N) -> O(N); N = nodes in tree
    # Space Complexity: O(2W) -> O(W); W = max width of tree
    def isSymmetric(self, root) -> bool:
      
      # Initiate queue
      queue = []
      
      # Initiate array to store values of nodes
      val = []
      
      # Add first value to queue and val
      queue.append(root)
      val.append(root.val)
      
      # Perform BFS
      while queue:
        
        # Get current level
        level = len(queue)
        
        if not self.isMirror(val):
          return False
        
        # Reset value of val
        val = []
        
        # Iterate through level
        for _ in range(level):
        
          # Get Node
          node = queue.pop(0)
          
          # Add node left
          if node.left:
            queue.append(node.left)
            val.append(node.left.val)
          else:
            val.append(None)
          
          # Add node right
          if node.right:
            queue.append(node.right)
            val.append(node.right.val)
          else:
            val.append(None)
        
      return True
    
    # Helper function to check if values mirror each other
    def isMirror(self, queue):
      
      length = len(queue)
      
      if length <= 1:
        return True
      
      # Check if the queue is mirroring each other
      for i in range(length // 2):
        
        if queue[i] != queue[length-1-i]:
          return False
        
      return True