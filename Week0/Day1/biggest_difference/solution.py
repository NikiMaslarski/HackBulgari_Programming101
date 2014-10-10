def biggest_difference(arr):
    new_arr = list(arr)
    new_arr.sort()
    return new_arr[0] - new_arr[-1]

