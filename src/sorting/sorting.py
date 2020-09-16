# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    posA = 0
    posB = 0

    for i in range(elements):
        # For some reason, in all 4 conditions below, merged_arr.append(arrA[posA]) or the B version didn't work
        # Never mind, I figured out why that was. In the initialization above, we made merged_arr = [0, 0, 0, 0, 0, etc]
        # Appending would leave the 0s intact, and have the sorted values stuck at the end of a longer array, now
        if posA >= len(arrA):
            # We already ran through and sorted arrA. Only elements in arrB remaining
            merged_arr[i] = arrB[posB]
            posB += 1
        elif posB >= len(arrB):
            # We already ran through and sorted arrB. Only elements in arrA remaining
            merged_arr[i] = arrA[posA]
            posA += 1
        elif arrA[posA] < arrB[posB]:
            merged_arr[i] = arrA[posA]
            posA += 1
        else:
            merged_arr[i] = arrB[posB]
            posB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        arr = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     if len(arr) > 1:
#         arr = merge_in_place(merge_sort_in_place(arr, arr[:len(arr) // 2], arr[len(arr) // 2:]), start, (len(arr) // 2), end)
#     # I constructed arr above along the same vein as my construction on line 36, but using the parameters specified for this stretch
#     # But at this point, I'm at a loss how start and end would or would not change in this recursion, and therefore
#     # how I might create the merge_in_place function above.

#     return arr

