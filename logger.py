import logging
import os


def setup_logging(log_file_path):
    # Проверяем наличие папки "logs" и создаем, если не существует
    log_directory = os.path.dirname(log_file_path)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Настройка логирования
    logging.basicConfig(filename=log_file_path, level=logging.INFO)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
