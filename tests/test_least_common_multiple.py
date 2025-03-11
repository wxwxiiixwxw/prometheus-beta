import pytest
from src.least_common_multiple import find_lcm

def test_lcm_basic_positive_numbers():
    """Test LCM of basic positive numbers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(2, 3) == 6

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(5, 5) == 5
    assert find_lcm(7, 7) == 7

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(4, 8) == 8
    assert find_lcm(7, 14) == 14

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert find_lcm(5, 7) == 35
    assert find_lcm(11, 13) == 143

def test_lcm_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm("4", 5)

def test_lcm_non_positive_numbers():
    """Test error handling for non-positive numbers"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(-3, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(4, -5)