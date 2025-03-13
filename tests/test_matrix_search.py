import pytest
from src.matrix_search import search_matrix

def test_search_matrix_valid_matrix():
    """Test searching in a valid matrix with various scenarios."""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    # Test existing elements
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 23) == True
    assert search_matrix(matrix, 60) == True
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 61) == False

def test_search_matrix_edge_cases():
    """Test edge cases like single-row, single-column, and boundary values."""
    # Single row matrix
    single_row = [[1, 3, 5, 7]]
    assert search_matrix(single_row, 3) == True
    assert search_matrix(single_row, 4) == False
    
    # Single column matrix
    single_col = [[1], [3], [5], [7]]
    assert search_matrix(single_col, 3) == True
    assert search_matrix(single_col, 4) == False

def test_search_matrix_empty_invalid():
    """Test error handling for empty or invalid matrices."""
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_search_matrix_large_matrix():
    """Test a larger matrix to ensure scaling."""
    large_matrix = [
        [x for x in range(1, 11)],
        [y for y in range(11, 21)],
        [z for z in range(21, 31)]
    ]
    
    assert search_matrix(large_matrix, 15) == True
    assert search_matrix(large_matrix, 25) == True
    assert search_matrix(large_matrix, 0) == False
    assert search_matrix(large_matrix, 32) == False