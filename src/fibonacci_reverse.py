def fibonacci_reverse(n):
    """
    Generate a list of Fibonacci numbers up to the Nth element in reverse order.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> fibonacci_reverse(0)
        []
        >>> fibonacci_reverse(1)
        [0]
        >>> fibonacci_reverse(5)
        [3, 2, 1, 1, 0]
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for small inputs
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    # Generate Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Return in reverse order, taking first n elements
    return list(reversed(fib[:n]))