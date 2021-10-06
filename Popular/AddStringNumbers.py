class AddStringsNumbers:

    # Iterative Solution without converting directly to integer
    # Time Complexity: O(Max(N1,N2))
    # Space Complexity: O(Max(N1,N2))
    def addStrings(self, num1: str, num2: str) -> str:
      
      # Initialise 2 back pointers
      p1 = len(num1) - 1
      p2 = len(num2) - 1
      
      # Initialise Result
      result = []
      
      # Initialise Carry
      carry = 0
      
      # Perform additions
      while p1 >= 0 or p2 >= 0:
        
        # Initiate Vals
        val1 = 0
        val2 = 0
        
        # Calculate value of p1 and p2
        ## Use python's ord() function to convert to integer
        if p1 >= 0:
          
          val1 = int(num1[p1])
        elif p1 < 0:
          val1 = 0
        
        if p2 >= 0:
          
          val2 = int(num2[p2])
        elif p2 < 0:
          val2 = 0
        
        curVal = (val1 + val2 + carry) % 10
        carry =  (val1 + val2 + carry) // 10
        
        # Append to result
        result.append(str(curVal))
        
        # Move Pointers
        p1 -= 1
        p2 -= 1
        
      
      # If there's last carry left
      if carry:
        result.append(str(carry))
      
      # return reversed result
      return "".join(result[::-1])