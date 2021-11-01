import heapq

class LongestHappyString:

    # Heap Solution
    # Time Complexity: O(A+B+C)
    # Space Complexity: O(A+B+C)
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
      
      # Edge Case
      if a == 0 and b == 0 and c == 0:
        return ""
      
      # Initialise result array
      result = []
      
      # Initialise max heap
      heap = []
      if a != 0:
        heapq.heappush(heap, [-a, 'a'])
      if b != 0:
        heapq.heappush(heap, [-b, 'b'])
      if c != 0:
        heapq.heappush(heap, [-c, 'c'])
      
      # Iterate through heap
      while heap:
        
        # Pop the char with most counts
        count, char = heapq.heappop(heap)
        
        # Check if char is the same as the previous 2 chars
        if len(result) > 1 and (char == result[-2] == result[-1]):
          
          # If heap is empty
          if not heap:
            # Quit looping
            break
          
          # If same chars as previous 2, switch char
          ## IMPORTANT TRICK to switch value without compromising the heap
          count, char = heapq.heapreplace(heap, [count, char])
        
        # Append char to result and increment count otherwise
        result.append(char)
        count += 1
        
        # If count < 0, push the duo back to the heap
        if count != 0:
          heapq.heappush(heap, [count, char])
      
      return "".join(result)