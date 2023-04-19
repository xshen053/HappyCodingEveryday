from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    
    # set Neg flag
    isNeg = 0
    if x < 0:
        isNeg = 1
        x = -x
    
    # build result
    s = []
    while (x != 0):
        digit = x % 10
        # s += "%s" % digit
        s += (chr(ord('0') + digit))
        x //= 10

    # if isNeg, add -
    if (isNeg):
        s += "-"
    
    # reverse s
    # s = s[::-1]
    return ''.join(reversed(s)) # ?? convert list to string??


def string_to_int(s: str) -> int:
    
    Neg = 1
    # operation
    if (s[0] == "+"):
        s = s[1:len(s)]
    elif (s[0] == "-"):
        Neg = -1
        s = s[1:len(s)]

    # handle 0 case
    if (s == "0"):
        return 0
    
    res = 0
    i = -1
    # Solution 1
    # {inv: res = s[0, i] corresponding integer}
    # for i in range(0, len(s)):
    #     # brute force way
    #     res += (ord(s[i]) - ord('0')) * pow(10, len(s[i:len(s)]) - 1)
    #     i = i + 1
    
    # Solution 2
    # a little better way: use existing value 10^i
    # div = pow(10, len(s[0:len(s)]) - 1)
    # for i in range(0, len(s)):
    #     # emit pow calculation
    #     res += (ord(s[i]) - ord('0')) * div
    #     i = i + 1
    #     div = div / 10

    # Solution3
    res = ord(s[0]) - ord('0')
    # {inv: res * 10 ^ (len(s) - i) = s[0, i) corresponding integer}
    for i in range(1, len(s)):
        # emit pow calculation
        res *= 10 
        # {res * 10 ^ (len(s) - i - 1) = s[0, i) corresponding integer}
        res += (ord(s[i]) - ord('0'))
        # {res * 10 ^ (len(s) - i - 1) = s[0, i + 1) corresponding integer}
        i = i + 1
        # {inv: res * 10 ^ (len(s) - i) = s[0, i) corresponding integer}

    # {res * 10 ^ 0 = s[0, len(s)) corresponding integer}
    return res * Neg

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
