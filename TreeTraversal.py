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

# Pseudocode of In-Order DFS non-working implementation
def DFSInOrder(root):

  return traverseInOrder(root, [])
    
def traverseInOrder(node, resultList):

  if node.left:
    traverseInOrder(node.left, resultList)
  
  resultList.append(node.value)

  if node.right:
    traverseInOrder(node.right, resultList)
  
  return resultList

# Pseudocode of Pre-Order DFS non-working implementation
def DFSPreOrder(root):

  return traversePreOrder(root, [])
    
def traversePreOrder(node, resultList):

  resultList.append(node.value)

  if node.left:
    traversePreOrder(node.left, resultList)

  if node.right:
    traversePreOrder(node.right, resultList)
  
  return resultList

# Pseudocode of Post-Order DFS non-working implementation
def DFSPostOrder(root):

  return traversePostOrder(root, [])
    
def traversePostOrder(node, resultList):

  if node.left:
    traversePostOrder(node.left, resultList)

  if node.right:
    traversePostOrder(node.right, resultList)
  
  resultList.append(node.value)
  
  return resultList