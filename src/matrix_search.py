def search_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix with specific constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order from left to right
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): A 2D matrix meeting the specified constraints
        target (int): The value to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is invalid or empty
    
    Time Complexity: O(log(m*n)), where m is number of rows and n is number of columns
    Space Complexity: O(1)
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Get matrix dimensions
    rows, cols = len(matrix), len(matrix[0])
    
    # Perform binary search on the entire matrix
    left, right = 0, rows * cols - 1
    
    while left <= right:
        # Calculate mid point
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        row = mid // cols
        col = mid % cols
        
        # Get the current value
        current = matrix[row][col]
        
        # Compare and adjust search space
        if current == target:
            return True
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False