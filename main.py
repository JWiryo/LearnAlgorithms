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

### Test Codes Here
# print(bubbleSort(numbers))
print(selectionSort(numbers))



