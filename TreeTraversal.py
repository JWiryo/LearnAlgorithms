# Pseudocode of BFS non-working implementation
def BFS(root):

  currentNode = root
  result = []
  queue = [] #queue can get really large
  queue.append(currentNode)

  while len(queue) > 0:

    # Dequeue
    currentNode = queue.pop(0)

    # Add value to result
    result.append(currentNode.val)

    if currentNode.left:
      queue.append(currentNode.left)

    if currentNode.right:
      queue.append(currentNode.right)
  
  return result
    
