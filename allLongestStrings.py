def allLongestStrings(inputArray):
    """
       MISSING DESCRIPTION
    """
    answer = [inputArray[0]]
    longest = len(inputArray[0])
    for entry in xrange(1,len(inputArray)):
        if len(inputArray[entry]) > longest:
            answer = [inputArray[entry]]
            longest = len(inputArray[entry])
            continue
        elif len(inputArray[entry]) == longest:
            answer.append(inputArray[entry])
    return answer
