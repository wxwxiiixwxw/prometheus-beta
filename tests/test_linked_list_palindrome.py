import pytest
from src.linked_list_palindrome import ListNode, is_palindrome_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create the linked list from.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_palindrome_empty_list():
    """Test that an empty list is considered a palindrome."""
    assert is_palindrome_linked_list(None) == True

def test_palindrome_single_element():
    """Test that a single-element list is a palindrome."""
    head = create_linked_list([5])
    assert is_palindrome_linked_list(head) == True

def test_palindrome_even_length():
    """Test a palindrome with even number of elements."""
    head = create_linked_list([1, 2, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_palindrome_odd_length():
    """Test a palindrome with odd number of elements."""
    head = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_non_palindrome_even_length():
    """Test a non-palindrome with even number of elements."""
    head = create_linked_list([1, 2, 3, 4])
    assert is_palindrome_linked_list(head) == False

def test_non_palindrome_odd_length():
    """Test a non-palindrome with odd number of elements."""
    head = create_linked_list([1, 2, 3, 4, 5])
    assert is_palindrome_linked_list(head) == False

def test_longer_palindrome():
    """Test a longer palindrome sequence."""
    head = create_linked_list([1, 2, 3, 4, 3, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_longer_non_palindrome():
    """Test a longer non-palindrome sequence."""
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    assert is_palindrome_linked_list(head) == False