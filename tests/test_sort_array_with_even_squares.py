import pytest
from src.sort_array_with_even_squares import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic sorting functionality"""
    arr = [3, 1, 2, 4, 5]
    expected = [1, 3, 5, 16, 4]
    assert sort_array_with_even_squares(arr) == expected

def test_all_even_numbers():
    """Test array with only even numbers"""
    arr = [4, 2, 6, 8]
    expected = [2, 4, 6, 64]
    assert sort_array_with_even_squares(arr) == expected

def test_no_even_numbers():
    """Test array with no even numbers"""
    arr = [1, 3, 5, 7]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(arr) == expected

def test_empty_array():
    """Test empty array"""
    arr = []
    expected = []
    assert sort_array_with_even_squares(arr) == expected

def test_single_element():
    """Test single element array"""
    arr = [5]
    expected = [5]
    assert sort_array_with_even_squares(arr) == expected

def test_with_negative_numbers():
    """Test array with negative numbers"""
    arr = [-3, -2, 1, 4, -5, 2]
    expected = [-5, -3, 1, 4, 16, 4]
    assert sort_array_with_even_squares(arr) == expected

def test_input_type_error():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")

def test_mixed_complexity():
    """Test a more complex mixed case"""
    arr = [10, 3, 2, 8, 1, 6, 4]
    expected = [1, 3, 4, 6, 10, 64, 36]
    assert sort_array_with_even_squares(arr) == expected