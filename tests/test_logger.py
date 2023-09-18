import unittest
from logger import setup_logging, log_info, log_error


class TestLogging(unittest.TestCase):

    def test_log_info(self):
        log_file_path = 'logs/test.log'
        setup_logging(log_file_path)

        message = 'This is an info message.'
        log_info(message)

        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            self.assertTrue(message in logs)

    def test_log_error(self):
        log_file_path = 'logs/test.log'
        setup_logging(log_file_path)

        message = 'This is an error message.'
        log_error(message)

        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            self.assertTrue(message in logs)


if __name__ == '__main__':
    unittest.main()
