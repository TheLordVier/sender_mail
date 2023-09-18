import unittest
from logger import setup_logging, log_info, log_error


class TestLogging(unittest.TestCase):

    def test_log_info(self):
        """
        Set up the log file path and configure logging
        """
        log_file_path = 'logs/test.log'
        setup_logging(log_file_path)

        # Log an information message
        message = 'This is an info message.'
        log_info(message)

        # Check if the message is present in the log file
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            self.assertTrue(message in logs)  # Check if the message is in the logs

    def test_log_error(self):
        """
        Set up the log file path and configure logging
        """
        log_file_path = 'logs/test.log'
        setup_logging(log_file_path)

        # Log an error message
        message = 'This is an error message.'
        log_error(message)

        # Check if the error message is present in the log file
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            self.assertTrue(message in logs)  # Check if the error message is in the logs


if __name__ == '__main__':
    unittest.main()
