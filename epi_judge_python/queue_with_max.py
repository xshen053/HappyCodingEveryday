from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

class QueueWithMax:
    def __init__(self) -> None:
        self.queue = collections.deque()
        self.max_queue = collections.deque()

    def enqueue(self, x: int) -> None:

        # {queue}
        # {max_queue[0] max num in queue}
        self.queue.append(x)
        # {queue = queue + x}


        # {i: number of pop times }
        # {max_queue[0, orginal_size - i) are all larger than x}
        while self.max_queue and self.max_queue[-1] < x:

            self.max_queue.pop()

        # {max_queue decreasing and all >= x}

        self.max_queue.append(x)
        # {max_queue[0] max num in queue}

    def dequeue(self) -> int:
        # {}
        if self.queue:
            # {queue is not empty}
            num = self.queue.popleft()
            # {queue = queue[1:] && num = queue[0]}
            if num == self.max_queue[0]:
                # {num == max_queue[0]}
                self.max_queue.popleft()
                # {max_queue = max_queue[1:]}

            return num
        
        raise IndexError('Emtpy queue')

    def max(self) -> int:
        if self.queue:
            return self.max_queue[0]
        
        raise IndexError('Emtpy queue')


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
