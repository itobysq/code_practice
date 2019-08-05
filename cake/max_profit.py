"""
Find the max profit given a list of stock prices
"""
def reassign_profit(buy, sell, max_profit):
    if sell - buy > max_profit:
        return sell - buy
    else:
        return max_profit

def get_max_profit(stock_prices):
    max_profit = 0
    if len(stock_prices) < 2:
        return 0

    for idx, val in enumerate(stock_prices):
        if idx == 0:
            buy = val
            continue
        if idx == 1:
            sell = val
            max_profit = reassign_profit(buy, sell, max_profit)
            continue
        if sell < buy:
            buy = sell
        if val > sell:
            sell = val
            max_profit = reassign_profit(buy, sell, max_profit)

        if val < buy:
            buy = val
            max_profit = reassign_profit(buy, sell, max_profit)

    return max_profit

if __name__ == '__main__':
    assert get_max_profit([]) == 0
    assert get_max_profit([1]) == 0
    assert get_max_profit([11, 5, 7, 9]) == 4
    assert get_max_profit([10, 7, 5, 8, 11, 9]) == 6
