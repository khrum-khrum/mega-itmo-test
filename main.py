def fibonacci(n):
    """Calculate the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    try:
        user_input = input("Enter a non-negative integer n to compute the n-th Fibonacci number (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting...")
            return
        n = int(user_input)
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is {result}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a non-negative integer or 'q' to quit.")

if __name__ == "__main__":
    main()