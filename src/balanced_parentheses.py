def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.

    Args:
        s (str): Input string to check for balanced parentheses.

    Returns:
        bool: True if all parentheses are balanced, False otherwise.

    Examples:
        >>> is_balanced_parentheses("()")  # Simple balanced case
        True
        >>> is_balanced_parentheses("(())")  # Nested balanced case
        True
        >>> is_balanced_parentheses("()()")  # Multiple sets of parentheses
        True
        >>> is_balanced_parentheses("(()")  # Unbalanced case
        False
        >>> is_balanced_parentheses(")("  # Unbalanced case
        False
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Mapping of closing to opening parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    
    # Set of opening parentheses
    opening_parentheses = set(parentheses_map.values())
    
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char in opening_parentheses:
            stack.append(char)
        
        # If it's a closing parenthesis
        elif char in parentheses_map:
            # If stack is empty or top of stack doesn't match, return False
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            
            # Remove the matching opening parenthesis
            stack.pop()
    
    # Return True only if stack is empty (all parentheses matched)
    return len(stack) == 0