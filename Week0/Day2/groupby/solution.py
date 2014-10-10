def groupby(func, seq):
    result = {}
    for item in seq:
        result[func(item)] = []
    for item in seq:
        result[func(item)].append(item)
    return result

