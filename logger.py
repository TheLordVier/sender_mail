import logging
import os


def setup_logging(log_file_path):
    """
    Set up logging by creating the logs directory if it doesn't exist and configuring logging.

    :param log_file_path: Path to the log file
    """
    # Check for the existence of the "logs" directory and create it if it doesn't exist
    log_directory = os.path.dirname(log_file_path)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Configure logging
    logging.basicConfig(filename=log_file_path, level=logging.INFO)


def log_info(message):
    """
    Log an informational message.

    :param message: Message to be logged
    """
    logging.info(message)


def log_error(message):
    """
    Log an error message.

    :param message: Error message to be logged
    """
    logging.error(message)
