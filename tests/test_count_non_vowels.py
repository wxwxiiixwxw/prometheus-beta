import pytest
from src.count_non_vowels import count_non_vowel_chars

def test_count_non_vowel_chars():
    # Test various scenarios
    assert count_non_vowel_chars("hello") == 3, "Should count 3 non-vowels in 'hello'"
    assert count_non_vowel_chars("WORLD") == 4, "Should handle uppercase correctly"
    assert count_non_vowel_chars("aeiou") == 0, "Should return 0 for all vowels"
    assert count_non_vowel_chars("") == 0, "Should handle empty string"
    assert count_non_vowel_chars("123!@#") == 6, "Should count non-alphabetic characters"
    assert count_non_vowel_chars("Python Programming") == 13, "Should work with mixed case and spaces"
    
def test_edge_cases():
    # Additional edge case tests
    assert count_non_vowel_chars(" ") == 1, "Should count space as non-vowel"
    assert count_non_vowel_chars("xyz") == 3, "Should work with all consonants"
    
def test_case_insensitivity():
    # Test case insensitivity
    assert count_non_vowel_chars("AeIoU") == 0, "Should handle mixed case vowels"
    assert count_non_vowel_chars("Hello WORLD") == 7, "Should work with mixed case"