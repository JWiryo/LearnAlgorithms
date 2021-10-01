class MaxLengthRepeatSubArray:

    # Bottom Up DP Solution
    # Time Complexity: O(N1*N2); N1 = length of nums1; N2 = length of nums2
    # Space Complexity: O(N1*N2)
    def findLength(self, nums1: [int], nums2: [int]) -> int:
      
      # Setup Memo
      memo = {}
      
      # Fill up initial DP memo
      ## Fill first row
      for i in range(len(nums1)):
        
        if nums1[i] == nums2[0]:
          memo[(i,0)] = 1
        else:
          memo[(i,0)] = 0
      
      ## Fill first column
      for j in range(len(nums2)):
        
        if nums1[0] == nums2[j]:
          memo[(0,j)] = 1
        else:
          memo[(0,j)] = 0
      
      # Fill up DP Table
      for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
          
          # If nums1[i][j] equal to nums2[i][j], add from previous memo
          if nums1[i] == nums2[j]:
            
            # Check Previous diagonal
            memo[(i,j)] = memo[(i-1,j-1)] + 1
          
          else:
            # Else, just put it as 0
            memo[(i,j)] = 0
      
      # Return max value in memo
      return max(memo.values())