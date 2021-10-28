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