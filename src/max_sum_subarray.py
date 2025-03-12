def find_max_sum_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum sum subarray.
    It works with arrays containing positive and negative integers.
    
    Args:
        arr (list): A list of integers to search for the maximum sum subarray.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    
    Examples:
        >>> find_max_sum_subarray([1, -2, 3, 10, -4, 7, 2, -5])
        22
        >>> find_max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
        7
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Kadane's algorithm with precise tracking of max subarray sum
    max_so_far = arr[0]  # Initialize with first element 
    max_ending_here = arr[0]
    
    for num in arr[1:]:
        # Update max_ending_here to be the maximum of current number or 
        # current number plus previous max_ending_here
        max_ending_here = max(num, max_ending_here + num)
        
        # Update max_so_far if the current max_ending_here is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far