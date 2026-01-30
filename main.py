def fibonacci(n):
    """Calculate the n-th Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b


def main():
    """Main function to handle user input and output."""
    try:
        n = int(input("Enter the position in the Fibonacci sequence: "))
        if n < 0:
            print("Error: Please enter a non-negative integer.")
            return
        
        result = fibonacci(n)
        print(f"The {n}-th Fibonacci number is: {result}")
        
        # Also show the sequence up to n
        sequence = [fibonacci(i) for i in range(n+1)]
        print(f"Fibonacci sequence up to position {n}: {sequence}")
    
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()