from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # {precondition: i = 0 is reachable}
    assert(len(A) != 0)
    # {so max_distance = 0 is fine}
    max_distance = 0
    # {inv: max_distance = max from[0, i - 1]}
    for i in range(len(A)):
        if (i <= max_distance):
            # {max from [0,  i - 1] && i <= max_distance}
            max_distance = max(i + A[i], max_distance)
            # {max_distance = max from[0, i]}
        # {inv: max_distance = max from[0, i - 1]}
    return max_distance >= len(A) - 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
