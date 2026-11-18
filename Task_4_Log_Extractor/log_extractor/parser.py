import logging
import re
from pathlib import Path

from .io_utils import read_file

logger = logging.getLogger(__name__)

pattern_base = "EncryptionToken=[a-zA-Z0-9+/=_-]+:[a-zA-Z0-9+/=_-]+"
all_sessions_pattern = re.compile(pattern_base + r'"')

def print_all_sessions(input_file_path):

    sessions = list_sessions(input_file_path)
    if sessions:
        print_available_sessions(sessions)
        logger.debug(f"{len(sessions)} sessions have been found in the {input_file_path} file")
    else:
        logger.debug(f"No sessions found in the provided file")
        print("Provided file doesn't contain any sessions")

def list_sessions(in_file_path: Path):
    sessions = []

    for line in read_file(in_file_path):
        match = all_sessions_pattern.search(line)
        if match:
            sessions.append(match.group())

    return sessions

def parse_session(in_file_path: Path, session_id: str):

    target_session = re.compile(pattern_base + f"{re.escape(session_id)}" + r'"')
    copying = False
    extracted_session = []

    # Analyzes the file content line by line until the specified session_id is located.
    # Extracts lines until the next session_id starts or EOF reached
    for line in read_file(in_file_path):

        if target_session.search(line):
            copying = True

        elif all_sessions_pattern.search(line):
            if copying:
                break

        if copying:
            extracted_session.append(line)

    return extracted_session


def print_available_sessions(sessions):
    print("\n")
    print("Available sessions in the log file:" + '\n')

    for session in sessions:
        print(session)

    print("\n")
    print("Please, specify a specific session you want to extract logs for with the "
          "--session_id={last few characters of a session} option")
