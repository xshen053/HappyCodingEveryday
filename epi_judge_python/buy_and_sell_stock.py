from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
    if (len(prices) == 1):
        return 0.0
    min_current = prices[0]
    max_current = 0
    for i in range(len(prices)):
        min_current = min(min_current, prices[i])
        max_current = max(max_current, prices[i] - min_current)
    return max_current

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
