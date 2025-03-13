import pytest
from src.palindromic_substrings import find_palindromic_substrings

def test_empty_string():
    """Test empty string returns empty list"""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test single character returns list with that character"""
    assert find_palindromic_substrings("a") == ["a"]

def test_no_palindromes():
    """Test string with no complex palindromes"""
    assert find_palindromic_substrings("abc") == ["a", "b", "c"]

def test_multiple_palindromes():
    """Test string with multiple palindromes"""
    result = find_palindromic_substrings("abba")
    assert result == ["a", "ab", "abba", "b", "bb"]

def test_repeated_characters():
    """Test string with repeated characters"""
    result = find_palindromic_substrings("aaa")
    assert result == ["a", "aa", "aaa"]

def test_mixed_palindromes():
    """Test string with mixed palindromic substrings"""
    result = find_palindromic_substrings("racecar")
    assert set(result) == set(["r", "a", "c", "e", "cec", "racecar", "aceca"])

def test_non_string_input():
    """Test non-string input returns empty list"""
    assert find_palindromic_substrings(123) == []

def test_unicode_characters():
    """Test unicode characters"""
    result = find_palindromic_substrings("анна")
    assert set(result) == set(["а", "анн", "анна", "нн"])