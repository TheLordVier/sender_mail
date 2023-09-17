import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(smtp_server, smtp_port, username, password, to_address, subject, message):
    try:
        # ������� ������ MIMEText ��� ���������� ������
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_address
        msg['Subject'] = subject

        # ��������� ��������� ���������
        msg.attach(MIMEText(message, 'plain'))

        # ������������� ���������� � SMTP-��������
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        # ���������� ������
        server.sendmail(username, to_address, msg.as_string())

        # ��������� ����������
        server.quit()

        return True, f'Email sent to {to_address} with subject: {subject}'

    except Exception as e:
        return False, f'Failed to send email to {to_address}. Error: {str(e)}'
