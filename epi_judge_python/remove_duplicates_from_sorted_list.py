from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# {[head, it)}

def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = L

    # {inv: [head, it] has no duplicate}

    while it:

        next_distinct = it.next

        # {inv: next_distinct.data == it.data}
        while next_distinct and it.data == next_distinct.data:
            next_distinct = next_distinct.next

        # 如果是None，那么it已经是尾, it->None
        # 如果不是None，it->next_distinct
        # 没有区别
        
        # {next_distinct is next node no duplicate}
        
        it.next = next_distinct
        # {[head, it + 1] has no duplicate}

        it = it.next    
        # {[head, it] has no duplicate}

    # {inv && it = None}
    return L

# # {[head, it]}
# def remove_duplicates(L: ListNode) -> Optional[ListNode]:
#     # handle L = [] case
#     if not L:
#         return L
    
#     dummy_head = ListNode(0, L)

#     cur_node = dummy_head.next

#     # {inv: [dummy_head.next, cur_node] has no duplicate}
#     while cur_node.next:
#         next_node = cur_node.next

#         # {inv: cur_node.next = next_node}
#         while next_node and cur_node.data == next_node.data:
#             next_node = next_node.next
#             cur_node.next = next_node

#         # {[dummy_head.next, cur_node] has no duplicate}
#         if not next_node:
#             break
        
#         # {inv && next_node.data != cur_node.data}
#         # ==> [dummy_head.next, next_node] has no duplicate

#         cur_node = next_node
#         # {inv: [dummy_head.next, cur_node] has no duplicate}

#     # {inv && cur_node is the last node ==> L has no duplicates}
#     return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
