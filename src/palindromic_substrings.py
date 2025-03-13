def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in the given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list[str]: A sorted list of all unique palindromic substrings in the input string
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abba")
        ['a', 'ab', 'abba', 'b', 'bb']
    """
    # Handle edge cases
    if not s or not isinstance(s, str):
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for start in range(len(s)):
        for end in range(start, len(s)):
            # Check if substring is palindrome
            substring = s[start:end+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return sorted(list(palindromes))