import os

def get_file_extension(file_path):
    """
    Get the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (without the dot) or an empty string if no extension exists.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is an empty string.
    """
    # Check for input type
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Extract the file extension using os.path.splitext
    _, extension = os.path.splitext(file_path)
    
    # Remove the leading dot and return
    return extension.lstrip('.')