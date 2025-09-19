import sys
import logging

def error_message_detail(error: Exception, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    message = f"Error in [{file_name}] at the line [{line_number}]: {str(error)}"
    logging.error(message)
    return message

class ProjectException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        
    def __str__(self):
        return self.error_message