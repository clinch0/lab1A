def two_pointers(arr1, arr2, i=0, j=0):
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            return True
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return False

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def binary_search_method(arr1, arr2):
    for item in arr1:
        if binary_search(arr2, item, 0, len(arr2) - 1) is True:
            return True
    
    return False

def exponential_search(arr, target, start):
    if start >= len(arr):
        return False, start
    
    if arr[0] == target:
        return True, start
    
    i = 1
    while start + i < len(arr) and arr[start + i] <= target:
        i *= 2
    
    left = start + i // 2
    start = left
    right = min(start + i, len(arr) - 1)

    return binary_search(arr, target, left, right), start

def exponential_method(arr1, arr2):
    start = 0

    for item in arr1:
        is_common, start = exponential_search(arr2, item, start)
        if is_common is True:
            return True
    
    return False

def binary_search_with_division(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False, left

def binary_division_method(arr1, arr2, l1, r1, l2, r2):
    if l1 > r1 or l2 > r2:
        return False
    
    mid1 = (l1 + r1) // 2

    elem = arr1[mid1]
    
    is_common, septum = binary_search_with_division(arr2, elem, l2, r2)
    
    if is_common:
        return True
    
    is_common_on_left = binary_division_method(arr1, arr2, l1, mid1 - 1, l2, septum - 1)

    if is_common_on_left:
        return True

    is_common_on_right = binary_division_method(arr1, arr2, mid1 + 1, r1, septum, r2)
    
    return is_common_on_right
