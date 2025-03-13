import pytest
from src.reorder_list_with_small_diff import reorder_list_with_small_diff

def test_normal_case():
    """Test a typical case where reordering is possible."""
    nums = [4, 2, 1, 3]
    result = reorder_list_with_small_diff(nums)
    assert result is not None
    
    # Verify constraints
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_already_ordered():
    """Test when the list is already valid."""
    nums = [1, 2, 3, 4]
    result = reorder_list_with_small_diff(nums)
    assert result is not None
    assert result == [1, 2, 3, 4]

def test_impossible_reordering():
    """Test a case where reordering is impossible."""
    nums = [1, 3, 6, 10]
    result = reorder_list_with_small_diff(nums)
    assert result is None

def test_empty_list():
    """Test empty list input."""
    nums = []
    result = reorder_list_with_small_diff(nums)
    assert result == []

def test_single_element():
    """Test list with single element."""
    nums = [5]
    result = reorder_list_with_small_diff(nums)
    assert result == [5]

def test_duplicate_elements():
    """Test list with duplicate elements."""
    nums = [1, 1, 2, 2]
    result = reorder_list_with_small_diff(nums)
    assert result is not None
    
    # Verify constraints
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1
    
    # Verify all original numbers are used
    assert sorted(result) == sorted(nums)

def test_mixed_large_small_numbers():
    """Test list with mixed large and small numbers."""
    nums = [100, 1, 50, 2, 99]
    result = reorder_list_with_small_diff(nums)
    assert result is not None
    
    # Verify constraints
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1
    
    # Verify all original numbers are used
    assert sorted(result) == sorted(nums)