import json
import os
import sys
import re
from datetime import date, datetime

# Takes date as input and returns age as integer.
def calculate_age(birth_date: date) -> int:
    today_date = date.today()

    if birth_date <= today_date:
        return today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))
    else:
        raise ValueError("Birth date cannot be greater than today's date")

# Prints provided string variables in console
def print_entry(*args):
    for param in args:
        print(f"{param}")
    print("")

# Opens provided .json file by file_path, identifies all entries whose age is below 18 and prints them.
def process_file(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            file_data = json.load(file)

    except json.decoder.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {file_path} file import failed. Details: {e}")
        return

    for index, entry in enumerate(file_data):
        try:
            #Extracting json entries
            name = entry["name"]
            birth_date_str = entry["birth_date"]
            gender = entry["gender"]

            #Converting str birthdate to date object
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            entry_age = calculate_age(birth_date)

            #Printing all entries whose age is below 18
            if entry_age < 18:
                print_entry(name, birth_date_str, gender)

        except (KeyError, ValueError) as e:
            print(f"Error: Invalid entry detected and skipped in {file_path} at index {index}. Details: {e}")


# Main script execution. Checking provided command-line arguments. At least one .json file path should be provided
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if os.path.exists(arg) and re.search(r"\.json$", arg):
            process_file(arg)
        else:
            print(f"Error: '{arg}' is not a valid .json file")
else:
    raise ValueError("Please provide at least one .json file name")

