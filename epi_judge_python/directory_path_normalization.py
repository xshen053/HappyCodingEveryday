from test_framework import generic_test



def shortest_equivalent_path(path: str) -> str:
    # passible path
    # - /usr/bin/gcc | //usr/bin/gcc ... 
    # - ./epi | epi
    # - ../epi
    
    # STEP 1: edge case
    if len(path) == 0:
        return path
    
    stack = []
    if (path[0] == '/'):
        stack.append('/')
    
    # don't forget '' : empty gap
    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            # impossible to out of boundary
            # because we don't meet '/'
            if not stack or stack[-1] == '..':
                stack.append(token)
            else:
                if stack[-1] == '/':
                    raise ValueError('Path Error')
                stack.pop()
        else:
            stack.append(token)

    result = '/'.join(stack)

    return result[result.startswith('//'):]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))

