from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    if L == None:
        return L
    
    l = length(L)
    k = k % l

    if k == 0:
        return L
    
    dummy_node = ListNode(0, L)
    
    pre = dummy_node
    
    # move l - k steps
    for _ in range(l - k):
        pre = pre.next

    node_shift = pre.next

    # move k steps
    tail = pre
    for _ in range(k):
        tail = tail.next

    pre.next = None
    tail.next = dummy_node.next
    dummy_node.next = node_shift
    
    return dummy_node.next
    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
