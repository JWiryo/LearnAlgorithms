# Negabinary Math
#     1 + 1 = 0, carry -1
#     -1 + 0 = 1, carry 1
#     1 + 0 = 1, carry 0
#     0 + 0 = 0, carry 0
#     0 + 1 = 1, carry 0
#     -1 + 1 = 0, carry 0
#     -1 + -1 is not possible

class NegaBinary:

    # Backwards Iterative Solution
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def addNegabinary(self, arr1: [int], arr2: [int]) -> [int]:
      
      # Initiate 2 pointers
      p1 = len(arr1) - 1
      p2 = len(arr2) - 1
      
      # Initiate Result Array
      result = []
      
      # Define helper function to do addition
      def addition(val1, val2):
      
        # Starts doing cases
        ## Both are 1
        if val1 == 1 and val2 == 1:
          
          sumVal = 0
          carry = -1
        
        ## Either one is -1
        elif (val1 == -1 and val2 == 0) or (val1 == 0 and val2 == -1):
          
          sumVal = 1
          carry = 1
        
        ## Either one is 1
        elif (val1 == 1 and val2 == 0) or (val1 == 0 and val2 == 1):
          
          sumVal = 1
          carry = 0
        
        # Else if both 0
        else:
          
          sumVal = 0
          carry = 0
        
        return sumVal, carry
          
      # Initiate first carry
      carry = 0
      
      # Iterate through the back
      while p1 >= 0 or p2 >= 0:
        
        curVal = carry
        carry1, carry2 = 0, 0
        
        # Calculate first addition
        if p1 >= 0:
          curVal, carry1 = addition(curVal, arr1[p1])
        
        # Calculate second addition
        if p2 >= 0:
          curVal, carry2 = addition(curVal, arr2[p2])
        
        # Calculate new carry
        carry = carry1 + carry2
        
        # Append answer to result
        result.append(curVal)
        
        # Move pointer
        p1 -= 1
        p2 -= 1
      
      # If carry = -1 at the end
      if carry == -1:
        result = [1,1] + result[::-1]
      else:
        # Just reverse
        result = result[::-1]
      
      # Remove leading zeroes
      for i in range(len(result)):
        
        # Once you see 1, choose itself and the subsequent elements
        if result[i] == 1:
          return result[i:]
        
      return [0]