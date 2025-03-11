import sys
import time
from typing import Callable, Optional


class ProcessProgressLogger:
    """
    A utility class for logging real-time progress of a process.
    
    This class provides methods to track and display progress of long-running tasks
    with customizable output and formatting.
    """

    def __init__(self, total_steps: int, prefix: str = 'Progress:', 
                 suffix: str = 'Complete', 
                 decimals: int = 1, 
                 length: int = 50, 
                 fill: str = '█', 
                 print_end: str = "\r"):
        """
        Initialize the progress logger.

        Args:
            total_steps (int): Total number of steps in the process
            prefix (str, optional): Prefix text for the progress bar. Defaults to 'Progress:'.
            suffix (str, optional): Suffix text for the progress bar. Defaults to 'Complete'.
            decimals (int, optional): Number of decimal places for percentage. Defaults to 1.
            length (int, optional): Character length of the progress bar. Defaults to 50.
            fill (str, optional): Bar fill character. Defaults to '█'.
            print_end (str, optional): End character for print. Defaults to "\r".
        """
        self.total_steps = total_steps
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.start_time = time.time()

    def update(self, current_step: int) -> None:
        """
        Update and print the progress bar.

        Args:
            current_step (int): Current step of the process.
        
        Raises:
            ValueError: If current_step is less than 0 or greater than total_steps.
        """
        if current_step < 0 or current_step > self.total_steps:
            raise ValueError(f"Current step must be between 0 and {self.total_steps}")

        # Calculate percentage and bar length
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (current_step / float(self.total_steps)))
        filled_length = int(self.length * current_step // self.total_steps)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)

        # Calculate time metrics
        elapsed_time = time.time() - self.start_time
        estimated_total_time = elapsed_time * (self.total_steps / current_step) if current_step > 0 else 0
        remaining_time = max(0, estimated_total_time - elapsed_time)

        # Construct the output
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix}'
        output += f' (Elapsed: {elapsed_time:.2f}s, Remaining: {remaining_time:.2f}s)'

        # Print the output
        print(output, end=self.print_end, flush=True)

        # Print newline when process is complete
        if current_step == self.total_steps:
            print()

    @staticmethod
    def track_process(process: Callable, total_steps: int, **kwargs) -> None:
        """
        Decorator-like method to track the progress of a given process.

        Args:
            process (Callable): The process/function to track
            total_steps (int): Total number of steps in the process
            **kwargs: Additional arguments to pass to ProcessProgressLogger

        Returns:
            The result of the process
        """
        logger = ProcessProgressLogger(total_steps, **kwargs)
        
        def wrapper():
            for step in range(total_steps + 1):
                logger.update(step)
                # Small delay to simulate processing
                time.sleep(0.1)
            return process()
        
        return wrapper()