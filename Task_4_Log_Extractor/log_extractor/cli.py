import argparse


def parse_args():
    # Parsing CommandLine arguments with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_file", type=str, required=True, help='Input file. Mandatory')
    parser.add_argument('--session_id', type=str, help='Session_ID to extract logs for the session. Optional')
    parser.add_argument('--out_file', type=str, help='Output file. Optional')

    return parser.parse_args()