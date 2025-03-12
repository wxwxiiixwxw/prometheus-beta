import pytest
import zstandard as zstd
from src.zstandard_compression import compress_data, decompress_data


def test_compress_str_data():
    """Test compressing a string"""
    test_string = "Hello, world! This is a test of Zstandard compression."
    compressed = compress_data(test_string)
    
    # Ensure compression actually reduces data and produces bytes
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(test_string.encode('utf-8'))


def test_compress_bytes_data():
    """Test compressing bytes"""
    test_bytes = b"Binary data compression test"
    compressed = compress_data(test_bytes)
    
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(test_bytes)


def test_decompress_data():
    """Test full compression and decompression cycle"""
    test_string = "Testing Zstandard compression and decompression"
    
    # Compress
    compressed = compress_data(test_string)
    
    # Decompress
    decompressed = decompress_data(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string


def test_compression_levels():
    """Test different compression levels"""
    test_data = "Testing different compression levels"
    
    # Test extreme compression levels
    low_comp = compress_data(test_data, compression_level=1)
    mid_comp = compress_data(test_data, compression_level=10)
    high_comp = compress_data(test_data, compression_level=22)
    
    # Verify they are different lengths
    assert len(low_comp) >= len(mid_comp)
    assert len(mid_comp) >= len(high_comp)


def test_invalid_compression_level():
    """Test invalid compression levels raise ValueError"""
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=0)
    
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=23)


def test_invalid_input_types():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        compress_data(None)
    
    with pytest.raises(TypeError):
        decompress_data("Not bytes")
    
    with pytest.raises(TypeError):
        decompress_data(123)


def test_empty_data():
    """Test compression and decompression of empty data"""
    empty_str = ""
    empty_bytes = b""
    
    # String
    compressed_str = compress_data(empty_str)
    decompressed_str = decompress_data(compressed_str)
    assert decompressed_str.decode('utf-8') == empty_str
    
    # Bytes
    compressed_bytes = compress_data(empty_bytes)
    decompressed_bytes = decompress_data(compressed_bytes)
    assert decompressed_bytes == empty_bytes


def test_large_data():
    """Test compression of large data"""
    large_data = "x" * 1_000_000
    
    compressed = compress_data(large_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == large_data