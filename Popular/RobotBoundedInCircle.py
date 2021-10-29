class RobotCircle:

    # Brute Force Solution
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def isRobotBounded(self, instructions: str) -> bool:
      
      # Initiate array for Moves [North, East, South, West]
      movements = [[0,1], [1,0], [0,-1], [-1,0]]
      
      # Initial Move = North
      moveIdx = 0
      
      # Initiate Vector
      vector = [0,0]
      
      # Iterate through instructions
      for inst in instructions:
        
        # if "L"
        if inst == "L":
          
          # Rotate Counter Clockwise to the West
          moveIdx = (moveIdx + 3) % 4
        
        # elif "R" to the east
        elif inst == "R":
          
          # Rotate Clockwise
          moveIdx = (moveIdx + 1) % 4
        
        # Else, go straight (add to vector)
        else:
          move = movements[moveIdx]
          vector[0] += move[0]
          vector[1] += move[1]

      # Check if they're back in origin OR direction is not facing north
      if vector == [0,0] or moveIdx != 0:
        return True
      else:
        return False