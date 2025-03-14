import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios"""
    # Simple palindrome pairs
    result = find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    assert len(result) > 0  # Some palindrome pairs exist

def test_empty_input():
    """Test empty input and single word input"""
    assert find_palindrome_pairs([]) == []
    assert find_palindrome_pairs(["a"]) == []

def test_no_palindrome_pairs():
    """Test case with no palindrome pairs"""
    assert len(find_palindrome_pairs(["cat", "dog", "bird"])) == 0

def test_single_char_palindromes():
    """Test palindrome pairs with single character words"""
    result = find_palindrome_pairs(["a", "b", "c", "ab", "ba"])
    assert len(result) > 0  # Some palindrome pairs exist

def test_duplicate_words():
    """Test handling of duplicate words"""
    result = find_palindrome_pairs(["a", "a"])
    assert len(result) > 0  # Some pairs are found

def test_long_palindrome_pairs():
    """Test palindrome pairs with longer words"""
    result = find_palindrome_pairs(["race", "car", "racecar"])
    assert len(result) > 0  # Some palindrome pairs exist

def test_large_input():
    """Test larger input to check performance"""
    words = ["a"] * 100  # large number of identical words
    result = find_palindrome_pairs(words)
    assert len(result) > 0  # Expect multiple pairs