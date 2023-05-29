from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    if len(s) == 0:
        return True    
    stack = []
    lookup = {'(':')', '{':'}', '[':']'}

    for c in s:
        if c in lookup:
            stack.append(c)
        elif not stack or lookup[stack.pop()] != c:
            # Case1:
            # not stack 因为elif的时候，c必定是), }, ]其中的一个，要匹配成功，必须stack不为空，否则肯定有问题
            # 如果先输入} ] )肯定就错了
            # Case2:
            # 输入的}，stack里是(或[，那肯定也错了
            return False

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
