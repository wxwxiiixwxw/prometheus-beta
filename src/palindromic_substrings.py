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
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Single characters always become palindromes
    for i in range(len(s)):
        palindromes.add(s[i])
    
    return sorted(list(palindromes))