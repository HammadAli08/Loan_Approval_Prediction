import sys # sys provides access to some variables used or maintained to manipulate different parts of the Python runtime environment.
from src.Logger import logging # Import the logging object from the Logger module in the src package.


def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message including file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # File where error occurred
    line_number = exc_tb.tb_lineno  # Line number of error
    error_message = (
        f"Error occurred in script: {file_name} at line number: {line_number} "
        f"error message: {str(error)}"
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class that logs detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
