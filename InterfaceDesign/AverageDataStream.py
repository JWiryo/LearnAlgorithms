from collections import deque

class MovingAverageDataStream:

    # Queue O(1) Solution
    # Time Complexity: O(1)
    # Space Complexity: O(N)
    def __init__(self, size: int):
      
      # Initiate Queue
      self.size = size
      self.valSum = 0
      self.queue = deque(maxlen = self.size)
        

    def next(self, val: int) -> float:
      
      # If queue length equal to size
      if len(self.queue) == self.size:
        
        # Pop left
        valToReduce = self.queue.popleft()
        
        # Reduce sumVal
        self.valSum -= valToReduce
        
      # Append to end of queue
      self.queue.append(val)
      self.valSum += val

      # Calculate average
      return self.__calculateAverage(self.queue)
        
    
    def __calculateAverage(self, queue):
      
      # Return average
      return self.valSum/len(queue)