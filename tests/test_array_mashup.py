import pytest
from src.array_mashup import arrayMashup

def test_basic_array_mashup():
    """Test basic array mashup functionality"""
    assert arrayMashup([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def test_single_element_arrays():
    """Test mashup with single-element arrays"""
    assert arrayMashup([1], [2]) == [3]

def test_zero_length_arrays():
    """Test mashup with empty arrays"""
    assert arrayMashup([], []) == []

def test_large_numbers():
    """Test mashup with larger numbers"""
    assert arrayMashup([1000, 2000], [3000, 4000]) == [4000, 6000]

def test_mismatched_length_arrays():
    """Test that different length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [3, 4, 5])

def test_non_positive_integers():
    """Test that non-positive integers raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, -5, 6])

def test_non_integer_inputs():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, 5.5, 6])

def test_non_list_inputs():
    """Test that non-list inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        arrayMashup((1, 2, 3), [4, 5, 6])