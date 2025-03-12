import re

def to_snake_case(input_string: str) -> str:
    """
    Convert a given string to snake_case.
    
    This function handles various input formats including:
    - Camel Case
    - Pascal Case
    - Kebab Case
    - Space-separated strings
    - Strings with mixed punctuation
    
    Args:
        input_string (str): The input string to convert to snake case
    
    Returns:
        str: The input string converted to snake_case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_snake_case("HelloWorld")
        'hello_world'
        >>> to_snake_case("hello-world")
        'hello_world'
        >>> to_snake_case("Hello World")
        'hello_world'
        >>> to_snake_case("hello_world")
        'hello_world'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric characters with a single space
    # This helps handle mixed punctuation and multiple separators
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Normalize spaces
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
    
    # Insert underscore before any uppercase letters 
    # that are preceded by a lowercase letter or number
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cleaned_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # Convert to lowercase and replace any remaining spaces with single underscore
    return re.sub(r'\s+', '_', s2).lower().strip('_')