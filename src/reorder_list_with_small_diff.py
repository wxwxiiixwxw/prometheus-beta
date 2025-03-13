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
    
    # Sort the input list to help with reordering
    sorted_nums = sorted(nums)
    
    # Try to create a valid reordering
    result = [sorted_nums[0]]
    used = {sorted_nums[0]}
    
    def can_add(current, candidate):
        """Check if candidate can be added to the result."""
        diff = abs(current - candidate)
        return diff in {0, 1} and candidate not in used
    
    # Try to build the list
    while len(result) < len(nums):
        # Find a suitable next number
        found_next = False
        for num in sorted_nums:
            if can_add(result[-1], num):
                result.append(num)
                used.add(num)
                found_next = True
                break
        
        # If no suitable number found, backtrack or return None
        if not found_next:
            return None
    
    return result if len(result) == len(nums) else None