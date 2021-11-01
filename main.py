import Sorting
import PriorityQueue as pq
import MatrixTraversal as mt
import GraphTraversal as gt
import TopologicalSort as ts
import Dijkstra as ds
import BellmanFord as bf

import Binary.ConvertBaseTwo as cbtwo
import Binary.ConvertBaseNegativeTwo as cbnegtwo

import DynamicProgramming.DP_MinCostStair as mcs
import DynamicProgramming.DP_ClimbStair as cs
import DynamicProgramming.DP_KnightChessboard as kc
import DynamicProgramming.DP_BuySellStocks as bss
import DynamicProgramming.DP_MinPathSum as mps
import DynamicProgramming.DP_UniquePaths as ups
import DynamicProgramming.DP_UniquePathsII as upsII
import DynamicProgramming.DP_MaxLengthOfRepeatedSubArray as mlrs
import DynamicProgramming.DP_LongestCommonSubsequence as lcs
import DynamicProgramming.DP_CoinChange as coin
import DynamicProgramming.DP_TargetSum as ts
import DynamicProgramming.DP_HouseRobber as hr
import DynamicProgramming.DP_PascalTriangle as ptri

import Backtracking.SudokuSolver as ss
import Backtracking.Permutation as perm
import Backtracking.Subsets as subs
import Backtracking.PhoneLetterCombinations as plc
import Backtracking.CombinationSum as combsum

import InterfaceDesign.Monarchy as monarchy
import InterfaceDesign.Trie as trie
import InterfaceDesign.LRUCache as cache
import InterfaceDesign.MyCalendar as cal
import InterfaceDesign.AverageDataStream as avgdatastream
import InterfaceDesign.SparseVector as sparsevec

import Popular.SpiralMatrix as spiral
import Popular.MinimumKnightMoves as mkm
import Popular.SlidingWindowMaximum as swm
import Popular.AddNegabinaryNumbers as anbn
import Popular.BulbSwitcherIII as bsIII
import Popular.AddStringNumbers as asn
import Popular.TopKFrequentElements as tkfe
import Popular.GroupAnagrams as gana
import Popular.FindAndReplacePattern as fandr
import Popular.RobotBoundedInCircle as robotcircle
import Popular.AsteroidCollision as asteroidcoll
import Popular.LongestHappyString as longhapstring

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
# print(Sorting.binarySearchRotated([4,5,7,0,1,2,3], 2))

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
#################### Binary ########################
####################################################

# Test Base 2 Conversion
# cbtwo = cbtwo.BinaryConvertBase2()
# print(cbtwo.convertToBinaryTwo(195))
# print(cbtwo.bitConvertToBinaryTwo(195))

# Test Base -2 Conversion
# cbnegtwo = cbnegtwo.BinaryConvertBaseNegative2()
# print(cbnegtwo.baseNeg2(100))
# print(cbnegtwo.bitBaseNeg2(100))

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

### Test DP-MaxLengthOfRepeatedSubArray Here
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,5]
# mlrs = mlrs.MaxLengthRepeatSubArray()
# print(mlrs.findLength(nums1, nums2))

### Test DP-LongestCommonSubsequence Here
lcsText1 = "ylqpejqbalahwr"
lcsText2 = "yrkzavgdmdgtqpg"
# lcs = lcs.LongestCommonSubsequence()
# print(lcs.memoRecursiveLongestCommonSubsequence(lcsText1, lcsText2))
# print(lcs.bottomUpLongestCommonSubsequence(lcsText1, lcsText2))

### Test DP-CoinChange Here
# coin = coin.CoinChange()
# print(coin.memoCoinChange([1,2,3,4,5], 25))
# print(coin.bottomUpCoinChange([1,2,3,4,5], 25))

### Test DP-TargetSum Here
# targetSum = [1,1,1,1,1]
# targetTarget = 3
# ts = ts.TargetSum()
# print(ts.findTargetSumWays(targetSum, targetTarget))

### Test DP-HouseRobber Here
# hrHouse = [1,2,3,4,5]
# hr = hr.HouseRobber()
# print(hr.rob(hrHouse))

### Test DP-PascalTriangle Here
# pascalNumRows = 5
# ptri = ptri.PascalTriangle()
# print(ptri.generate(pascalNumRows))

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
# plc = plc.PhoneLetterComb()
# print(plc.letterCombinations("234"))

### Test Backtracking-Combination Sum  Here
# csCandidates = [2,3,5,6,7]
# csTarget = 8
# combsum = combsum.CombinationSum()
# print(combsum.combinationSum(csCandidates, csTarget))


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

# calendar = cal.MyCalendar()
# print(calendar.book(10,20)) # True
# print(calendar.book(15,25)) # False
# print(calendar.book(30,45)) # True

# avgdatastream = avgdatastream.MovingAverageDataStream(3)
# print(avgdatastream.next(1))
# print(avgdatastream.next(2))
# print(avgdatastream.next(3))
# print(avgdatastream.next(4))

# sparsevec1 = sparsevec.SparseVector([1,2,0,0,4])
# sparsevec2 = sparsevec.SparseVector([0,3,0,-1,2])
# print(sparsevec1.dotProduct(sparsevec2))

####################################################
############### Popular Questions ##################
####################################################

### Test Spiral Matrix Here
spiralM = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# spiral = spiral.SpiralMatrix()
# print(spiral.spiralOrder(spiralM))

### Test MinimumKnightMoves Here
mkmX = 2
mkmY = 1
# mkm = mkm.MinimumKnightMoves()
# print(mkm.minKnightMoves(mkmX, mkmY))

### Test SlidingWindowMaximum Here
swmNums = [1,3,-1,-3,5,3,6,7]
swmK = 3
# swm = swm.SlidingWindowMaximum()
# print(swm.optimizedMaxSlidingWindow(swmNums, swmK))

### Test AddNegabinaryNumbers Here
nbnum1 = [1,1,1,1,1]
nbnum2 = [1,0,1]
# anbn = anbn.NegaBinary()
# print(anbn.addNegabinary(nbnum1,nbnum2))

### Test AddNegabinaryNumbers Here
lightmoments = [2,1,3,4,5]
# bsIII = bsIII.BulbSwitcherIII()
# print(bsIII.optimizedNumTimesAllBlue(lightmoments))

### Test AddStringNumbers Here (Very Important to master)
stringNum1 = "12345678"
stringNum2 = "23456789"
# asn = asn.AddStringsNumbers()
# print(asn.addStrings(stringNum1, stringNum2))

### Test TopKFrequent Elements Here
# tkfe = tkfe.TopKFrequentElements()
# print(tkfe.topKFrequent([1,1,1,2,2,3], 2))

### Test GroupAnagrams Here
anagramStrings = ["eat","tea","tan","ate","nat","bat"]
# gana = gana.groupAnagrams()
# print(gana.groupAnagrams(anagramStrings))

### Test FindAndReplacePattern Here
# fandrWords = ["abc","deq","mee","aqq","dkd","ccc"]
# fandrpattern = "abb"
# fandr = fandr.FindAndReplace()
# print(fandr.findAndReplacePattern(fandrWords, fandrpattern))

### Test Robot In Circle Here
# robotcircle = robotcircle.RobotCircle()
# print(robotcircle.isRobotBounded("GLLRG"))

### Test Asteroid Collision Here
# asteroidcoll = asteroidcoll.Asteroid()
# print(asteroidcoll.asteroidCollision([-2,-2,1,-2]))

### Test Longest Happy String Here
longhapstring = longhapstring.LongestHappyString()
print(longhapstring.longestDiverseString(1,2,7))

