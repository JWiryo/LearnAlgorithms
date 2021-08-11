numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -1, -3]

### Sorting Implementation Here

## Bubble Sort
#Time Complexity = O(n^2)
#Space Complexity = O(1)
def bubbleSort(arr):

  length = len(arr)
  for i in range(length-1):
    for j in range(length-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

## Selection Sort
#Time Complexity = O(n^2)
#Space Complexity = O(1)

### Personal Implementation
def selectionSort(arr):

  length = len(arr)
  for i in range(length-1):
    minNum = arr[i]

    for j in range(i+1, length):
      if arr[j] <= minNum:
        minNum = arr[j]
        arr[i], arr[j] = arr[j], arr[i]
  
  return arr

### Alternate implementation based on Udemy course by Andrei Neagoie & Yihua Zhang
def selectionSortAlt(arr):

  length = len(arr)
  for i in range(length-1):
    minIdx = i

    for j in range(i+1, length):
      if arr[j] <= arr[minIdx]:
        minIdx = j

    arr[i], arr[minIdx] = arr[minIdx], arr[i]    
    
  return arr

## Insertion Sort
#Time Complexity = O(n^2) [Best case is O(n) if list already almost sorted]
#Space Complexity = O(1)

### Personal Implementation
def insertionSort(arr):

  length = len(arr)
  for i in range(1, length):
    
    curValue = arr[i]
    j = i - 1
    while j >= 0 and arr[j] >= curValue:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = curValue
  
  return arr

## Merge Sort
#Time Complexity = O(nlogn)
#Space Complexity = O(n)

### Implementation based on Udemy course by Andrei Neagoie & Yihua Zhang
def mergeSort(arr):

  # Base Case
  length = len(arr)
  if length == 1:
    return arr
  
  # Divide Array into 2-halves
  half = length // 2
  left = arr[:half]
  right = arr[half:]
  
  # Recursive Case
  return merge(mergeSort(left), mergeSort(right))

def merge(left, right):

  temp = []
  i = 0
  j = 0

  # Comparison Case
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      temp.append(left[i])
      i += 1
    else:
      temp.append(right[j])
      j += 1

  # Remaining Left case
  while i < len(left):
    temp.append(left[i])
    i += 1
  
  # Remaining Right case
  while j < len(right):
    temp.append(right[j])
    j += 1

  return temp

## Merge Sort
#Time Complexity = O(n^2) but O(nlogn) on average
#Space Complexity = O(n)

### Implementation based on Udemy course by Andrei Neagoie & Yihua Zhang
def quickSort(arr, left, right):

  # Base Case
  length = len(arr)
  if length < 2:
    return arr

  if left < right:
    # Get partition
    partitionIdx = partition(arr, left, right)

    # Perform Quick Sort
    quickSort(arr, left, partitionIdx - 1)
    quickSort(arr, partitionIdx + 1, right)
  
  return arr

def partition(arr, left = 0, right = None):

  partitionIdx = left
  pivotIdx = right

  for j in range(left, right):
    if arr[j] <= arr[pivotIdx]:
      arr[j], arr[partitionIdx] = arr[partitionIdx], arr[j]
      partitionIdx += 1
  arr[partitionIdx], arr[pivotIdx] = arr[pivotIdx], arr[partitionIdx]

  return partitionIdx
      

### Test Codes Here
# print(bubbleSort(numbers))
# print(selectionSort(numbers))
# print(insertionSort(numbers))
# print(mergeSort(numbers))
# print(quickSort(numbers, 0, len(numbers)-1))

### Binary Search Implementation Here

def binarySearch(arr, target):

  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    foundVal = arr[mid]

    if foundVal == target:
      return mid
    elif foundVal < target:
      left = mid + 1
    else:
      right = mid - 1
    
  return -1

### Test Codes Here
print(binarySearch(mergeSort(numbers), 4))
