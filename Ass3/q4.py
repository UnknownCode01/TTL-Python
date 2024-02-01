def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

# Read N from the user
try:
    n = int(input("Enter the value of N: "))
    if n <= 0:
        raise ValueError("N should be a positive integer.")
    
    result = generate_fibonacci(n)
    print(f"Fibonacci sequence up to {n}: {result}")

except ValueError as ve:
    print(f"Error: {ve}")
