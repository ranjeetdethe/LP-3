package Java;

public class Knapsack {

    // Method to solve the 0-1 Knapsack problem
    public static int knapsack(int[] weights, int[] values, int capacity, int n) {
        // Create a DP table to store maximum values for each weight capacity
        int[][] dp = new int[n + 1][capacity + 1];

        // Build the DP table in a bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0) {
                    dp[i][w] = 0; // Base case: No items or zero capacity
                } else if (weights[i - 1] <= w) {
                    // Item can be included: Choose max of including or excluding the item
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                } else {
                    // Item cannot be included: Exclude it
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][capacity]; // Max value for given capacity and n items
    }

    public static void main(String[] args) {
        // Example weights and values of items
        int[] weights = {10, 20, 30};
        int[] values = {60, 100, 120};
        int capacity = 50;
        int n = weights.length;

        int maxValue = knapsack(weights, values, capacity, n);
        System.out.println("Maximum value in Knapsack = " + maxValue);
    }
    
}
