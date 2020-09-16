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
def agnostic_binary_search(arr, target):
    # Your code here
    # So the arrays are sorted, but we don't know if they're in ascending or descending order

    pos = -1
    if len(arr) > 0:
        start = 0
        end = len(arr) - 1
        pos = (start + end) // 2

        print(f"Target: {target}, Array: {arr}")
        print(f"Start: {arr[start]}, Pos: {arr[pos]}, End: {arr[end]}")

        if len(arr) > 1:
            if arr[start] < arr[end]:
                print("In Ascending")
                # Ascending order
                if arr[pos] > target:
                    return agnostic_binary_search(arr[start:pos], target)
                if arr[pos] < target:
                    return agnostic_binary_search(arr[(pos + 1):(end + 1)], target)
            else:
                # Descending order
                print("In Ascending")
                if arr[pos] > target:
                    return agnostic_binary_search(arr[(pos + 1):(end + 1)], target)
                if arr[pos] < target:
                    return agnostic_binary_search(arr[start:pos], target)

    # Oh! We're out of the if-statement. Test the pos we're about to return.
    print(f"Pos to return: {pos}")
    return pos

    # Technically, this code works to find the target for all cases, ...
    # However, the value of the target's pos for original array keeps changing with each augmented array in the return
    # This can be corrected with start and end attributes being added as passed-in parameters in the function, but I assume I'm
    # supposed to accomplish this goal without adding parameters
    # def agnostic_binary_search(arr, target, start=0, end=len(arr) - 1)
    # The returns: return agnostic_binary_search(arr, target, new_start, new_end)

