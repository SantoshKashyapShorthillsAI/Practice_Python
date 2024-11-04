# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array
def sort012(arr, n):
    lo = 0
    hi = n - 1
    mid = 0
    # Iterate till all the elements are sorted
    while mid <= hi:
      # If the element is 0
      if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo = lo + 1
        mid = mid + 1
        # If the element is 1
      elif arr[mid] == 1:
        mid = mid + 1
        # If the element is 2
      else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi - 1
    return arr

# Function to print array
def printArray(arr):
    for k in arr:
        print(k, end=' ')


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
arr = sort012(arr, n)
printArray(arr)