def matrix_bombing_plan(m):
    result_dict = {}

    for i in range(len(m)):
        for ii in range(len(m[i])):
            result_dict[(i, ii)] = m[i][ii]
            start1 = -1
            start2 = -1
            end1 = 2
            end2 = 2

            if i == 0:
                start1 = 0
            elif i == len(m) - 1:
                end1 = 1
            if ii == 0:
                start2 = 0
            elif ii == len(m[i]) - 1:
                end2 == 1

            for j in range(start1, end1):
                for jj in range(start2, end2):
                    if m[i][ii] < m[i - j][ii - jj]:
                        result_dict[(i, ii)] += +m[i - j][ii - jj] - m[i][ii]
    return result_dict
