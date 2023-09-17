# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import logging
#
# # Настройки почтового аккаунта
# smtp_server = 'smtp.mail.ru'
# smtp_port = 587
# username = 'xaviniesta1991@mail.ru'  # Ваша почта на mail.ru
# password = 'zX4fcb4PsZpq77APycSE'  # Пароль от вашей почты для внешнего приложения (генерируется отдельно)
#
#
# # Функция для отправки письма
# def send_email(to_address, subject, message):
#     try:
#         # Создаем объект MIMEText для текстового письма
#         msg = MIMEMultipart()
#         msg['From'] = username
#         msg['To'] = to_address
#         msg['Subject'] = subject
#
#         # Добавляем текстовое сообщение
#         msg.attach(MIMEText(message, 'plain'))
#
#         # Устанавливаем соединение с SMTP-сервером
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(username, password)
#
#         # Отправляем письмо
#         server.sendmail(username, to_address, msg.as_string())
#
#         # Закрываем соединение
#         server.quit()
#
#         # Логирование успешной отправки
#         logging.info(f'Email sent to {to_address} with subject: {subject}')
#
#     except Exception as e:
#         # Логирование ошибок
#         logging.error(f'Failed to send email to {to_address}. Error: {str(e)}')
#
#
# # Пример использования
# if __name__ == '__main__':
#     logging.basicConfig(filename='email_log.log', level=logging.INFO)
#     to_address = 'xaviniesta1991@mail.ru'
#     subject = 'Тестовое письмо'
#     message = 'Привет, это тестовое письмо с помощью Python и smtplib. Проверка!'
#
#     send_email(to_address, subject, message)


# import os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import logging
#
# from mail_config import smtp_server, smtp_port, username, password
#
# # Проверяем наличие папки "logs" и создаем, если не существует
# log_directory = "logs"
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)
#
#
# # Функция для отправки письма
# def send_email(to_address, subject, message):
#     try:
#         # Создаем объект MIMEText для текстового письма
#         msg = MIMEMultipart()
#         msg['From'] = username
#         msg['To'] = to_address
#         msg['Subject'] = subject
#
#         # Добавляем текстовое сообщение
#         msg.attach(MIMEText(message, 'plain'))
#
#         # Устанавливаем соединение с SMTP-сервером
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(username, password)
#
#         # Отправляем письмо
#         server.sendmail(username, to_address, msg.as_string())
#
#         # Закрываем соединение
#         server.quit()
#
#         # Логирование успешной отправки
#         logging.info(f'Email sent to {to_address} with subject: {subject}')
#
#     except Exception as e:
#         # Логирование ошибок
#         logging.error(f'Failed to send email to {to_address}. Error: {str(e)}')
#
#
# # Пример использования
# if __name__ == '__main__':
#     # Устанавливаем путь к файлу лога
#     log_file_path = os.path.join(log_directory, 'email_log.log')
#
#     # Настраиваем логирование
#     logging.basicConfig(filename=log_file_path, level=logging.INFO)
#
#     to_address = 'xaviniesta1991@mail.ru'
#     subject = 'Тестовое письмо для отправки'
#     message = 'Привет, это тестовое письмо с помощью Python и smtplib.'
#
#     send_email(to_address, subject, message)


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import logging
# import json
# import os
# from mail_config import smtp_server, smtp_port, username, password
#
# # Настройка логирования
# log_file_path = os.path.join('logs', 'email_log.log')
# logging.basicConfig(filename=log_file_path, level=logging.INFO)
#
#
# # Функция для отправки письма
# def send_email(to_address, subject, message):
#     try:
#         # Создаем объект MIMEText для текстового письма
#         msg = MIMEMultipart()
#         msg['From'] = username
#         msg['To'] = to_address
#         msg['Subject'] = subject
#
#         # Добавляем текстовое сообщение
#         msg.attach(MIMEText(message, 'plain'))
#
#         # Устанавливаем соединение с SMTP-сервером
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(username, password)
#
#         # Отправляем письмо
#         server.sendmail(username, to_address, msg.as_string())
#
#         # Закрываем соединение
#         server.quit()
#
#         # Логирование успешной отправки
#         logging.info(f'Email sent to {to_address} with subject: {subject}')
#
#     except Exception as e:
#         # Логирование ошибок
#         logging.error(f'Failed to send email to {to_address}. Error: {str(e)}')
#
#
# # Загрузка данных из JSON файла
# json_file_path = os.path.join('data', 'list_mail.json')
# with open(json_file_path, 'r') as json_file:
#     data = json.load(json_file)
#
# # Пример использования: отправка писем каждому адресату
# for key, email in data['data'].items():
#     subject = 'Тестовое письмо'
#     message = 'Привет, это тестовое письмо с помощью Python и smtplib.'
#     send_email(email, subject, message)


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import logging
# import json
# import os
# from mail_config import smtp_server, smtp_port, username, password
#
# # Проверяем наличие папки "logs" и создаем, если не существует
# log_directory = "logs"
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)
#
# # Настройка логирования
# log_file_path = os.path.join(log_directory, 'email_log.log')
# logging.basicConfig(filename=log_file_path, level=logging.INFO)
#
#
# # Функция для отправки письма
# def send_email(to_address, subject, message):
#     try:
#         # Создаем объект MIMEText для текстового письма
#         msg = MIMEMultipart()
#         msg['From'] = username
#         msg['To'] = to_address
#         msg['Subject'] = subject
#
#         # Добавляем текстовое сообщение
#         msg.attach(MIMEText(message, 'plain'))
#
#         # Устанавливаем соединение с SMTP-сервером
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(username, password)
#
#         # Отправляем письмо
#         server.sendmail(username, to_address, msg.as_string())
#
#         # Закрываем соединение
#         server.quit()
#
#         # Логирование успешной отправки
#         logging.info(f'Email sent to {to_address} with subject: {subject}')
#
#     except Exception as e:
#         # Логирование ошибок
#         logging.error(f'Failed to send email to {to_address}. Error: {str(e)}')
#
#
# if __name__ == '__main__':
#     # Загрузка данных из JSON файла
#     json_file_path = os.path.join('data', 'list_mail.json')
#     with open(json_file_path, 'r') as json_file:
#         data = json.load(json_file)
#
#     # Пример использования: отправка писем каждому адресату
#     for key, email in data['data'].items():
#         subject = 'Тестовое письмо'
#         message = 'Привет, это тестовое письмо с помощью Python и smtplib.'
#         send_email(email, subject, message)


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
