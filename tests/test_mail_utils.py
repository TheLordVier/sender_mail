import unittest
from mail_utils import send_email


class TestEmailUtils(unittest.TestCase):
    def test_send_email(self):
        # Replace with your test data
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        username = 'test@example.com'
        password = 'password'
        to_address = 'recipient@example.com'
        subject = 'Test Subject'
        message = 'Test Message'

        success, response = send_email(smtp_server, smtp_port, username, password, to_address, subject, message)

        # Assert that email was sent successfully
        self.assertTrue(success)
        self.assertIn('Email sent to', response)


if __name__ == '__main__':
    unittest.main()
