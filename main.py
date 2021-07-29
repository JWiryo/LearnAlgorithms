numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, -1, -3]

### Implementation Here

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

### Test Codes Here
# print(bubbleSort(numbers))
# print(selectionSort(numbers))
# print(insertionSort(numbers))
print(mergeSort(numbers))



