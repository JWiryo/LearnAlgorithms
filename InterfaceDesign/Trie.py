# State Assumptions:
# 1. Can we implement helper classes? -> Yes

# Test Cases:
    # trie.insert("apple");
    # console.log(trie.search("apple"));   // returns true
    # console.log(trie.search("app"));     // returns false
    # console.log(trie.startsWith("app")); // returns true
    # trie.insert("dog")
    # trie.insert("app");

# Trie Implementation
# Time Complexity (to create a Trie): O(L * n); L = length of longest word & n = number of word
# Space Complexity: O(l*K); l = length of word, K = memory consumed by each character in word

class Node:
    
    def __init__(self):
        self.keys = {}
        self.end = False
        

class Trie:

    def __init__(self):
        """
        Initialize root node
        """
        self.root = Node()
        
    
    # Time Complexity: O(l); l = length of word
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Start at root
        head = self.root
        
        # Go through each character in word
        for character in word:
            
            # If character not inside keys, create new Node
            if character not in head.keys:
                head.keys[character] = Node()
            
            # Move on to next character
            head = head.keys[character]
        
        # Set ending node's 'end' value to True
        head.end = True
    
    # Time Complexity: O(l); l = length of word
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Start at root
        head = self.root
        
        # Go through each character in word
        for character in word:
            
            if character in head.keys:
                head = head.keys[character]
            else:
                return False
        
        # Return True if End, else return False
        return True if head.end == True else False
        
    # Time Complexity: O(l); l = length of word
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Start at root
        head = self.root
        
        # Go through each character in prefix
        for character in prefix:
            
             # If character inside keys, move on to character node
            if character in head.keys:
                head = head.keys[character]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)