from test_framework import generic_test


def evaluate(expression: str) -> int:
    # STEP 0 split string
    stack = expression.split(",")

    # STEP 1 Edge cases
    if len(stack) == 1:
        return int(stack[0])
    
    # {stack: [3, 4, +, 2, *, 1, +]}

    # STEP 2 cacluate using a stack, make sure there are
    stack.reverse()
    # {[+, 1, *, 2, +, 4, 3]}
    result = 0
    # print(stack)

    # {inv: [0, len(stack)) haven't processed}

    # 
    cal_stack = []
    while len(stack) != 0:
        # wrong place to define cal_stack
        # cal_stack = []
        while 1:
            if (stack[-1] == "+" or stack[-1] == "-" or stack[-1] == "*" or stack[-1] == "/"):
                break
            cal_stack.append(stack.pop())
            
        # {cal_stack has numbers && stack[-1] is operator}
        op = stack.pop()
        j = cal_stack.pop()
        i = cal_stack.pop()
        i, j = int(i), int(j)
        temp = 0
        if (op == "+"):
            temp = i + j
        elif (op == "-"):
            temp = i - j
        elif (op == "*"):
            temp = i * j
        elif (op == "/"):
            temp = i // j
        cal_stack.append(temp)

    return cal_stack.pop()

    

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
