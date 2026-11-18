import logging


def setup_logging():
    log_file_handler = logging.FileHandler("log_file.txt", mode='w', encoding="utf-8")
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(log_file_handler)