def nan_expand(times):
    string = ''
    if times:
        for iteration in range(times):
            string = string + "Not a "
        string = string + "NaN"
    return string

