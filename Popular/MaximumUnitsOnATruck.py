class MaximumUnitsTruck:

    # Sorting + GreedySolution
    # Time Complexity: O(N Log N + N) -> O(N Log N)
    # Space Complexity: O(1)
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
      
      # Initiate current load and current units
      currLoad = 0
      currUnits = 0
      
      # Initiate counter
      boxIdx = 0
      
      # Sort based on most number of units
      boxTypes.sort(key=lambda x:x[1], reverse = True)
      
      # Iterate while truck is not full
      while currLoad < truckSize and boxIdx < len(boxTypes):
        
        # Get variables
        numBoxes = boxTypes[boxIdx][0]
        unitPerBox = boxTypes[boxIdx][1]
        
        # Get remaining space
        remaining = truckSize - currLoad
        
        # If we can put in full load
        if remaining >= numBoxes:
          
          # Insert into truck
          currLoad += numBoxes
          currUnits += numBoxes * unitPerBox
        
        # If there's still a bit of space
        elif remaining > 0 and remaining < numBoxes:
          
          # Insert into truck remaining
          currLoad += remaining
          currUnits += remaining * unitPerBox
        
        # Iterate to next box
        boxIdx += 1
      
      return currUnits