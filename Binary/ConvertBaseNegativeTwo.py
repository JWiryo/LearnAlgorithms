class BinaryConvertBaseNegative2:

    # Math Solution
    # Time Complexity: O(N); N = number of digits in the negabinary representation
    # Space Complexity: O(N)
    def baseNeg2(self, n: int) -> str:
      
      # Edge Case
      if n == 0:
        return "0"
      
      # Initiate base
      base = -2
      
      # Answer
      ansStack = []
      
      # Keep looping until n is finished
      while n:
        
        # Calculate remainder
        rem = n % base
        
        # Calculate new n
        n = n // base
        
        # Check if remainder is negative
        if rem < 0:
          
          # Add absolute value of the base to remainder
          rem += abs(base)
          
          # Add 1 to quotient
          n += 1
        
        # Push remainder to stack
        ansStack.append(str(rem))
      
      # Return reversed stack
      return "".join(ansStack[::-1])

    def bitBaseNeg2(self, n:int) -> str:

        # Prepare stack
        stack = []

        # Keep looping until num reaches 0
        while n:

          # Perform bitwise AND with 1, this is the same as N % 2
          rem = n & 1

          # Push remainder to stack
          stack.append(str(rem))

          # Calculate new num by floor division using RIGHT SHIFT of 1
          n = -(n >> 1)
        
        # Return reversed stack
        return "".join(stack[::-1])