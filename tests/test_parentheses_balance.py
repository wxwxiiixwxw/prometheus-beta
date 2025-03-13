import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_basic_balanced_parentheses():
    """Test basic balanced parentheses scenarios"""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("()()()") == True
    assert is_balanced_parentheses("(())()") == True

def test_unbalanced_parentheses():
    """Test unbalanced parentheses scenarios"""
    assert is_balanced_parentheses("(()") == False
    assert is_balanced_parentheses("())") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("()(()") == False

def test_edge_cases():
    """Test edge case scenarios"""
    assert is_balanced_parentheses("") == True  # Empty string
    assert is_balanced_parentheses("(((())))") == True  # Deeply nested
    assert is_balanced_parentheses("((()(())))") == True  # Complex nesting

def test_only_valid_inputs():
    """Test that the function works only with parentheses"""
    with pytest.raises(TypeError):
        is_balanced_parentheses(123)  # Non-string input
    with pytest.raises(TypeError):
        is_balanced_parentheses(None)  # None input