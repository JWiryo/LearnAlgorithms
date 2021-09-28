class PhoneLetterComb:

  # Recursive Backtracking Solution
  # Time Complexity: O(N*N^N)
  # Space Complexity: O(N^N + N)
  def letterCombinations(self, digits: str) -> [str]:
    
    # Edge Case
    if len(digits) == 0:
      return []
    
    # Setup Hashmap
    dlMap = {}
    dlMap["2"] = ["a", "b", "c"]
    dlMap["3"] = ["d", "e", "f"]
    dlMap["4"] = ["g", "h", "i"]
    dlMap["5"] = ["j", "k", "l"]
    dlMap["6"] = ["m", "n", "o"]
    dlMap["7"] = ["p", "q", "r", "s"]
    dlMap["8"] = ["t", "u", "v"]
    dlMap["9"] = ["w", "x", "y", "z"]
    
    # Setup solution set and decision space
    solution = []
    decisionSpace = []
    
    # Add list of letters into decision space
    for digit in digits:
      decisionSpace.append(dlMap[digit])
    
    # Define Helper Function
    def combine(currentAnswer, decisionSpace, idx):
      
      # Base Case -> Copying is done so O(N) where N = length of digits
      if len(currentAnswer) == len(digits):
        solution.append("".join(currentAnswer[:]))
        return
      
      # Iterate through decisionSpace Lists -> O(N!) = O(N^N)
      for i in range(idx, len(decisionSpace)):
        for j in range(len(decisionSpace[i])):
          
          # Append the current word to current Answer
          currentAnswer.append((decisionSpace[i][j]))
          
          # Recurse
          combine(currentAnswer, decisionSpace, i+1)
          
          # Backtrack
          currentAnswer.pop()
    
    # Base Recursion
    combine([], decisionSpace, 0)
    return solution