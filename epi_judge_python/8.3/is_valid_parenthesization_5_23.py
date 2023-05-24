from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    if len(s) == 0:
        return True
    
    stack = []
    lookup = {'(':')', '{':'}','[':']'}
    for c in s:
        if c in lookup:
            stack.append(c)
        elif not stack or lookup[stack.pop()] != c:
            return False
        
    return not stack

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
