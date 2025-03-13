def find_palindrome_word_pairs(words):
    """
    Find pairs of indices where words form palindromes when their characters are reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing indices of palindrome word pairs.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-string elements.
    """
    # Validate input type
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    
    # Validate list contents
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    # Store palindrome pairs
    palindrome_pairs = []
    
    # Check all possible pairs of indices
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index comparisons
            if i == j:
                continue
            
            # Reverse the word at index j and concatenate with word at index i
            combined = words[i] + words[j][::-1]
            
            # Check if the combined word is a palindrome
            if combined == combined[::-1]:
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs