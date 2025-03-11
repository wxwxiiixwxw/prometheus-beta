import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_positive_numbers():
    """Test set bit counting for various positive integers."""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(5) == 2  # Binary: 101
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(255) == 8  # Binary: 11111111

def test_count_set_bits_negative_numbers():
    """Test set bit counting for negative integers."""
    assert count_set_bits(-5) == 2  # Absolute value of 5
    assert count_set_bits(-15) == 4  # Absolute value of 15
    assert count_set_bits(-1) == 1  # Absolute value of 1

def test_count_set_bits_large_numbers():
    """Test set bit counting for larger integers."""
    assert count_set_bits(1024) == 1  # Binary: 10000000000
    assert count_set_bits(2**16 - 1) == 16  # All 16 bits set

def test_count_set_bits_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    
    with pytest.raises(TypeError):
        count_set_bits(None)