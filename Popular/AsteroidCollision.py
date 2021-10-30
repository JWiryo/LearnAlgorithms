class Asteroid:

      # Stack Solution
      # Time Complexity: O(N)
      # Space Complexity: O(N)
    def asteroidCollision(self, asteroids: [int]) -> [int]:
      

      # Initialise stack
      stack = []
      
      # Iterate through asteroids
      for rock in asteroids:
        
        # If stack is empty or rock going right
        if not stack or rock > 0:
          
          # Append to stack
          stack.append(rock)
        
        # If rock going left [negative]
        else:
          
          # Collision may occur
          collision = True
          while stack and collision:
            
            # Get previous rock
            prevRock = stack[-1]
            
            # If previous rock going left, no collision occur
            if prevRock < 0:
              
              stack.append(rock)
              collision = False
            
            # Else if its going right
            else:
              
              # If same size, both breaks
              if abs(prevRock) == abs(rock):
                
                stack.pop()
                collision = False
              
              elif abs(prevRock) > abs(rock):
                
                collision = False
              
              else:
                
                stack.pop()
                
                # Edge case if stack becomes empty
                if not stack:
                  stack.append(rock)
                  collision = False
      
      return stack