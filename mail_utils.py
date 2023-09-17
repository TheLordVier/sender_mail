import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(smtp_server, smtp_port, username, password, to_address, subject, message):
    try:
        # Create a MIMEText object for the plain text message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach the plain text message
        msg.attach(MIMEText(message, 'plain'))

        # Establish a connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        # Send the email
        server.sendmail(username, to_address, msg.as_string())

        # Close the connection
        server.quit()

        # Return success and a message indicating the email was sent
        return True, f'Email sent to {to_address} with subject: {subject}'

    except Exception as e:
        # Return failure and an error message if sending fails
        return False, f'Failed to send email to {to_address}. Error: {str(e)}'
