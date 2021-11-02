class MinMoveToMedian:

    # Sorting Solution
    # Time Complexity: O(NLogN + N)
    # Space Complexity: O(1)
    def minMoves2(self, nums: [int]) -> int:
      
      # Initialise step
      step = 0
      
      # Sort the array
      nums.sort()
      
      # Find median
      length = len(nums)
      ## If Even
      if length % 2 == 0:
        
        median = (nums[length//2] + nums[(length-1)//2]) / 2
      
      ## If Odd
      else:
        
        median = nums[length//2]
      
      # Iterate through nums array
      for num in nums:
        
        # If already equal to median
        if num == median:
          continue
        
        # Add steps with the difference between the number and the median
        step += abs(num - median)
      
      return int(step)
        
        
        