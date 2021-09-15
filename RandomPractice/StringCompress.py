# /**
#  * Input: ["a","a","b","b","c","c","c"]
#  *
#  * <p>Output: Return 6, and the first 6 characters of the input array should be:
#  * ["a","2","b","2","c","3"]
#  *
#  * <p>Explanation: "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
#  */

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:

  def StringCompress(listString):

    map = {}

    for character in listString:

      if character in map:
        map[character] += 1

      map[character] = 0
    

    output = []
    for character, count in map.enumerate():

      output.append(character)

      if count > 1:
        output.append(count)
      
    
    return "".join(output)

# /*
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible.
#  If the number of spaces on a line do not divide evenly between words,
#   the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Pseudocode

# Count the number letters in a character
# Need to add space after first character

"This is an", "example of text", "justification."

def extraSpace(words, maxWidth):
  
  countPointer = 1
  nextPointer = 0

  count = 0

  result = []

  while nextPointer < len(words):

    temp = []

    count += len(words[countPointer]) + 1
    temp.append(words[countPointer])
    temp.append(" ")
    if count <= maxWidth:
      countPointer += 1
    else:

      # Exceeded Max Width
      count -= len(words[countPointer]) - 1
      countPointer -= 1
      nextPointer -= 1
      temp.pop()

      result += temp
      
      count = 0
      countPointer = nextPointer
      temp = []
  
# ["This"," ", "is", " ", "an"]
  for sentenceList in result:
    length = lenCalculator(sentenceList) #length of the all the characters
    spacesToFill = maxWidth - length

    spacePointer = 0

    # [1,3]
    indexOfSpaceList = spaceIndexGetter(sentenceList)

    while spacesToFill != 0:

      for idx in indexOfSpaceList:
        
        sentenceList[idx] += " "
        spacesToFill -= 1
    
  return result