
def count_ways_to_make_200():
    ways = [0] * 201
    ways[0] = 1  # There's one way to make 0 (using no coins)

    denominations = [1, 2, 5, 10, 20, 50, 100]

    for coin in denominations:
        for amount in range(coin, 201):
            ways[amount] += ways[amount - coin]

    return ways[200]

result = count_ways_to_make_200()
print("Number of ways to make 200:", result)