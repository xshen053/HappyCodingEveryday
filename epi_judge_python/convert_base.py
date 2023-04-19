from test_framework import generic_test

def str_num(num_as_string: str) -> int:
    if ord(num_as_string[0]) - ord('0') > 9:
        return ord(num_as_string[0]) - ord('A') + 10
    else:
        return ord(num_as_string[0]) - ord('0')

def num_str(num: int) -> str:
    if (num > 9):
        return chr(ord('A') + num - 10)
    else:
        return chr(ord('0') + num)

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return '0'
    
    Neg = 0
    if num_as_string[0] == '-':
        Neg = 1
        num_as_string = num_as_string[1:len(num_as_string)]

    # STEP1: convert str to num 10-base
    num_base10 = 0
    num_base10 = str_num(num_as_string[0])
    for i in range(1, len(num_as_string)):
        num_base10 *= b1
        num_base10 += str_num(num_as_string[i])
        i = i + 1

    # STEP2: convert it to b2-base
    temp = num_base10
    res = []
    # {inv: res + temp * b2 ^ len(res) = num_base10}
    while temp != 0:
        mod = temp % b2
        temp = temp // b2
        res.append(num_str(mod))

    # STEP3: Neg Check
    if (Neg):
        res.append('-')

    return ''.join(reversed(res))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
