import unittest
from unittest.mock import patch
from mail_utils import send_email


class TestSendEmail(unittest.TestCase):

    @patch('mail_utils.smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        # Set up mocks
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.return_value = None
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.return_value = None
        mock_smtp_instance.quit.return_value = None

        # Call the function
        success, message = send_email('smtp.example.com', 587, 'username', 'password',
                                      'to@example.com', 'Test Subject', 'Test Message')

        # Assertions
        self.assertTrue(success)
        self.assertEqual(message, 'Email sent to to@example.com with subject: Test Subject')

    @patch('mail_utils.smtplib.SMTP')
    def test_send_email_failure(self, mock_smtp):
        # Set up mocks to raise an exception
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.return_value = None
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.side_effect = Exception('Mocked exception')

        # Call the function
        success, message = send_email('smtp.example.com', 587, 'username', 'password',
                                      'to@example.com', 'Test Subject', 'Test Message')

        # Assertions
        self.assertFalse(success)
        self.assertIn('Failed to send email to to@example.com.', message)


if __name__ == '__main__':
    unittest.main()
