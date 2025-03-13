import pytest
from src.palindrome_word_pairs import find_palindrome_word_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome word pairs"""
    words = ["bat", "tab", "cat"]
    assert (0, 1) in find_palindrome_word_pairs(words)
    assert (1, 0) in find_palindrome_word_pairs(words)

def test_no_palindrome_pairs():
    """Test list with no palindrome pairs"""
    words = ["hello", "world", "python"]
    assert len(find_palindrome_word_pairs(words)) == 0

def test_empty_list():
    """Test empty list input"""
    assert len(find_palindrome_word_pairs([])) == 0

def test_single_word_list():
    """Test list with a single word"""
    words = ["hello"]
    assert len(find_palindrome_word_pairs(words)) == 0

def test_all_palindrome_pairs():
    """Test list where multiple palindrome pairs exist"""
    words = ["abc", "cba", "def", "fed"]
    results = find_palindrome_word_pairs(words)
    assert (0, 1) in results
    assert (1, 0) in results
    assert (2, 3) in results
    assert (3, 2) in results

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_palindrome_word_pairs("not a list")

def test_invalid_list_content():
    """Test that ValueError is raised for list with non-string elements"""
    with pytest.raises(ValueError, match="All elements must be strings"):
        find_palindrome_word_pairs(["valid", 123, "invalid"])