import Sorting
import PriorityQueue as pq
import MatrixTraversal as mt
import GraphTraversal as gt
import TopologicalSort as ts

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

### Test Sorting Codes Here
# print(Sorting.bubbleSort(numbers))
# print(Sorting.selectionSort(numbers))
# print(Sorting.insertionSort(numbers))
# print(Sorting.mergeSort(numbers))
# print(Sorting.quickSort(numbers, 0, len(numbers)-1))

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
ts = ts.TopologicalSort()
print(ts.checkCycleTopologicalSort(adjacencyList))