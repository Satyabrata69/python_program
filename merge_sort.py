def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Traverse both lists and insert the smaller element from left or right into the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Collect the remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
