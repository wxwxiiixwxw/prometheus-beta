def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list of tuple): List of (weight, value) tuples representing items
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid (negative weights/capacity, non-numeric inputs)
    """
    # Input validation
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    if not items:
        return 0
    
    # Validate items
    for weight, value in items:
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Item weights must be non-negative numbers")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item values must be non-negative numbers")
    
    # Convert to integers to avoid floating-point precision issues
    capacity = int(capacity)
    items = [(int(weight), int(value)) for weight, value in items]
    
    # Initialize dynamic programming table
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build solution bottom-up
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Include current item if possible
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Return maximum value
    max_value = max(dp[n])
    return max_value