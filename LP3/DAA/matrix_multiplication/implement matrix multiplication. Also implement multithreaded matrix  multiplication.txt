import numpy as np          # Import numpy for array handling and matrix operations
import threading            # Import threading for multithreading capabilities
import time                 # Import time to measure execution time

# Standard matrix multiplication
def matrix_multiply(A, B):
    # Initialize result matrix with zeros
    result = np.zeros((A.shape[0], B.shape[1]))
    # Loop over each row of A
    for i in range(A.shape[0]):
        # Loop over each column of B
        for j in range(B.shape[1]):
            # Loop to compute the dot product
            for k in range(A.shape[1]):
                # Perform multiplication and summation
                result[i][j] += A[i][k] * B[k][j]
    # Return the resultant matrix
    return result

# One thread per row multiplication
def row_multiply(A, B, result, row):
    # Loop over each column of B
    for j in range(B.shape[1]):
        # Loop to compute the row's products
        for k in range(A.shape[1]):
            # Calculate the value for the specific row
            result[row][j] += A[row][k] * B[k][j]

# Function to perform matrix multiplication using threading, one thread per row
def matrix_multiply_threaded_row(A, B):
    # Initialize result matrix
    result = np.zeros((A.shape[0], B.shape[1]))
    # List to hold threads
    threads = []
    # Loop over each row of A
    for i in range(A.shape[0]):
        # Create a new thread for each row
        thread = threading.Thread(target=row_multiply, args=(A, B, result, i))
        # Add thread to list
        threads.append(thread)
        # Start the thread
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    # Return the resultant matrix
    return result

# One thread per cell multiplication
def cell_multiply(A, B, result, i, j):
    # Calculate value for cell (i,j)
    result[i][j] = sum(A[i][k] * B[k][j] for k in range(A.shape[1]))

# Function to perform matrix multiplication using threading, one thread per cell
def matrix_multiply_threaded_cell(A, B):
    # Initialize result matrix
    result = np.zeros((A.shape[0], B.shape[1]))
    # List to hold threads
    threads = []
    # Loop over each row of A
    for i in range(A.shape[0]):
        # Loop over each column of B
        for j in range(B.shape[1]):
            # Create a new thread for each cell
            thread = threading.Thread(target=cell_multiply, args=(A, B, result, i, j))
            # Add thread to list
            threads.append(thread)
            # Start the thread
            thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    # Return the resultant matrix
    return result

# Performance analysis function
def analyze_performance(A, B):
    # Record start time for standard multiplication
    start_time = time.time()
    # Perform standard multiplication
    matrix_multiply(A, B)
    # Calculate elapsed time
    standard_time = time.time() - start_time

    # Record start time for row-wise threaded multiplication
    start_time = time.time()
    # Perform row-wise threaded multiplication
    matrix_multiply_threaded_row(A, B)
    # Calculate elapsed time
    row_threaded_time = time.time() - start_time

    # Record start time for cell-wise threaded multiplication
    start_time = time.time()
    # Perform cell-wise threaded multiplication
    matrix_multiply_threaded_cell(A, B)
    # Calculate elapsed time
    cell_threaded_time = time.time() - start_time

    # Return the times for comparison
    return standard_time, row_threaded_time, cell_threaded_time

# Sample Matrices for Testing
# Create a 100x100 random matrix A
A = np.random.rand(100, 100)
# Create a 100x100 random matrix B
B = np.random.rand(100, 100)

# Run performance analysis and collect output
performance_results = analyze_performance(A, B)

# Print the performance results for each multiplication method
print("Standard Multiplication Time:", performance_results[0])
print("Threaded Row-wise Multiplication Time:", performance_results[1])
print("Threaded Cell-wise Multiplication Time:", performance_results[2])
