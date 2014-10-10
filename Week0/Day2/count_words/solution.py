def count_words(arr):
    result = {}
    for word in arr:
        result[word] = 0
    for word in arr:
        result[word] += 1
    return result

