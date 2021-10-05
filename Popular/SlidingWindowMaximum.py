from collections import deque

class SlidingWindowMaximum:

    def optimizedMaxSlidingWindow(self, nums: [int], k: int) -> [int]:
      
      # Initialise Result
      result = []
      
      # Initialise Queue to store indexes
      queue = deque()
      
      # Fill in first k elements to queue
      for i in range(k):
        queue = self.__cleanQueue(queue, i, nums, k)
        queue.append(i)
      
      # Get currentMax and append to result
      currentMaxIdx = 0
      
      for i in queue:
        if nums[i] > nums[currentMaxIdx]:
          currentMaxIdx = i
        
      result.append(nums[currentMaxIdx])
      
      # Iterate through rest of array
      for i in range(k, len(nums)):
        
        # Clean-up queue
        queue = self.__cleanQueue(queue, i, nums, k)
        
        # Append item to queue
        queue.append(i)
        
        # Appen item with index from first index in queue to result
        result.append(nums[queue[0]])
      
      return result
    
    # Define helper function to clean queue
    def __cleanQueue(self, queue, idx, nums, k):
      
      # If queue is not empty and first index is not within indexes in sliding window, pop the first index
      if queue and queue[0] == idx - k:
        
        queue.popleft()
      
      # Keep popping indexes that has higher index than currentIdx but has smaller value than it
      while queue and nums[idx] > nums[queue[-1]]:
        
        queue.pop()
      
      return queue
      
      
      
      
# Queue Brute Force Solution
# Time Complexity: O(N*K); N = length of nums
# Space Complexity: O(N)    

    def bruteForceMaxSlidingWindow(self, nums: [int], k: int) -> [int]:
      
      # Initialise Result
      result = []
      
      # Initialise Queue
      queue = deque()
      
      # Fill in first k elements to queue
      for i in range(k):
        queue.append(nums[i])
      
      # Get currentMax and append to result
      currentMax = max(queue)
      result.append(currentMax)
      
      # Iterate through rest of array
      for i in range(k, len(nums)):
        
        # Get value to be added
        currentVal = nums[i]
        
        # Get value to be kicked out
        leftVal = queue.popleft()
        
        # Add value to queue
        queue.append(currentVal)
        
        # If value to be inserted is larger than current max
        if currentVal > currentMax:
          currentMax = currentVal
        
        # If leftVal == currentMax
        if leftVal == currentMax:

            # Get new currentMax
            currentMax = max(queue)
        
        # Append currentMax to result
        result.append(currentMax)
      
      return result
            
        
      
      
      
      
        