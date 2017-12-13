def makeArrayConsecutive2(statues):
    """
       MISSING DESCRIPTION
    """
    count = 0
    sort = sorted(statues)
    end = sort[len(sort)-1]
    begining = sort[0]
    temp = {}
    for i in sort:
        temp[i] = None
    for j in range(begining, end):
        if temp.has_key(j):
            pass
        else:
            temp[j] = None
            count += 1
    return count
