from datetime import datetime

def get_day_of_week(date):
    """
    Return the name of the day for a given date.

    Args:
        date (str or datetime): The date to get the day name for. 
                                Can be a string in 'YYYY-MM-DD' format 
                                or a datetime object.

    Returns:
        str: The full name of the day of the week (e.g., 'Monday', 'Tuesday')

    Raises:
        ValueError: If the input date is in an invalid format or cannot be parsed.
    """
    # If input is a string, convert to datetime
    if isinstance(date, str):
        try:
            # Try parsing the date string
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    
    # If input is not a datetime object after conversion, raise error
    if not isinstance(date, datetime):
        raise TypeError("Input must be a date string or datetime object.")
    
    # Return the full day name
    return date.strftime('%A')