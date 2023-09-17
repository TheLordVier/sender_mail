import os
import json
from mail_config import smtp_server, smtp_port, username, password
from logger import setup_logging, log_info, log_error
from mail_utils import send_email


if __name__ == '__main__':
    # Путь к файлу логов
    log_file_path = os.path.join('logs', 'email_log.log')

    # Настройка логирования
    setup_logging(log_file_path)

    # Загрузка данных из JSON файла
    json_file_path = os.path.join('data', 'list_mail.json')
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Пример использования: отправка писем каждому адресату
    for key, email in data['data'].items():
        subject = 'Test send'
        message = 'Привет, это тестовое письмо с помощью Python и smtplib.'
        success, message = send_email(smtp_server, smtp_port, username, password, email, subject, message)
        if success:
            log_info(message)
        else:
            log_error(message)
