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

## Quick Sort
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

## Dijkstra 3-Way Partition Sort
#Time Complexity = O(n)
#Space Complexity = O(1)

### Implementation based on Udemy course by Andrei Neagoie & Yihua Zhang
def threeWaySort(nums, midValue):

  # Edge case handling
  if len(nums) <= 1:
      return nums
  
  # Select mid value, in this problem, it is 1
  mid = 1
  
  # Initialize 3 pointers
  # Pointer i --> elements 0 to i = values LESS THAN mid
  # Pointer j --> elements i to j = values EQUAL TO mid
  # Pointer k --> elements j to K = values GREATER THAN mid
  i, j, k = 0, 0, len(nums)-1
  
  # Keep going until pointer j passes k
  while j <= k:

    if nums[j] < mid:
      # Swap elements at i and j
      nums[i], nums[j] = nums[j], nums[i]
      
      # Increase Pointer i and j
      i += 1
      j += 1
        
    elif nums[j] > mid:
      # Swap elements at j and k
      nums[j], nums[k] = nums[k], nums[j]
      
      # Reduce pointer k
      k -= 1
    else:
        
      # Move pointer j
      j += 1
  
  return nums


### Binary Search Implementations Here
# Binary Search for Normal Sorted Array
# Time Complexity: O(Log N)
# Space Complexity: O(1)
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

# Binary Search for Rotated Array Solution; Idea is to keep searching wherever side we know that is sorted
# Time Complexity: O(Log N)
# Space Complexity: O(1)

def binarySearchRotated (nums: [int], target: int) -> int:
  
  # Initiate left and right pointer
  left = 0
  right = len(nums) - 1
  
  # In case we found on first try, just return the values
  if nums[left] == target:
    return left
  elif nums[right] == target:
    return right
  
  # Perform binary search
  while left <= right:
    
    # Calculate mid      
    mid = (left + right) // 2

    # Incase we found target at mid
    if nums[mid] == target:
      return mid

    # If first element is less than mid element, we know that left side is sorted
    if nums[left] <= nums[mid]:
      
      # If target value is less than or equal to left element and less than mid element, we go left
      if target >= nums[left] and target < nums[mid]:
        
        # Update right pointer
        right = mid - 1
      
      # Otherwise,
      else:
        
        # Update left pointer
        left = mid + 1

    # Else, we know it is on the right side is sorted
    else:
      
      # If target value is greater than or equal to mid and target value less than right, we go right
      if target <= nums[right] and target > nums[mid]:
        
        # Update left pointer
        left = mid + 1
      
      # Otherwise,
      else:
        
        # Update right pointer
        right = mid - 1
    
  return -1


