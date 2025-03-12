import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test well-known palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindromes."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True

def test_edge_cases():
    """Test edge cases."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("!!") == True  # Just special characters

def test_case_sensitivity():
    """Test case-insensitive palindrome checking."""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric and special characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False

def test_non_palindromes():
    """Test various non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_input_types():
    """Test different input types and error handling."""
    with pytest.raises(TypeError):
        is_palindrome(None)
    
    with pytest.raises(TypeError):
        is_palindrome(123)  # Non-string input