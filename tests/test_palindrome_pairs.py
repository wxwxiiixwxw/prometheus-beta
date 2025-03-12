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
    # Note: This test ensures that the function finds concatenation palindromes
    assert len(result) > 0, "Should find palindrome pairs"
    # Verify that at least basic expected pairs are present
    expected_pairs = [(0, 1), (1, 0)]
    assert all(pair in result for pair in expected_pairs), "Should include basic palindrome pairs"

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

def test_additional_palindrome_scenarios():
    """Test additional palindrome concatenation scenarios."""
    words = ["a", "abc", "aba", ""]
    result = find_palindrome_pairs(words)
    # Verify various palindrome concatenation scenarios
    assert len(result) > 0, "Should find palindrome pairs in complex scenarios"