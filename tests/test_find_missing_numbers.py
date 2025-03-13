import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test basic functionality of finding missing numbers"""
    arr = [1, 2, 4, 6, 3, 7, 8]
    assert find_missing_numbers(arr) == [5]

def test_find_missing_numbers_no_missing():
    """Test case where no numbers are missing"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_multiple_missing():
    """Test case with multiple missing numbers"""
    arr = [1, 3, 7, 9]
    assert find_missing_numbers(arr) == [2, 4, 5, 6, 8]

def test_find_missing_numbers_single_element():
    """Test case with a single element array"""
    arr = [5]
    assert find_missing_numbers(arr) == [3, 4, 6, 7]

def test_find_missing_numbers_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_find_missing_numbers_non_integer():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="Input array must contain only integers"):
        find_missing_numbers([1, 2, 'a', 4])

def test_find_missing_numbers_negative_numbers():
    """Test case with negative numbers"""
    arr = [-3, -1, 0, 2]
    assert find_missing_numbers(arr) == [-2, 1]

def test_find_missing_numbers_unsorted():
    """Test that the function works with unsorted input"""
    arr = [4, 1, 7, 3, 9]
    assert find_missing_numbers(arr) == [2, 5, 6, 8]