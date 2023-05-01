from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # 为什么要引入dummy_head,主要原因是第一个node可能会变化
    # 所以引入dummy_head就避免把first node当成特殊情况处理

    dummy_head = ListNode(0, L)

    l2 = dummy_head.next
    l1 = dummy_head
    # {inv: l2 = l1 + i + 1 && l1 = dummy_head}
    for _ in range(k - 1):
        l2 = l2.next

    # {l2 = l1 + k && l1 = firstnode}

    # {inv: l2 = l1 + k && l2 is not the last node}
    while l2.next:
        l1 = l1.next
        l2 = l2.next

    l1.next = l1.next.next

    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
