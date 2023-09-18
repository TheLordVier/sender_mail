import unittest
from unittest.mock import patch
from mail_utils import send_email


class TestSendEmail(unittest.TestCase):

    @patch('mail_utils.smtplib.SMTP')  # Use the patch decorator to mock the SMTP class from mail_utils.
    def test_send_email_success(self, mock_smtp):
        """
        Set up mocks for a successful email send
        """
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.return_value = None
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.return_value = None
        mock_smtp_instance.quit.return_value = None

        # Call the send_email function with mock SMTP server and capture the result
        success, message = send_email('smtp.example.com', 587, 'username', 'password',
                                      'to@example.com', 'Test Subject', 'Test Message')

        # Assertions to test if the email sending was successful
        self.assertTrue(success)
        self.assertEqual(message, 'Email sent to to@example.com with subject: Test Subject')

    @patch('mail_utils.smtplib.SMTP')  # Mock the SMTP class again for a failure scenario
    def test_send_email_failure(self, mock_smtp):
        """
        Set up mocks to simulate an exception during email send
        """
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.return_value = None
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.side_effect = Exception('Mocked exception')

        # Call the send_email function with mock SMTP server and capture the result
        success, message = send_email('smtp.example.com', 587, 'username',
                                      'password', 'to@example.com', 'Test Subject',
                                      'Test Message')

        # Assertions to test if the email sending failed
        self.assertFalse(success)
        self.assertIn('Failed to send email to to@example.com.', message)


if __name__ == '__main__':
    unittest.main()
