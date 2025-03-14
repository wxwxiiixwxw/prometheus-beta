import pytest
from src.balanced_parentheses import is_balanced_parentheses

def test_simple_balanced_parentheses():
    """Test basic balanced parentheses cases."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("()()") == True

def test_nested_balanced_parentheses():
    """Test nested balanced parentheses cases."""
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("((()()))") == True

def test_multiple_types_of_parentheses():
    """Test multiple types of balanced parentheses."""
    assert is_balanced_parentheses("()[]{}") == True
    assert is_balanced_parentheses("([{}])") == True
    assert is_balanced_parentheses("([]){}()") == True

def test_unbalanced_parentheses():
    """Test unbalanced parentheses cases."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("((") == False
    assert is_balanced_parentheses("))") == False
    assert is_balanced_parentheses("(()") == False
    assert is_balanced_parentheses("())") == False

def test_mismatched_parentheses():
    """Test mismatched parentheses types."""
    assert is_balanced_parentheses("([)]") == False
    assert is_balanced_parentheses("(]") == False
    assert is_balanced_parentheses("[)") == False

def test_empty_string():
    """Test empty string case."""
    assert is_balanced_parentheses("") == True

def test_string_with_other_characters():
    """Test strings with non-parentheses characters."""
    assert is_balanced_parentheses("a(b)c") == True
    assert is_balanced_parentheses("a((b)c)") == True
    assert is_balanced_parentheses("(a(b)c)") == True

def test_complex_cases():
    """Test complex balanced and unbalanced cases."""
    assert is_balanced_parentheses("({[]})") == True
    assert is_balanced_parentheses("(a+b)*(c-d)") == True
    assert is_balanced_parentheses("((a+b)*(c-d))") == True
    assert is_balanced_parentheses("(a+b)*(c-d") == False