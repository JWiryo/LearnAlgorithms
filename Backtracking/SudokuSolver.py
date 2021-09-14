# State Assumptions:
# 1. Is solution guaranteed? -> Yes
# 2. What happens if board is solved? -> Leave it

# Test Cases:
# 1. 

# Backtracking
# Time Complexity: O(n!^n) -> O(9!)
# Space Complexity: O(1) -> O(81)

class SudokuSolver:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Get size of board
        n = len(board)
        
        # Initialise Hashmaps
        rowMap, colMap, boxMap = {}, {}, {}
        
        # Create set for each index in row, col and box hashmaps
        for i in range(n):
            
            rowMap[i] = set()
            colMap[i] = set()
            boxMap[i] = set()

        # Add values to board
        for i in range(n):
            for j in range(n):
                
                # Get value on board
                val = board[i][j]
                valBoxId = self.getBoxId(i,j)
                
                # Insert to respective hashmaps
                if val != ".":
                    rowMap[i].add(val)
                    colMap[j].add(val)
                    boxMap[valBoxId].add(val)
        
        # Perform backtracking
        self.solveBacktrack(board, rowMap, colMap, boxMap, 0, 0)

        return board
        
    
    def solveBacktrack(self, board, rowMap, colMap, boxMap, startRow, startCol):

        # Boundary Check
        if startRow == len(board) or startCol == len(board[0]):
            return True
        else:
            if board[startRow][startCol] == '.':
                
                # Try ADDITION of value 1 to 9
                for val in range(1, 10):
                    
                    # Assign value to box
                    board[startRow][startCol] = str(val)
                    
                    # Get box ID
                    boxId = self.getBoxId(startRow, startCol)
                    
                    # Get the maps
                    rowSet = rowMap[startRow]
                    colSet = colMap[startCol]
                    boxSet = boxMap[boxId]
                    
                    
                    # DECISION: If Insertion is Valid
                    if self.isValid(val, rowSet, colSet, boxSet):
                        
                        # Add values to the set
                        rowSet.add(str(val))
                        colSet.add(str(val))
                        boxSet.add(str(val))
                        
                        # Recursive Call
                        if startCol == len(board[0]) - 1:
                            
                            if self.solveBacktrack(board, rowMap, colMap, boxMap, startRow + 1, 0):
                                return True
                        else:
                            if self.solveBacktrack(board, rowMap, colMap, boxMap, startRow, startCol + 1):
                                return True
                    
                        # DELETION
                        rowSet.remove(str(val))
                        colSet.remove(str(val))
                        boxSet.remove(str(val))
                
                    # Revert back board state
                    board[startRow][startCol] = "."
                    
            else:
                if startCol == len(board[0]) - 1:
                    if self.solveBacktrack(board, rowMap, colMap, boxMap, startRow + 1, 0):
                        return True
                else:
                    if self.solveBacktrack(board, rowMap, colMap, boxMap, startRow, startCol + 1):
                        return True
                        
        return False
                    
        
    
    # Check Validity of Solution
    def isValid(self, val, rowSet, colSet, boxSet):
        
        if str(val) in rowSet or str(val) in colSet or str(val) in boxSet:
            return False
        
        return True
        
    
    # Get Index of 3x3 Box that value is in
    def getBoxId(self, row, col):
        
        # Floor Division of column to get box column index
        colVal = col // 3
        
        # Floor Division of row to get box row index
        rowVal = row // 3 * 3
        
        return rowVal + colVal
        
        
        