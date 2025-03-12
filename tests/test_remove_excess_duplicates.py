import pytest
from src.remove_excess_duplicates import remove_excess_duplicates

def test_remove_excess_duplicates_basic():
    """Test basic functionality of removing excess duplicates."""
    assert remove_excess_duplicates("aabbbcccc") == "aabbcc"
    assert remove_excess_duplicates("abcde") == "abcde"

def test_remove_excess_duplicates_empty_string():
    """Test behavior with empty string."""
    assert remove_excess_duplicates("") == ""

def test_remove_excess_duplicates_all_unique():
    """Test string with all unique characters."""
    assert remove_excess_duplicates("abcdefg") == "abcdefg"

def test_remove_excess_duplicates_multiple_duplicates():
    """Test string with multiple types of duplicates."""
    assert remove_excess_duplicates("aabbccddeeefff") == "aabbccddee"

def test_remove_excess_duplicates_preserve_two():
    """Ensure exactly two occurrences of each character are preserved."""
    assert remove_excess_duplicates("aaabbbccc") == "aabbcc"

def test_remove_excess_duplicates_edge_cases():
    """Test various edge cases."""
    assert remove_excess_duplicates("   ") == "  "
    assert remove_excess_duplicates("!!!") == "!!"

def test_remove_excess_duplicates_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        remove_excess_duplicates(123)
    with pytest.raises(TypeError):
        remove_excess_duplicates(None)
    with pytest.raises(TypeError):
        remove_excess_duplicates(["a", "b", "c"])