import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from max_sum_subarray import find_max_sum_subarray

def test_basic_positive_array():
    """Test a basic array with positive numbers"""
    assert find_max_sum_subarray([1, 2, 3, 4, 5]) == 15

def test_array_with_negative_numbers():
    """Test an array with both positive and negative numbers"""
    assert find_max_sum_subarray([1, -2, 3, 10, -4, 7, 2, -5]) == 18

def test_all_negative_numbers():
    """Test an array with all negative numbers"""
    assert find_max_sum_subarray([-1, -2, -3, -4, -5]) == -1

def test_single_element_array():
    """Test an array with a single element"""
    assert find_max_sum_subarray([42]) == 42

def test_zero_sum_array():
    """Test an array where the max sum is zero"""
    assert find_max_sum_subarray([-1, -2, 0, -3, -4]) == 0

def test_error_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_max_sum_subarray([])

def test_error_non_list_input():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_sum_subarray("not a list")

def test_error_non_numeric_elements():
    """Test that list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_sum_subarray([1, 2, "three", 4, 5])

def test_mixed_types_numeric():
    """Test that the function works with mixed numeric types"""
    assert find_max_sum_subarray([1, 2.5, -3, 4, -5.5]) == 4.5