from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime): First date 
        date2 (str or datetime): Second date

    Returns:
        int: Number of days between the two dates (absolute value)

    Raises:
        ValueError: If dates cannot be parsed or are invalid
    """
    # Convert input to datetime objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.fromisoformat(date1.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.fromisoformat(date2.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}")
    
    # Validate that inputs are datetime objects
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Inputs must be datetime objects or valid date strings")
    
    # Calculate the absolute difference in days
    delta = abs((date2 - date1).days)
    
    return delta