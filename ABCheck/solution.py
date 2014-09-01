def ABChecker(string):
    for i in range(len(string) - 4):
        if string[i] == 'a' and string[i+4] == 'b':
            return True
        elif string[i] == 'b' and string[i+4] == 'a':
            return True
    return False
