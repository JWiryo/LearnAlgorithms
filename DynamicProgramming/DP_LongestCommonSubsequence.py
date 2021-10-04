class LongestCommonSubsequence:


    # Top Down Recursive with Memo Solution
    # Time Complexity: O(M*N)
    # Space Complexity: O(M*N)
    def memoRecursiveLongestCommonSubsequence(self, text1: str, text2: str) -> int:
      
      # Edge Case
      if len(text1) == 0 or len(text2) == 0:
        return 0
      
      # Setup Memo
      memo = {}
      
      def lcsCounter(i,j):
        
        # Boundary Case
        if i == len(text1) or j == len(text2):
          
          return 0
        
        if (i,j) in memo:
          return memo[(i,j)]
        
        # If characters are equal
        if text1[i] == text2[j]:
          
          # Add diagonal value by 1
          memo[(i,j)] = lcsCounter(i+1,j+1) + 1
          
        else:
          # Check top and left neighbours and get max value
          memo[(i,j)] = max(lcsCounter(i+1,j), lcsCounter(i,j+1))
        
        return memo[(i,j)]
      
      lcsCounter(0,0)
      return memo[(0,0)]

    # Bottom-Up DP Solution
    # Time Complexity: O(M*N)
    # Space Complexity: O(M*N)
    def bottomUpLongestCommonSubsequence(self, text1: str, text2: str) -> int:
      
      # Edge Case
      if len(text1) == 0 or len(text2) == 0:
        return 0
      
      # Setup Memo table with excess 1 dimension on both row and column; this is to setup the "-1" row and columns
      memo = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
      
      # Loop through inner table
      for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
          
          # If 2 characters are equal:
          if text1[i-1] == text2[j-1]:
            
            memo[i][j] = memo[i-1][j-1] + 1
            
          # Else, find the longest common subsequence until that point from its previous column / previous row
          else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])
      
      return memo[len(text1)][len(text2)]