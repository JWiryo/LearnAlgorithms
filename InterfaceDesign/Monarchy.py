class Royal:

  def __init__(self, name: str):
    self.name = name
    self.isAlive = True
    self.children = []

class Monarchy:

  def __init__(self, monarch: str):
    self.king = Royal(monarch)
    self.monarchyMap = {monarch: self.king}

  def birth(self, name: str, parent: str):

    # Create Royal self
    selfRoyal = Royal(name)
    
    # Find parent
    parentRoyal = self.monarchyMap[parent]

    # Add to parent's succession
    parentRoyal.children.append(name)

    # Add self to monarchyMap
    self.monarchyMap[name] = selfRoyal
  
  def death(self, name: str):
    
    # Find self
    selfRoyal = self.monarchyMap[name]

    # Set isAlive to False
    selfRoyal.isAlive = False
  
  def orderOfSuccession(self) -> []:

    succession = []
    # Perform Pre-Order DFS traversal
    def dfs(royalName: str):
      
      # Base case
      if not royalName:
        return

      # Get selfRoyal
      selfRoyal = self.monarchyMap[royalName]
      
      # Append self to succession (Pre-Order)
      if selfRoyal.isAlive:
        succession.append(selfRoyal.name)
      
      # Recurse DFS
      for children in selfRoyal.children:
        dfs(children)
    
    # Initialise dfs call
    dfs(self.king.name)

    # Return line of succession
    return succession
