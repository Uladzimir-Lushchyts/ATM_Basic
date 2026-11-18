import sys
from pathlib import Path
import logging
from .log_setup import setup_logging
from .io_utils import write_session
from .parser import print_all_sessions, parse_session
from .cli import parse_args
from .time_logger import time_logger
from .file_operation_error import FileOperationError

logger = logging.getLogger(__name__)

@time_logger
def main():

    setup_logging()

    args = parse_args()

    logger.debug(f"Program started. Provided arguments:"
                 f" in_file:{args.in_file}"
                 f", session_id:{args.session_id}"
                 f", out_file:{args.out_file}"
                 )

    try:
        # Resolving absolute path to the file
        input_file_path = Path(args.in_file).resolve()

        # If target session_id is not specified
        if args.session_id is None:
            # parsing the log file and printing all available session_ids to pick up a specific one
            print_all_sessions(input_file_path)
        else:

            # if specific session_id is provided, searching the log file for the session info
            session = parse_session(input_file_path, args.session_id)

            # if session info is found
            if session:

                # if output file is not provided - creating a new file at the same location as input file
                output_file_path = Path(args.out_file).resolve() if args.out_file \
                    else input_file_path.with_name(f"{input_file_path.stem}_parsed.log")

                logger.info(f"Output file path: {output_file_path}")

                # writing found session to the output file and handling exceptions
                write_session(output_file_path, session)

            # If specified session hasn't been found in the log file printing all available sessions
            else:
                print("Provided file doesn't contain the specified session")
                logger.debug(f"Provided file doesn't contain the specified session_id: {args.session_id}")
                print_all_sessions(input_file_path)

    except FileOperationError as e:
        logger.error(f"FileOperationError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
