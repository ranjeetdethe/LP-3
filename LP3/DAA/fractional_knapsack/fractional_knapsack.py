class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(values, weights, capacity):
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0.0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            capacity = 0
    return total_value

while True:
    try:
        print("Press Ctrl+C to terminate...")
        n = int(input('Enter number of items: '))
        values = [int(i) for i in input("Enter values of items: ").split()]
        weights = [int(i) for i in input("Enter weights of items: ").split()]
        capacity = int(input("Enter maximum weight: "))
        
        if len(values) != n or len(weights) != n:
            print("Error: The number of values and weights must match the number of items.")
            continue
        
        maximum_value = fractional_knapsack(values, weights, capacity)
        print('The maximum value of items that can be carried:', maximum_value)
    except KeyboardInterrupt:
        print("\nTerminating the program.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
