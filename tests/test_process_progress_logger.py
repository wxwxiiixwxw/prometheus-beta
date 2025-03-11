import pytest
import time
import io
import sys
from src.process_progress_logger import ProcessProgressLogger


def test_progress_logger_initialization():
    """Test initialization of ProcessProgressLogger."""
    total_steps = 100
    logger = ProcessProgressLogger(total_steps)
    
    assert logger.total_steps == 100
    assert logger.prefix == 'Progress:'
    assert logger.suffix == 'Complete'
    assert logger.decimals == 1
    assert logger.length == 50


def test_progress_logger_update(capsys):
    """Test the update method of ProcessProgressLogger."""
    total_steps = 10
    logger = ProcessProgressLogger(total_steps)
    
    # Capture stdout
    logger.update(5)
    captured = capsys.readouterr()
    
    # Check the output contains key elements
    assert '|' in captured.out
    assert '%' in captured.out
    assert 'Elapsed:' in captured.out
    assert 'Remaining:' in captured.out


def test_progress_logger_invalid_steps():
    """Test handling of invalid step values."""
    total_steps = 10
    logger = ProcessProgressLogger(total_steps)
    
    # Test negative step
    with pytest.raises(ValueError, match="Current step must be between 0 and 10"):
        logger.update(-1)
    
    # Test step greater than total
    with pytest.raises(ValueError, match="Current step must be between 0 and 10"):
        logger.update(11)


def test_track_process():
    """Test the track_process decorator-like method."""
    def mock_process():
        return "Process Complete"
    
    total_steps = 5
    tracked_process = ProcessProgressLogger.track_process(mock_process, total_steps)
    
    # Run the tracked process and check the return value
    result = tracked_process
    assert result == "Process Complete"


def test_process_logger_customization():
    """Test customization of ProcessProgressLogger."""
    total_steps = 20
    logger = ProcessProgressLogger(
        total_steps,
        prefix='Custom Prefix:',
        suffix='Done',
        decimals=2,
        length=30,
        fill='#'
    )
    
    assert logger.prefix == 'Custom Prefix:'
    assert logger.suffix == 'Done'
    assert logger.decimals == 2
    assert logger.length == 30
    assert logger.fill == '#'