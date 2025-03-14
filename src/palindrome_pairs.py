def find_palindrome_pairs(words):
    """
    Find indices of pairs of words that form palindromes when concatenated.
    
    A palindrome pair is a pair of words (i, j) such that when concatenated 
    in either order (words[i] + words[j] or words[j] + words[i]), 
    the result is a palindrome.
    
    Args:
        words (List[str]): A list of strings to check for palindrome pairs
    
    Returns:
        List[List[int]]: A list of pairs of indices where palindrome pairs exist
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the length of the longest word
    Space Complexity: O(1) excluding the output list
    
    Examples:
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 4], [4, 3]]
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    # Input validation
    if not words or len(words) < 2:
        return []
    
    palindrome_pairs = []
    
    # Check all possible pairs
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index pairs
            if i == j:
                continue
            
            # Check if concatenation forms a palindrome in both orders
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append([i, j])
    
    return palindrome_pairs