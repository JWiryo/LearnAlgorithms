class Permutation:

  # Given a list of items, generate all possible permutations
  # Utilise Backtracking

  # Time Complexity: O(N*N!); N = size of list
  # Space Complexiy: O(N)
  def permutations(self, numList):
    
    # Initialize Result Array
    result = []

    # currentAnswer = temporary answer list
    # currentNumList = current decision space
    def permute(currentAnswer, decisionSpace):

      # Base Case; currentNumList is empty and all inside answer
      if len(decisionSpace) == 0:

        # Add copy of the answer of size 3
        result.append(currentAnswer[:])
        return

      # Start looping through each number in the list
      for element in decisionSpace:
        
        # Add element to currentAnswer
        currentAnswer.append(element)

        # Select next elements to try; Copy to a new variable
        currentDecisionSpace = decisionSpace[:]
        # Remove the element appended to answer
        currentDecisionSpace.remove(element)

        # Perform DFS
        permute(currentAnswer, currentDecisionSpace)

        # Perform Backtracking to previous state
        # Remove last tried element in currentAnswer
        currentAnswer.pop()
    
    permute([], numList)
      
    return result

  # Given a list of items, generate all possible permutations
  # Utilise Backtracking
  def permutationsV2(self, numList):
    
    # Initialize Result Array
    result = []

    # currentAnswer = temporary answer list
    # currentNumList = current decision space
    def permute(currentAnswer, currentNumList):

      # Base Case; currentNumList is empty and all inside answer
      if len(currentNumList) == 0:

        # Add copy of the answer of size 3
        result.append(currentAnswer[:])
        return

      # Start looping through each number in the list
      for idx in range(len(currentNumList)):
        
        # Add element to currentAnswer
        currentAnswer.append(currentNumList[idx])

        # Select next elements to try; Copy to a new variable
        decisionSpace = currentNumList[:idx] + currentNumList[idx+1:]

        # Perform DFS
        permute(currentAnswer, decisionSpace)

        # Perform Backtracking to previous state
        # Remove last tried element in currentAnswer
        currentAnswer.pop()
    
    permute([], numList)
      
    return result






        











