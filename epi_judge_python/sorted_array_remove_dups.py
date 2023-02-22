import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0

    write_index = 1
    # {inv: [0, write_index) is not duplicate from array[0, i)}
    for i in range(1, len(A)):
        # {inv: [0, write_index) is not duplicate from array[0, i)}
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            # {[0, write_index + 1) is not duplicate from array[0, i + 1)}    
            write_index += 1
            # {[0, write_index) is not duplicate from array[0, i + 1)}

        # {inv: [0, write_index) is not duplicate from array[0, i)}        
    # {inv && i = len(A) ==> [0, write_index) is not duplicate from A}    
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
