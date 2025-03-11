import pytest
import io
import sys
from src.console_utils import clear_console_and_log

def test_clear_console_and_log_valid_message(capsys):
    """Test that the function logs a valid message."""
    test_message = "Hello, World!"
    clear_console_and_log(test_message)
    
    # Capture the output
    captured = capsys.readouterr()
    assert test_message in captured.out

def test_clear_console_and_log_empty_string(capsys):
    """Test logging an empty string."""
    clear_console_and_log("")
    
    # Capture the output
    captured = capsys.readouterr()
    assert captured.out.strip() == ""

def test_clear_console_and_log_invalid_type():
    """Test that an invalid input type raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        clear_console_and_log(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        clear_console_and_log(None)

def test_clear_console_and_log_unicode_message(capsys):
    """Test logging a message with Unicode characters."""
    unicode_message = "こんにちは世界"
    clear_console_and_log(unicode_message)
    
    # Capture the output
    captured = capsys.readouterr()
    assert unicode_message in captured.out