def count_non_vowel_chars(input_string: str) -> int:
    """
    Count the number of non-vowel characters in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        int: The number of non-vowel characters.

    Notes:
        - Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive)
        - Non-alphabetic characters are considered non-vowels
        - Empty string returns 0
    """
    # Handle edge case of empty string
    if not input_string:
        return 0
    
    # Define vowels (lowercase for case-insensitive comparison)
    vowels = set('aeiou')
    
    # Count non-vowel characters
    return sum(1 for char in input_string.lower() if char not in vowels)