from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        # STEP 1: Think about what variable do we need
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x: int) -> None:
        # STEP 2: if we need resize, resize first
        # Hint:
        # * we cannot just resize array
        # * we need reset element
        if len(self._entries) == self._num_queue_elements:
            # reset
            self._entries = (self._entries[self._head:] + self._entries[:self._head])
            # reset head and tail
            self._head, self._tail = 0, self._num_queue_elements
            # resize
            self._entries += [None] * (
                len(self._entries) * (Queue.SCALE_FACTOR - 1))
            
        # STEP 3: normal case
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self) -> int:
        # STEP 4: 
        # Hint: 
        # * what if the array is empty 
        # * We want to return that element
        # * remove is from head

        if not self._num_queue_elements:
            raise IndexError('Empty Queue')
        
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        
        return ret

    def size(self) -> int:
        return self._num_queue_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
