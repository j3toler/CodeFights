def matrixElementsSum(matrix):
    """
       MISSING DESCRIPTION
    """
    pass
    rows = len(matrix)
    columns = len(matrix[0])
    haunted = [0 for i in range(columns)]
    total = 0
    for row in xrange(rows):
        for room in xrange(columns):
            if haunted[room] != 0:
                continue
            if matrix[row][room] == 0:
                haunted[room] = 1
                continue
            total += matrix[row][room]
    return total
