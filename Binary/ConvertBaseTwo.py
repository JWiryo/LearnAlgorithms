class BinaryConvertBase2:

  def convertToBinaryTwo(self, num:int) -> str:

    # Prepare stack
    stack = []

    # Keep looping until num reaches 0
    while num:

      # Calculate remainder
      rem = num % 2

      # Push remainder to stack
      stack.append(str(rem))

      # Calculate new num
      num //= 2
    
    # Return reversed stack
    return "".join(stack[::-1])

  def bitConvertToBinaryTwo(self, num:int) -> str:

    # Prepare stack
    stack = []

    # Keep looping until num reaches 0
    while num:

      # Perform bitwise AND with 1, this is the same as N % 2
      rem = num & 1

      # Push remainder to stack
      stack.append(str(rem))

      # Calculate new num by floor division using RIGHT SHIFT of 1
      num >>= 1
    
    # Return reversed stack
    return "".join(stack[::-1])