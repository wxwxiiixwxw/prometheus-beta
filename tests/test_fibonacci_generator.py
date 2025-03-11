import pytest
from src.fibonacci_generator import generate_fibonacci_sequence

def test_fibonacci_sequence_basic():
    """Test basic Fibonacci sequence generation"""
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_sequence_zero_terms():
    """Test generating 0 terms"""
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_sequence_one_term():
    """Test generating 1 term"""
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two_terms():
    """Test generating 2 terms"""
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_many_terms():
    """Test generating a longer Fibonacci sequence"""
    assert generate_fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_invalid_input_negative():
    """Test generating sequence with negative input"""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_sequence_invalid_input_type():
    """Test generating sequence with invalid input type"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(None)