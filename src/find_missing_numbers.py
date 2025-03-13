def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers.
    
    Returns:
        list: A sorted list of missing numbers in the range from the minimum to the maximum of the input array.
    
    Raises:
        ValueError: If the input array is empty or contains non-integer values.
    """
    # Check for empty array
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Validate input is a list of integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Input array must contain only integers")
    
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a set of the input array for O(1) lookup
    arr_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val, max_val + 1) 
        if num not in arr_set
    ]
    
    return missing_numbers