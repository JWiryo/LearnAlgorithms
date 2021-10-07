import heapq

class TopKFrequentElements:

    # Heap Solution
    # Time Complexity: O(2*N Log N + N) -> O(N Log N)
    # Space Complexity: O(2N) -> O(N)
    def topKFrequent(self, nums: [int], k: int) -> [int]:
      
      # Initialise Hashmap
      hashmap = {}
      
      # Initialise Heap
      heap = []
      
      # Initialise result array
      result = []
      
      # Perform first pass of calculation -> O(N) time
      for num in nums:
        
        # Increment count if key is in hashmap
        if num in hashmap:
          hashmap[num] += 1
        
        # else, Initialise key-value pair
        else:
          hashmap[num] = 1
      
      # Iterate through hashmap -> O(N Log N)
      for key,value in hashmap.items():
        
        # Push value and key to heap
        heapq.heappush(heap, (-value, key))
      
      # Iterate k times -> O(N Log N)
      for _ in range(k):
        
        # Pop heap
        result.append(heapq.heappop(heap)[1])
      
      return result