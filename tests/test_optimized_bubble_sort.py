import pytest
from src.optimized_bubble_sort import optimized_bubble_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_already_sorted():
    """Test when list is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test when list is in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert optimized_bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test empty list"""
    arr = []
    assert optimized_bubble_sort(arr) == []

def test_single_element():
    """Test list with single element"""
    arr = [42]
    assert optimized_bubble_sort(arr) == [42]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_negative_numbers():
    """Test list with negative numbers"""
    arr = [-5, 2, -8, 0, 3, -1]
    assert optimized_bubble_sort(arr) == sorted(arr)

def test_invalid_input():
    """Test invalid input raises TypeError"""
    with pytest.raises(TypeError):
        optimized_bubble_sort("not a list")
    with pytest.raises(TypeError):
        optimized_bubble_sort(123)
    with pytest.raises(TypeError):
        optimized_bubble_sort(None)