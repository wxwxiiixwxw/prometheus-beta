import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios"""
    # Simple palindrome pairs
    assert sorted(find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])) == \
           sorted([[0, 1], [1, 0], [3, 4], [4, 3]])

def test_empty_input():
    """Test empty input and single word input"""
    assert find_palindrome_pairs([]) == []
    assert find_palindrome_pairs(["a"]) == []

def test_no_palindrome_pairs():
    """Test case with no palindrome pairs"""
    assert find_palindrome_pairs(["cat", "dog", "bird"]) == []

def test_single_char_palindromes():
    """Test palindrome pairs with single character words"""
    result = find_palindrome_pairs(["a", "b", "c", "ab", "ba"])
    assert sorted(result) == sorted([[1, 4], [4, 1], [2, 3], [3, 2]])

def test_duplicate_words():
    """Test handling of duplicate words"""
    result = find_palindrome_pairs(["a", "a"])
    assert result == []

def test_long_palindrome_pairs():
    """Test palindrome pairs with longer words"""
    result = find_palindrome_pairs(["race", "car", "racecar"])
    assert sorted(result) == sorted([[1, 2], [2, 1]])

def test_large_input():
    """Test larger input to check performance"""
    words = ["a"] * 100  # large number of identical words
    result = find_palindrome_pairs(words)
    assert len(result) == 0  # no palindrome pairs