def checkPalindrome(inputString):
    """
       assumes inputString is of type str
       returns True if inputString is the same forwards as it is backwards
       returns False otherwise
    """
    inputString = inputString.lower()
    if inputString[::-1] == inputString:
        return True
    return False
