package Java;

public class EightQueens {

    private static final int N = 8; // Size of the board

    // Function to print the board
    public static void printBoard(int[][] board) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1) {
                    System.out.print("Q "); // Print Q for queens
                } else {
                    System.out.print(". "); // Print . for empty spaces
                }
            }
            System.out.println();
        }
        System.out.println();
    }

    // Function to check if a queen can be placed at board[row][col]
    private static boolean isSafe(int[][] board, int row, int col) {
        // Check column for any queen
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1) {
                return false;
            }
        }

        // Check upper-left diagonal for any queen
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        // Check upper-right diagonal for any queen
        for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true; // Safe to place queen
    }

    // Recursive function to place queens on the board
    private static boolean solveNQueens(int[][] board, int row) {
        if (row >= N) { // All queens placed
            return true;
        }

        // Loop through columns to place queen in each row
        for (int col = 0; col < N; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1; // Place queen

                // Recursive call to place the next queen
                if (solveNQueens(board, row + 1)) {
                    return true;
                }

                board[row][col] = 0; // Backtrack if placing here doesn't lead to a solution
            }
        }

        return false; // No valid placement found for this row
    }

    public static void main(String[] args) {
        int[][] board = new int[N][N];

        // Placing the first queen in a predefined position (row 0, column 0)
        board[0][0] = 1;

        // Start placing queens from row 1
        if (solveNQueens(board, 1)) {
            System.out.println("Solution for the 8-Queens problem:");
            printBoard(board);
        } else {
            System.out.println("No solution found.");
        }
    }
    
}