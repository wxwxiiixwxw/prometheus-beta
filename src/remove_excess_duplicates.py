def remove_excess_duplicates(input_string):
    """
    Remove characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    
    Examples:
        >>> remove_excess_duplicates("aabbbcccc")
        'aabbcc'
        >>> remove_excess_duplicates("abcde")
        'abcde'
        >>> remove_excess_duplicates("")
        ''
    """
    # If input is not a string, raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return input_string
    
    # Count character occurrences preserving order
    result = []
    char_counts = {}
    
    for char in input_string:
        # Keep track of count for each character
        char_counts[char] = char_counts.get(char, 0) + 1
        
        # Only add if count is 1 or 2
        if char_counts[char] <= 2:
            result.append(char)
    
    return ''.join(result)