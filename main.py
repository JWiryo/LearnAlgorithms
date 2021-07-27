numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

#Time Complexity = O(n^2)
#Space Complexity = O(1)
def bubbleSort(arr):

  length = len(arr)
  for i in range(length-1):
    for j in range(length-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

print(bubbleSort(numbers))
