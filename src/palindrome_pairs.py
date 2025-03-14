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
    """
    # Input validation
    if not words or len(words) < 2:
        return []
    
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Special case for single character words
    def handle_single_char_case():
        # Collect indices of single character words
        single_char_indices = [i for i, word in enumerate(words) if len(word) == 1]
        
        # For non-single character words that can form palindrome with single chars
        for i in range(len(words)):
            if len(words[i]) == 1:
                continue
            
            for j in single_char_indices:
                if i == j:
                    continue
                
                # Check both orders
                if is_palindrome(words[i] + words[j]):
                    palindrome_pairs.append([i, j])
                if is_palindrome(words[j] + words[i]):
                    palindrome_pairs.append([j, i])
    
    # Handling single character cases first
    handle_single_char_case()
    
    # Check other pairs
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index and single character cases already handled
            if i == j or len(words[i]) == 1 or len(words[j]) == 1:
                continue
            
            # Skip duplicates
            if words[i] == words[j]:
                continue
            
            # Check palindrome pairs
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append([i, j])
    
    return palindrome_pairs