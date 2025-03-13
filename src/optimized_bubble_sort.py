def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces unnecessary iterations.
    
    Key optimizations:
    1. Tracks if any swaps occurred in each pass
    2. Stops early if no swaps are made in a full pass
    3. Reduces iterations by tracking the last sorted position
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps occurred in this pass
        swapped = False
        
        # Last i elements are already in place, so reduce iterations
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr