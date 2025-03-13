import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5)]  # (weight, value)
    capacity = 5
    assert solve_knapsack(items, capacity) == 7  # Item with weight 2 and 3

def test_empty_items():
    """Test with empty list of items"""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test when knapsack capacity is zero"""
    items = [(1, 10), (2, 20), (3, 30)]
    assert solve_knapsack(items, 0) == 0

def test_single_item_fits():
    """Test when a single item fits exactly"""
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10

def test_single_item_doesnt_fit():
    """Test when a single item doesn't fit"""
    items = [(6, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_multiple_combinations():
    """Test scenario with multiple possible combinations"""
    items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    capacity = 7
    assert solve_knapsack(items, capacity) == 12  # Items with value 4 and 7

def test_floating_point_inputs():
    """Test with floating point weights and values"""
    items = [(2.5, 3.0), (3.2, 4.5), (4.1, 5.2)]
    capacity = 5.5
    assert solve_knapsack(items, capacity) == 7  # Verify proper handling of floats

def test_invalid_negative_capacity():
    """Test handling of negative capacity"""
    items = [(1, 10), (2, 20)]
    with pytest.raises(ValueError, match="Capacity must be a non-negative number"):
        solve_knapsack(items, -5)

def test_invalid_negative_weight():
    """Test handling of negative item weight"""
    items = [(1, 10), (-2, 20)]
    with pytest.raises(ValueError, match="Item weights must be non-negative numbers"):
        solve_knapsack(items, 10)

def test_invalid_negative_value():
    """Test handling of negative item value"""
    items = [(1, -10), (2, 20)]
    with pytest.raises(ValueError, match="Item values must be non-negative numbers"):
        solve_knapsack(items, 10)