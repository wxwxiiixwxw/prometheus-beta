import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic scenarios of finding palindrome pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert set(map(tuple, result)) == {(0, 1), (1, 0)}, "Should find palindrome pairs"

def test_advanced_palindrome_pairs():
    """Test advanced scenarios with multiple palindrome pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected = {(0, 1), (1, 0), (3, 4), (4, 3)}
    assert set(map(tuple, result)) == expected, "Should handle complex palindrome pair scenarios"

def test_empty_input():
    """Test input with an empty list of words."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list for empty input"

def test_single_word_input():
    """Test input with a single word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list for single word input"

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs."""
    words = ["foo", "bar", "baz"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list when no palindrome pairs exist"

def test_same_word_pairs():
    """Ensure function does not return pairs of the same index."""
    words = ["hi", "hi"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should not return pairs with the same index"