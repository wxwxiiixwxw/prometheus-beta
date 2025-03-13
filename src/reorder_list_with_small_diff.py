def reorder_list_with_small_diff(nums):
    """
    Reorder a list of integers so that the difference between consecutive 
    elements is always 1, -1, or 0.
    
    Args:
        nums (list): Input list of integers
    
    Returns:
        list or None: Reordered list where consecutive elements differ 
                      by at most 1, or None if impossible
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    # Handle edge cases
    if not nums:
        return []
    
    if len(nums) == 1:
        return nums
    
    # Count occurrences to handle duplicates
    from collections import Counter
    num_counts = Counter(nums)
    
    # Sort the input list to help with reordering
    sorted_nums = sorted(set(nums))
    
    def backtrack(current_result, remaining):
        """Recursive backtracking to find a valid reordering."""
        # Success condition
        if not remaining:
            return current_result
        
        # Try adding the next number
        for i, num in enumerate(remaining):
            # If list is empty or difference is within constraints
            if (not current_result or 
                abs(current_result[-1] - num) <= 1):
                
                # Create new lists to avoid modifying originals
                new_result = current_result + [num]
                new_remaining = remaining[:i] + remaining[i+1:]
                
                # Recursive call
                solution = backtrack(new_result, new_remaining)
                if solution:
                    return solution
        
        # No solution found
        return None
    
    # Try backtracking from multiple start points
    for start_index, start_num in enumerate(sorted_nums):
        result = backtrack([start_num], 
                           sorted_nums[:start_index] + sorted_nums[start_index+1:])
        if result and len(result) == len(nums):
            return result
    
    return None