def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    n = int(input("Enter the number of items: "))
    values = [int(i) for i in input("Enter values of items: ").split()]
    weights = [int(i) for i in input("Enter weights of items: ").split()]
    capacity = int(input("Enter the maximum capacity of the knapsack: "))

    if len(values) != n or len(weights) != n:
        print("Error: The number of values and weights must match the number of items.")
        return

    max_value = knapsack(values, weights, capacity)
    print("The maximum value that can be obtained in the knapsack is:", max_value)

main()




