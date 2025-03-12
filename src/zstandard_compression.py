import zstandard as zstd
import io
from typing import Union, Optional


def compress_data(data: Union[str, bytes], compression_level: int = 3) -> bytes:
    """
    Compress data using Zstandard compression algorithm.

    Args:
        data (Union[str, bytes]): The data to compress. 
            If str, it will be encoded to UTF-8 bytes.
        compression_level (int, optional): Compression level from 1-22. 
            Defaults to 3. Higher levels provide better compression 
            but take longer to process.

    Returns:
        bytes: Compressed data

    Raises:
        ValueError: If compression level is out of valid range
        TypeError: If input data is not str or bytes
    """
    # Validate compression level
    if not 1 <= compression_level <= 22:
        raise ValueError("Compression level must be between 1 and 22")

    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Create Zstandard compressor
    cctx = zstd.ZstdCompressor(level=compression_level)
    
    # Compress the data
    return cctx.compress(data)


def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zstandard compressed data.

    Args:
        compressed_data (bytes): Zstandard compressed data

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        zstd.ZstdError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Create Zstandard decompressor
    dctx = zstd.ZstdDecompressor()
    
    # Decompress the data
    return dctx.decompress(compressed_data)