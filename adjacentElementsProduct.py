def adjacentElementsProduct(inputArray):
    """
       assumes inputArray is of type list
       first, creates and empty buffer to store the highest product produced
       itterates over the entire list, multiplying the adjacent elements together
       if the product produced is greater than the number stored in the buffer, replace buffer with current product
       return buffer
    """
    assert type(inputArray) == list
    answer = inputArray[0]*inputArray[1]
    if len(inputArray) > 2:
        for i in xrange(1,len(inputArray)-1):
            temp = inputArray[i]*inputArray[i+1]
            if temp > answer:
                answer = temp
    return answer
