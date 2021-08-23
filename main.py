import Sorting
import PriorityQueue as pq

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -1, -3]

### Test Sorting Codes Here
# print(Sorting.bubbleSort(numbers))
# print(Sorting.selectionSort(numbers))
# print(Sorting.insertionSort(numbers))
# print(Sorting.mergeSort(numbers))
# print(Sorting.quickSort(numbers, 0, len(numbers)-1))

### Test Binary Search Here
# print(Sorting.binarySearch(Sorting.mergeSort(numbers), 4))

### Test Heap & Priority Queue Here
pq = pq.PriorityQueue()

#### Push Values to heap
pq.push(5)
pq.push(10)
pq.push(8)
print(pq.printQueue())

pq.pop()
print(pq.printQueue())