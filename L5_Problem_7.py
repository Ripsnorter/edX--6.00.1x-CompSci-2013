'''
L5 Problem 7
------------

For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string), by counting up the number of characters in the string.

Hint: String slicing may be useful in this problem...
'''

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Base case: When aStr is the empty string,
    #  its length is zero.
    if aStr == '':
        return 0

    # Recursive case: If the string is not zero-length, then remove the first
    #  character and the length is 1 + the length of the rest of the string
    return 1 + lenRecur(aStr[1:])
