from list_node import ListNode
from test_framework import generic_test
from reverse_list import reverse_list

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    
    # STEP1 finds second half of L
    slow = fast = L

    # {pre: length of list = l}

    # [n1, n2] denotes distance between node n1 and n2, eg. [0, 0] = 0, [0, 1] = 1
    # {inv: [head, fast] = 2 * [head, slow]}
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # {inv && [head, fast] = l OR l + 1} ==> [0, slow] = l / 2 OR (l + 1) / 2}
    
    '''
    经过观察, 当[head, fast] = l_even + 1 时, # node 为奇数, [0, slow] = (l_even + 1) / 2
    # 当[head, fast] = l_even 时， # node 为偶数，[0, slow] = (l_even) / 2
    # 根据观察，(l_even) / 2 == (l_even + 1) / 2, eg 4 / 2 = 5 / 2
    # 所以不管 #链表 是odd还是even, slow永远和第一个node的距离是 length / 2, 即 第(length / 2) + 1 个node
    '''
    # STEP2 reverse second half of L
    # get head of first_half and second_half lists

    first_half_iter, second_half_iter = L, reverse_list(slow)

    # {inv: linkedlist hasn't ended yet}
    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next

    # finish comparison, return true
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
