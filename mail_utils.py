import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(smtp_server, smtp_port, username, password, to_address, subject, message):
    try:
        # Создаем объект MIMEText для текстового письма
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_address
        msg['Subject'] = subject

        # Добавляем текстовое сообщение
        msg.attach(MIMEText(message, 'plain'))

        # Устанавливаем соединение с SMTP-сервером
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        # Отправляем письмо
        server.sendmail(username, to_address, msg.as_string())

        # Закрываем соединение
        server.quit()

        return True, f'Email sent to {to_address} with subject: {subject}'

    except Exception as e:
        return False, f'Failed to send email to {to_address}. Error: {str(e)}'
