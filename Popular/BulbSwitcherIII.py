class BulbSwitcherIII:
    def bruteForceNumTimesAllBlue(self, light: [int]) -> int:
      
      # Setup Variables
      onBulbs = 0
      on = 1
      
      # Setup bulbList -> O(N) space
      bulbList = [0] * len(light)
      
      # Initate result
      result = 0
      
      # Iterate through moments -> O(N) time
      for moment in range(len(light)):
        
        # Initialise blue
        blue = 0
        
        # Get bulb to be turned on
        bulb = light[moment]
        bulbList[bulb-1] = on
        
        # Increment number of on bulbs
        onBulbs += 1
        
        # Check if number of onBulbs >= bulb, otherwise, it's probably less and don't even bother calculating
        if onBulbs < bulb:
          continue
        
        # Calculate blue -> O(N) time
        i = 0
        while bulbList[i] != 0 and i < len(bulbList)-1:
          blue += 1
          i += 1
        
        if blue == onBulbs or onBulbs == len(light):
          result += 1
      
      return result

# Optimized Solution
# Time Complexity: O(N)
# Space Complexity: O(1)

    def optimizedNumTimesAllBlue(self, light: [int]) -> int:
      
      # Setup Variables
      onBulbs = 0
      requiredBulbs = 0
      
      # Initiate result
      result = 0
      
      # Iterate through moments
      for moment in range(len(light)):
        
        # Get bulb number
        bulbNum = light[moment]
        
        # Increment switched on bulbs
        onBulbs += 1
        
        # This means that require all bulbs before it to switch on to be consider blue moment
        ## If bulb number is higher than the current required number of bulbs, we replace
        if bulbNum > requiredBulbs:
          requiredBulbs = bulbNum
        
        # If the number of on bulbs is greater than the required amount, we increment result
        if onBulbs >= requiredBulbs:
          result += 1
      
      return result