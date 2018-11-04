def ways(coins, value):
    """
    Getting the number of ways to generate the target value with a given list of bills.
    """
    if value == 0:
        return 1
    elif value < 0:
        return 0
    elif coins == []:
        return 0
    else:
        return sum([ways(coins, value-coin) for coin in coins])

print(ways([25, 10, 5], 25))

