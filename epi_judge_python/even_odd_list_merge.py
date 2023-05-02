from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # Edge case
    if L is None:
        return L
    
    


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # Edge case
    if L is None:
        return L
    
    odd = L
    even = odd.next
    head_even = even

    # {inv: [head, odd] [head even] are in separate list}
    while odd.next and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    
    # {inv && odd 或者 even的下一个是None，说明到头了}

    # {odd and even are okay}
    odd.next = head_even
    # {odd->even}

    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
