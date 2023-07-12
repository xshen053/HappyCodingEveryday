from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections
from collections import namedtuple
from typing import List

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ['element', 'max_value'])
    def __init__(self):
        # More readable
        self._element_with_cached_max_: List[Stack.ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._element_with_cached_max_) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        return self._element_with_cached_max_[-1].max_value

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        return self._element_with_cached_max_.pop().element
    
    def push(self, x: int) -> None:
        # Case1 if empty: push
        if self.empty():
            self._element_with_cached_max_.append(self.ElementWithCachedMax(x, x))
        # Case2 compare max and push
        else:
            self._element_with_cached_max_.append(self.ElementWithCachedMax(x, max(x, self.max())))
 

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
