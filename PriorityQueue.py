class PriorityQueue:

  ### Constructor

  def __init__(self):
    self.heap = []

  ### Public Methods

  def size(self):
    return len(self.heap)
  
  def isEmpty(self):
    return len(self.heap) == 0

  def peek(self):
    return self.heap[0]
  
  def push(self, value):

    # Append value to heap
    self.heap.append(value)

    # Sift up
    self.__siftUp()

    return self.size()

  def pop(self):
    
    if self.size() > 1:

      # Swap first and last value
      self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    
    poppedValue = self.heap.pop()

    # Perform Sift Down
    self.__siftDown()

    return poppedValue
  
  def printQueue(self):
    return [i for i in self.heap]
  
  ### Private Methods

  def __parent(self, idx):
    return (idx-1) // 2
  
  def __leftChild(self, idx):
    return (idx*2) + 1
  
  def __rightChild(self, idx):
    return (idx*2) + 2
  
  def __compare(self, i, j):
    return self.heap[i] > self.heap[j]
  
  def __siftUp(self):
    # Get index of last element
    nodeIdx = len(self.heap) - 1
    
    # Iterate until it stops at root
    while nodeIdx > 0 and self.__compare(nodeIdx, self.__parent(nodeIdx)):

      # Perform swap
      self.heap[nodeIdx], self.heap[self.__parent(nodeIdx)] = self.heap[self.__parent(nodeIdx)], self.heap[nodeIdx]
      nodeIdx = self.__parent(nodeIdx)
  
  def __siftDown(self):
    # Get index of first element
    nodeIdx = 0
    size = self.size()

    while (self.__leftChild(nodeIdx) < size and self.__compare(self.__leftChild(nodeIdx), nodeIdx)) or (self.__rightChild(nodeIdx) < size and self.__compare(self.__rightChild(nodeIdx), nodeIdx)):

      # Perform check to see whether left or right child has greater value
      if self.__rightChild(nodeIdx) < size \
      and self.__compare(self.heap[self.__rightChild], self.heap[self.__leftChild]):
        greaterValIdx = self.__rightChild
      else:
        greaterValIdx = self.__leftChild
    
      self.heap[nodeIdx], self.heap[greaterValIdx] = self.heap[greaterValIdx], self.heap[nodeIdx]
      nodeIdx = greaterValIdx
  
