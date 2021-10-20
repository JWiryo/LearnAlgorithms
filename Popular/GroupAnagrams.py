class groupAnagrams:

    # Hashmap + Sorted Key Solution
    # Time Complexity: O(N* W Log W); N = Number of Words; W = Length of each word
    # Space Complexity: O(A); A = number of anagrams
    def groupAnagrams(self, strs: [str]) -> [[str]]:
      
      #Edge Case
      if len(strs) <= 1:
        return [strs]
      
      # Initialise Hashmap
      strMap = {}
      
      # Iterate through each word
      for word in strs:
        
        # Sort the word and transform to a string
        sortedWord = "".join(sorted(word))
        
        # Check if the sorted characters in the word are in hashmap
        if sortedWord in strMap:
          
          # If yes, increment count
          strMap[sortedWord].append(word)
          
        else:
          
          # Otherwise, Insert the word into dictionary
          strMap[sortedWord] = [word]
      
      # Initialise result array
      result = []
      
      # Add the anagram to result array
      for anagrams in strMap.values():
        
        result.append(anagrams)
      
      return result
      