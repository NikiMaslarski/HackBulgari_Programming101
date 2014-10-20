def reduce_file_path(path):
    list_as_stack = []
    path = path.split('/')
    for folder in path:
        list_as_stack.append(folder)
        if folder == '..':
            list_as_stack.pop()
            list_as_stack.pop()
        elif folder == '.':
            list_as_stack.pop()

    result = '/'.join(list_as_stack)
    if len(result) <= 1:
        return result
    elif result[-1] == '/':
        return result[:-1]
    else:
        return result

