def binomial_coefficient(n, k):
    # Create a 2D array to store the binomial coefficients
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Calculate binomial coefficients
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1  # Base case: C(n, 0) = C(n, n) = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]  # Recursive relation

    return C[n][k]

def main():
    n = int(input("Enter n (total elements): "))
    k = int(input("Enter k (elements to choose): "))
    
    if k > n or n < 0 or k < 0:
        print("Invalid input: Ensure that 0 <= k <= n.")
        return
    
    result = binomial_coefficient(n, k)
    
    # Output the result
    print(f"The binomial coefficient C({n}, {k}) is: {result}")


main()

# Sample Output:
# Enter n (total elements): 5
# Enter k (elements to choose): 2
# The binomial coefficient C(5, 2) is: 10
