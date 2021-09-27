####################################################
############ OrderedDict #################
####################################################

from collections import OrderedDict

class OrderedDictLRUCache:
    
    # Space Complexity: O(capacity)
    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = OrderedDict()
        
    # Time Complexity: O(1) on Average
    def get(self, key: int) -> int:
        
      # Check if key is in hashmap
      if key in self.cache:

        # Move value to the end as it is recently used
        self.cache.move_to_end(key, last = True)

        # Return value
        return self.cache[key] 
      else:
        return -1
    # Time Complexity: O(1) on Average
    def put(self, key: int, value: int) -> None:
        
      # Check if key is in hashmap
      if key in self.cache:
        
        # Delete the item
        del self.cache[key]
      
      # Add value to orderedDict
      self.cache[key] = value

      # Check if cache size bigger than capacity
      if len(self.cache) > self.capacity:

        # Pop item at beginning of queue
        self.cache.popitem(last = False)        


####################################################
############ Linked List + HashMap #################
####################################################

# Implement a doubly-linked-list
class DoublyLinkedList:
    
    def __init__(self, key, val):
        
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:
    
    # Space Complexity: O(capacity)
    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = {}
        
        # Initialise Head and Tail
        self.head = DoublyLinkedList(-9999, -9999)
        self.tail = DoublyLinkedList(9999, 9999)
        
        # Setup pointers
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # Time Complexity: O(1) on Average
    def get(self, key: int) -> int:
        
        # Check if key is in hashmap
        if key in self.cache:
            
            # Get node from cache
            node = self.cache[key]
            
            # Renew the cache
            self.__remove(node)
            self.__add(node)
            
            # Return node val
            return node.val
        # Otherwise, return -1
        else:
            return -1
        
    # Time Complexity: O(1) on Average
    def put(self, key: int, value: int) -> None:
        
        # Check if key is in hashmap
        if key in self.cache:
            
            # Remove that val from 
            self.__remove(self.cache[key])
        
        # Create new Node
        node = DoublyLinkedList(key, value)
        
        # Add Node to Dictionary
        self.cache[key] = node
        
        # Add Node to LinkedList
        self.__add(node)
        
        # If Size bigger than capacity, remove item beside head
        if len(self.cache) > self.capacity:
            nodeToDelete = self.head.next
            
            # Delete first node after head
            self.__remove(nodeToDelete)
            
            # Delete key-value pair from dictionary
            del self.cache[nodeToDelete.key]
        
    
    # Implement Private Functions to add and remove nodes from linked list
    def __add(self, node):
        
        # Get last node before tail
        lastNode = self.tail.prev
        
        # Add next Node after last Node
        lastNode.next = node
        node.prev = lastNode
        
        # Fix tail to new node
        self.tail.prev = node
        node.next = self.tail
        
    def __remove(self, node):
        
        # Get prev and next node
        prevNode = node.prev
        nextNode = node.next
        
        # Change pointers of prev and next Node
        prevNode.next = nextNode
        nextNode.prev = prevNode