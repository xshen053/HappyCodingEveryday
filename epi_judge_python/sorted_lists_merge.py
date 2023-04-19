from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()
    # {L1: 2-5-7}
    # {L2: 3-11-16}
    # {inv: tail is the tail of L1 + L2 and all elements before tail are sorted}
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
            # {tail: head-2}
            # {L1: 5-7}
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
        # {inv: tail is the tail of L1 + L2 and all elements before tail are sorted}
    tail = L1 or L2
    return dummy_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
