# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    pos = -1 # default value for return. Can be changed if length > 0
    if len(arr) > 0:
        # The arr we're passed in are already sorted from lowest to highest
        # Check values using the binary method -- going in halves
        pos = (start + end) // 2

        if arr[pos] > target:
            # Check to the left of pos
            return binary_search(arr, target, start, (pos - 1))

        if arr[pos] < target:
            # Check to the right of pos
            return binary_search(arr, target, (pos + 1), end)

    return pos


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

