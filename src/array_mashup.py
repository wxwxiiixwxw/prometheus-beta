def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.

    Args:
        array1 (list): First input array of positive integers
        array2 (list): Second input array of positive integers

    Returns:
        list: A new array where each element is the sum of 
              corresponding elements from input arrays

    Raises:
        ValueError: If inputs are not lists of positive integers
        ValueError: If input arrays have different lengths
    """
    # Validate input types
    if not (isinstance(array1, list) and isinstance(array2, list)):
        raise ValueError("Inputs must be lists")
    
    # Validate input contains only positive integers
    if not (all(isinstance(x, int) and x > 0 for x in array1) and 
            all(isinstance(x, int) and x > 0 for x in array2)):
        raise ValueError("All elements must be positive integers")
    
    # Validate array lengths match
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Perform array mashup by summing corresponding elements
    return [a + b for a, b in zip(array1, array2)]