import logging


def setup_logging():
    # File log handler for Debug and above level messages
    log_file_handler = logging.FileHandler("log_file.txt", mode='a', encoding="utf-8")
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

    # Console log handler for Errors and higher level messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Root logger setup
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Adding log handlers
    root_logger.addHandler(log_file_handler)
    root_logger.addHandler(console_handler)