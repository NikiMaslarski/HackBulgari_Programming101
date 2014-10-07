def Dash_insert(num):
    result = []
    while num:
        result.append(str(num % 10))
        if (num % 10)%2 == 1 and (num / 10 % 10) % 2 == 1:
            result.append('-')
        num = num/10
    result.reverse()
    return ''.join(result)
