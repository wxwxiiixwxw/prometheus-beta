import pytest
from src.nested_list_flatten import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple list."""
    input_list = [1, 2, 3]
    assert flatten_nested_list(input_list) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    input_list = [1, [2, 3], 4]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    input_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_nested_list([]) == []

def test_flatten_list_with_mixed_types():
    """Test flattening a list with mixed types."""
    input_list = [1, 'a', [2, [3.14, 'b']], {'c': 4}]
    assert flatten_nested_list(input_list) == [1, 'a', 2, 3.14, 'b', {'c': 4}]

def test_non_list_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list("not a list")
        flatten_nested_list(123)
        flatten_nested_list(None)