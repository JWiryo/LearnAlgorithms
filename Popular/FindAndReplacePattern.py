class FindAndReplace:
    def findAndReplacePattern(self, words: [str], pattern: str) -> [str]:
      
      # Initiate result
      result = []
      
      # Define method to check isomorphism
      def isIsomorph(word):
        
        # Check if their len is actually equal first
        if len(word) != len(pattern):
          
          return False
        
        # Check for isomorphism
        return len(set(word)) == len(set(pattern)) == len(set(zip(word,pattern)))
      
      # Use python filter
      return list(filter(isIsomorph, words))