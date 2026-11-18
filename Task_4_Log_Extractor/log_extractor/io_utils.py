import logging
from pathlib import Path
from .file_operation_error import FileOperationError

logger = logging.getLogger(__name__)

def handle_io_error(e: Exception, operation: str, path: Path):
    if isinstance(e, FileNotFoundError):
        message = f"Specified file doesn't exist. File Path: {path}"
    elif isinstance(e, PermissionError):
        message = f"No permissions to {operation} the file. File Path: {path}"
    elif isinstance(e, IsADirectoryError):
        message = f"Specified file is a directory. File Path: {path}"
    elif isinstance(e, UnicodeDecodeError):
        message = f"Specified file has non-UTF-8 encoding. File Path: {path}"
    else:
        message = f"Unexpected error occurred during file {operation}. File: {path}"

    print(f"{message}")
    logger.error(f"{type(e).__name__}: {e}")
    raise FileOperationError(message) from e

def write_session(output_file_path: Path, session: list[str]):

    try:
        if output_file_path.is_dir():
            raise IsADirectoryError(f"{output_file_path} is a directory")

        with open(output_file_path, "w", encoding="utf-8") as file:
            file.writelines(session)
            print(f"File has been successfully written to {output_file_path}")
            logger.info(f"File has successfully written to {output_file_path}")

    except Exception as e:
        handle_io_error(e, "write", output_file_path)

def read_file(in_file_path: Path):
    try:
        if Path.is_dir(in_file_path):
            raise IsADirectoryError(f"{in_file_path} is a directory")

        with open(in_file_path, mode='r', encoding ="utf-8") as file:
            yield from file

    except Exception as e:
        handle_io_error(e, "read", in_file_path)