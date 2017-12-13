def shapeArea(n):
    """
       MISSING DESCRIPTION
    """
    assert type(n) == int and n >= 1
    if n == 1:
        return 1
    if n == 2:
        return 5
    else:
        temp = n + (n-1)
        answer = temp
        while True:
            temp -= 2
            answer += temp*2
            if temp == 1:
                break
        return answer                
