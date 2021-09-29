import Sorting
import PriorityQueue as pq
import MatrixTraversal as mt
import GraphTraversal as gt
import TopologicalSort as ts
import Dijkstra as ds
import BellmanFord as bf

import DynamicProgramming.DP_MinCostStair as mcs
import DynamicProgramming.DP_ClimbStair as cs
import DynamicProgramming.DP_KnightChessboard as kc
import DynamicProgramming.DP_BuySellStocks as bss
import DynamicProgramming.DP_MinPathSum as mps
import DynamicProgramming.DP_UniquePaths as ups
import DynamicProgramming.DP_UniquePathsII as upsII

import Backtracking.SudokuSolver as ss
import Backtracking.Permutation as perm
import Backtracking.Subsets as subs
import Backtracking.PhoneLetterCombinations as plc

import InterfaceDesign.Monarchy as monarchy
import InterfaceDesign.Trie as trie
import InterfaceDesign.LRUCache as cache

import Popular.SpiralMatrix as spiral

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -1, -3]
matrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
];

adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
];

adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0]
];

dijkstraGraph = [
  [0,1,1], 
  [1,2,1],
  [2,3,1]
]
dijkstraN = 4

dutchFlagProblem = [2,0,2,1,1,0,2,0,2,1,1,0,2,0,2,1,1,0,2,0,2,1,1,0]

### Test Sorting Codes Here
# print(Sorting.bubbleSort(numbers))
# print(Sorting.selectionSort(numbers))
# print(Sorting.insertionSort(numbers))
# print(Sorting.mergeSort(numbers))
# print(Sorting.quickSort(numbers, 0, len(numbers)-1))
# print(Sorting.threeWaySort(dutchFlagProblem, 1))

### Test Binary Search Here
# print(Sorting.binarySearch(Sorting.mergeSort(numbers), 4))

### Test Heap & Priority Queue Here
# pq = pq.PriorityQueue()

#### Push Values to heap
# pq.push(5)
# pq.push(10)
# pq.push(8)
# print(pq.printQueue())

# pq.pop()
# print(pq.printQueue())

### Test Matrix Traversal Here
# mt = mt.MatrixTraversal()
# print(mt.arrDFS(matrix))
# print(mt.arrBFS(matrix))
# print(mt.personalArrBFS(matrix))

### Test Graph Traversal Here
# gt = gt.GraphTraversal()
# print(gt.adjListBFS(adjacencyList))
# print(gt.adjMatrixBFS(adjacencyMatrix))
# print(gt.adjListDFS(adjacencyList))
# print(gt.adjMatrixDFS(adjacencyMatrix))

### Test Topological Sort Here
# ts = ts.TopologicalSort()
# print(ts.checkCycleTopologicalSort(adjacencyList))


### Test Dijkstra Here
# ds = ds.Dijkstra(dijkstraN)
# print(ds.dijkstra(dijkstraGraph, dijkstraN, 1))

### Test BellmanFord Here
# bf = bf.BellmanFord()
# print(bf.BellmanFord(dijkstraGraph, dijkstraN, 0))


####################################################
###################### DP ##########################
####################################################

# Test Variables
stairCost = [1,100,1,1,1,100,1,1,100,1]
stairN = 45

### Test DP-MinCostStair Here
# mcs = mcs.MinCostStair()
# print(mcs.bruteForceMinCostClimbingStairs(stairCost))
# print(mcs.memoizedMinCostClimbingStairs(stairCost))
# print(mcs.bottomUpMinCostClimbingStairs(stairCost))
# print(mcs.bottomUpOptimizedMinCostClimbingStairs(stairCost))

### Test DP-ClimbStair Here
# cs = cs.ClimbStair()
# print(cs.climbStairs(stairN))

### Test DP-KnightChessboard Here
# kc = kc.KnightChess()
# print(kc.bruteForceKnightProbability(3,2,0,0))
# print(kc.memoizedKnightProbability(8,30,0,0))
# print(kc.bottomUpKnightProbability(8,30,0,0))
# print(kc.bottomUpOptimizedknightProbability(8,30,0,0))

### Test DP-BuySellStocks Here
stockPrices = [7,1,5,3,6,4]
# bss = bss.BuySellStocks()
# print(bss.bruteForceMaxProfit(stockPrices))
# print(bss.kadaneMaxProfit(stockPrices))

### Test DP-MinPathSum Here
mpsMatrix = [[1,3,1],[1,5,1],[4,2,1]]
# mps = mps.MinimumPathSum()
# print(mps.memoizedMinPathSum(mpsMatrix))

### Test DP-UniquePaths Here
ups = ups.UniquePaths()
# print(ups.bruteForceUniquePaths(7,3))
# print(ups.memoUniquePaths(23,12))

### Test DP-UniquePathsII Here
upsIIObstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# upsII = upsII.UniquePathsII()
# print(upsII.bruteForceUniquePathsWithObstacles(upsIIObstacleGrid))
# print(upsII.memoUniquePathsWithObstacles(upsIIObstacleGrid))

####################################################
################# Backtracking #####################
####################################################

### Test Backtracking-SudokuSolver Here
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# ss = ss.SudokuSolver()
# print(ss.solveSudoku(board))

### Test Backtracking-Permutation Here
numList = [1,2,3]

# perm = perm.Permutation()
# print(perm.permutations(numList))

### Test Backtracking-Subsets Here
# subs = subs.Subset()
# print(subs.subsets(numList))

### Test Backtracking-Phone Letters Combination Here
plc = plc.PhoneLetterComb()
# print(plc.letterCombinations("234"))

####################################################
############### Interface Design ###################
####################################################
# mon = monarchy.Monarchy("Jake")
# mon.birth('Catherine', 'Jake');
# mon.birth('Tom', 'Jake');
# mon.birth('Celine', 'Jake');
# mon.birth('Peter', 'Celine');
# mon.birth('Jane', 'Catherine');
# mon.birth('Farah', 'Jane');
# mon.birth('Mark', 'Catherine');
# mon.death("Jake")
# mon.death("Mark")
# print(mon.orderOfSuccession())

# trie = trie.Trie()
# trie.insert("apple");
# print(trie.search("apple"));   # returns true
# print(trie.search("app"));     # returns false
# print(trie.startsWith("app")); # returns true
# trie.insert("dog")
# trie.insert("app");
# print(trie.search("do")) # returns false
# print(trie.startsWith("do")) # returns true

# cache = cache.LRUCache(2)
# cache = cache.OrderedDictLRUCache(2)
# cache.put(1, 1) # cache is {1=1}
# cache.put(2, 2) # cache is {1=1, 2=2}
# print(cache.get(1))   # return 1
# cache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(cache.get(2))    # returns -1 (not found)
# cache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(cache.get(1))   # return -1 (not found)
# print(cache.get(3))   # return 3
# print(cache.get(4))   # return 4

####################################################
############### Popular Questions ##################
####################################################

### Test Spiral Matrix Here
spiralM = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiral = spiral.SpiralMatrix()
print(spiral.spiralOrder(spiralM))

