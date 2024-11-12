import numpy as np  # Import numpy for array handling
import threading  # Import threading for multithreading capabilities
import time  # Import time to measure execution time


# Standard Merge Sort
def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    # Find the middle index
    mid = len(arr) // 2
    # Recursively sort the left half
    left_half = merge_sort(arr[:mid])
    # Recursively sort the right half
    right_half = merge_sort(arr[mid:])
    # Merge the sorted halves
    return merge(left_half, right_half)


# Merge two sorted arrays
def merge(left, right):
    merged = []  # List to hold the merged result
    i = j = 0  # Pointers for left and right arrays
    # Loop until one of the arrays is exhausted
    while i < len(left) and j < len(right):
        # Append the smaller element to merged
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append remaining elements (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged  # Return the merged array


# Multithreaded Merge Sort
def threaded_merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    # Create two threads to sort each half
    left_thread = threading.Thread(target=lambda: merge_sort(arr[:mid]))
    right_thread = threading.Thread(target=lambda: merge_sort(arr[mid:]))

    # Start the threads
    left_thread.start()
    right_thread.start()

    # Wait for both threads to finish
    left_thread.join()
    right_thread.join()

    # Merge the sorted halves
    return merge(arr[:mid], arr[mid:])


# Performance analysis function
def analyze_performance(sort_function, arr):
    start_time = time.time()  # Record the start time
    sort_function(arr)  # Perform sorting
    return time.time() - start_time  # Return the elapsed time


# Test cases for performance analysis
def test_performance():
    # Best Case: Already sorted array
    best_case = np.arange(10000)  # Sorted array
    # Worst Case: Reverse sorted array
    worst_case = np.arange(10000, 0, -1)  # Reverse sorted array

    # Analyze performance for best case
    best_case_standard_time = analyze_performance(merge_sort, best_case.copy())
    best_case_threaded_time = analyze_performance(threaded_merge_sort, best_case.copy())

    # Analyze performance for worst case
    worst_case_standard_time = analyze_performance(merge_sort, worst_case.copy())
    worst_case_threaded_time = analyze_performance(threaded_merge_sort, worst_case.copy())

    # Print the results
    print("Best Case - Standard Merge Sort Time:", best_case_standard_time)
    print("Best Case - Threaded Merge Sort Time:", best_case_threaded_time)
    print("Worst Case - Standard Merge Sort Time:", worst_case_standard_time)
    print("Worst Case - Threaded Merge Sort Time:", worst_case_threaded_time)


# Run the performance test
test_performance()
