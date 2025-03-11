import pytest
from datetime import datetime, timedelta
from src.date_difference import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between identical dates"""
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 0

def test_calculate_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 11)
    assert calculate_days_between_dates(date1, date2) == 10

def test_calculate_days_between_dates_reverse_order():
    """Test that order of dates doesn't matter"""
    date1 = datetime(2023, 1, 11)
    date2 = datetime(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 10

def test_calculate_days_between_dates_string_input():
    """Test calculating days with date string inputs"""
    date1 = "2023-01-01"
    date2 = "2023-01-11"
    assert calculate_days_between_dates(date1, date2) == 10

def test_calculate_days_between_dates_iso_format():
    """Test calculating days with ISO format strings"""
    date1 = "2023-01-01T00:00:00Z"
    date2 = "2023-01-11T00:00:00Z"
    assert calculate_days_between_dates(date1, date2) == 10

def test_calculate_days_between_dates_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(ValueError):
        calculate_days_between_dates("invalid date", "2023-01-11")

def test_calculate_days_between_dates_mixed_input_types():
    """Test calculating days with mixed input types"""
    date1 = datetime(2023, 1, 1)
    date2 = "2023-01-11"
    assert calculate_days_between_dates(date1, date2) == 10

def test_calculate_days_between_dates_long_duration():
    """Test calculating days for a longer time span"""
    date1 = datetime(2020, 1, 1)
    date2 = datetime(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 1096  # 3 years including leap years