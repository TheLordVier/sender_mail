import unittest
import os
from logger import log_info, log_error


class TestLogger(unittest.TestCase):
    def test_log_info(self):
        log_info('This is a test info log message')

        # Check if the log file was created
        self.assertTrue(os.path.exists('logs/email_log.log'))

    def test_log_error(self):
        log_error('This is a test error log message')

        # Check if the log file was created
        self.assertTrue(os.path.exists('logs/email_log.log'))


if __name__ == '__main__':
    unittest.main()
