class ClimbStair:

# Dynamic Programming (Top-Down Memoize Recursive)
# Time Complexity: O(N)
# Space Complexity: O(N) -> Maximum call stack is only a single branch down to the bottom of the binary tree even though we perform the call 2^n times
  def climbStairs(self, n: int) -> int:
      
      # Init Memoization
      memo = {}
      
      def climb(n):
          
          # Base Case
          memo[1] = 1
          memo[2] = 2

          # Memoized Existence Check
          if n in memo:
              return memo[n]

          # Recursive Case
          memo[n] = climb(n-1) + climb(n-2)
          return memo[n]
      
      return climb(n)