import os
import json
from mail_config import smtp_server, smtp_port, username, password
from logger import setup_logging, log_info, log_error
from mail_utils import send_email


if __name__ == '__main__':
    # Path to the log file
    log_file_path = os.path.join('logs', 'email_log.log')

    # Setup logging
    setup_logging(log_file_path)

    # Load data from the JSON file
    json_file_path = os.path.join('data', 'list_mail.json')
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Example usage: sending emails to each recipient
    for key, email in data['data'].items():
        subject = 'Test send'
        message = 'Hello, this is a test email using Python and smtplib!'
        success, message = send_email(smtp_server, smtp_port, username, password, email, subject, message)
        if success:
            log_info(message)
        else:
            log_error(message)
