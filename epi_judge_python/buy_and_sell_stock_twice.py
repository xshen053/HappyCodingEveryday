from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    min_current = prices[0]
    max_current = 0
    F = [0] * len(prices)
    B = [0] * len(prices)
    for i in range(len(prices)):
        min_current = min(min_current, prices[i])
        max_current = max(max_current, prices[i] - min_current)
        F[i] = max_current
    min_current = prices[len(prices) - 1]
    max_current = float('-inf')
    max_price_so_far = float('-inf')
    for i in range(len(prices) - 1, 0, -1):
        max_price_so_far = max(max_price_so_far, prices[i])
        max_current = max(max_current, max_price_so_far - prices[i])
        B[i] = max_current
    for i in range(len(prices)):
        if (i == 0):
            max_current = B[i]
        else:
            max_current = max(F[i - 1] + B[i], max_current)
    return max_current


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
