import os
import platform

def clear_console_and_log(message):
    """
    Clear the console screen and then log a message.

    This function uses platform-specific methods to clear the console screen
    before printing the provided message. It supports Windows, macOS, and Linux.

    Args:
        message (str): The message to log after clearing the console.

    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Determine the operating system and use appropriate clear command
    system = platform.system().lower()
    
    try:
        if system == 'windows':
            os.system('cls')
        elif system in ['linux', 'darwin']:  # darwin is macOS
            os.system('clear')
        else:
            # Fallback for unknown systems
            print('\n' * 100)  # Print multiple newlines to "clear" the console
    except Exception as e:
        print(f"Error clearing console: {e}")

    # Log the message after clearing
    print(message)