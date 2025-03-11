import pytest
from datetime import datetime
from src.day_of_week import get_day_of_week

def test_get_day_of_week_string_input():
    """Test getting day of week from a string input."""
    assert get_day_of_week('2023-06-14') == 'Wednesday'
    assert get_day_of_week('2023-06-15') == 'Thursday'

def test_get_day_of_week_datetime_input():
    """Test getting day of week from a datetime input."""
    date = datetime(2023, 6, 14)
    assert get_day_of_week(date) == 'Wednesday'

def test_get_day_of_week_invalid_string():
    """Test error handling for invalid string format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('14-06-2023')

def test_get_day_of_week_invalid_input():
    """Test error handling for invalid input type."""
    with pytest.raises(TypeError, match="Input must be a date string or datetime object"):
        get_day_of_week(12345)

def test_different_dates():
    """Test various dates to ensure correct day names."""
    test_cases = [
        ('2023-01-01', 'Sunday'),
        ('2023-12-25', 'Monday'),
        ('2024-02-29', 'Thursday'),  # Leap year
    ]
    
    for date_str, expected_day in test_cases:
        assert get_day_of_week(date_str) == expected_day