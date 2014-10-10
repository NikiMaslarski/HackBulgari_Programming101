COINS = [100, 50, 20, 10, 5, 2, 1]


def calculate_coins(sum_):
    sum_ *= 100
    result = {}
    for coin in COINS:
        result[coin] = 0
        while sum_ - coin >= 0:
            sum_ -= coin
            result[coin] += 1
    return result

