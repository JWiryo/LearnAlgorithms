class SimpleHashMap:

    def __init__(self):
      # Initiate large array
      self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
      
      # Update value of that index
      self.map[key] = value
        

    def get(self, key: int) -> int:
      
      # Check if index key inside map has value
      if self.map[key] != None:
        
        return self.map[key]
      
      # Otherwise
      return -1

    def remove(self, key: int) -> None:
      
      # Check if index key inside map has value
      if self.map[key] != None:
        
        self.map[key] = None