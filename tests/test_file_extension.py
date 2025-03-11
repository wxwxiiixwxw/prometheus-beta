import pytest
import os
from src.file_extension import get_file_extension

def test_get_file_extension_normal_cases():
    # Test various file extensions
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'
    assert get_file_extension('archive.tar.gz') == 'gz'

def test_get_file_extension_paths():
    # Test with full paths
    assert get_file_extension('/home/user/document.txt') == 'txt'
    assert get_file_extension('C:\\Users\\Name\\file.docx') == 'docx'

def test_get_file_extension_no_extension():
    # Test files without extension
    assert get_file_extension('README') == ''
    assert get_file_extension('/path/to/filename') == ''

def test_get_file_extension_hidden_files():
    # Test hidden files (dotfiles)
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('/home/user/.bashrc') == ''

def test_get_file_extension_error_handling():
    # Test error cases
    with pytest.raises(TypeError):
        get_file_extension(None)
    
    with pytest.raises(TypeError):
        get_file_extension(123)
    
    with pytest.raises(ValueError):
        get_file_extension('')

def test_get_file_extension_edge_cases():
    # Edge cases with special characters
    assert get_file_extension('file.with.multiple.dots.txt') == 'txt'
    assert get_file_extension('file_with_no_extension') == ''