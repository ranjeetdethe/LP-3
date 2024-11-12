def fibonacci_recursive(n, step_count=[0]):
    step_count[0] += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n-1, step_count) + fibonacci_recursive(n-2, step_count)

def fibonacci_iterative(n):
    step_count = 0
    a = 0
    b = 1
    for _ in range(n):
        step_count += 1
        temp = a + b
        a = b
        b = temp
    return a, step_count

n = int(input("Enter the term number: "))

recursive_steps = [0]
fib_recursive = fibonacci_recursive(n, recursive_steps)
print(f"Recursive: Fibonacci({n}) = {fib_recursive}, Steps = {recursive_steps[0]}")

fib_iterative, iterative_steps = fibonacci_iterative(n)
print(f"Iterative: Fibonacci({n}) = {fib_iterative}, Steps = {iterative_steps}")
