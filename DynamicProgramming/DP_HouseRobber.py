class HouseRobber:
    
    # Bottom-Up DP Solution
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def rob(self, nums: [int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        # Setup DP Memo hashmap
        memo = {}
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
          
          # Maximum that can be earned in this house is maximum of
          # 1. Robbing this house and 2nd previous house
          # 2. Robbing previous house
          memo[i] = max(memo[i-1], memo[i-2] + nums[i])
          
        
        # Initiate base case
        return memo[len(nums)-1]