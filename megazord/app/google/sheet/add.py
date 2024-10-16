"""
This module contains a function to add promotion records to a Google Sheet.

Functions:
    add_promotion(records: list): Adds promotion records to a Google Sheet.

Usage:
    Run this module to add promotion records to a Google Sheet.
"""
import pandas as pd
import gspread
from app.google.get_credentials import credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "11RRrpwKYwYOx8B8TrsTlCWmhDwU6fyE3uRpwZFvgm0M"
SAMPLE_RANGE_NAME = "A1:E"


def add_promotion(records: list):
    """
    Adds promotion records to a Google Sheet.
    This function takes a list of promotion records, appends them to an existing
    Google Sheet, and updates the sheet with the new data.
    Args:
        records (list): A list of dictionaries, where each dictionary represents
                        a promotion record to be added to the Google Sheet.
    Raises:
        gspread.exceptions.GSpreadException: If there is an error while accessing
                                             or updating the Google Sheet.
    Example:
        records = [
            {"column1": "value1", "column2": "value2"},
            {"column1": "value3", "column2": "value4"}
        ]
        add_promotion(records)
    """
    creds = credentials()

    try:

        gc = gspread.authorize(creds)

        spreadsheet = gc.open_by_key(
            "11RRrpwKYwYOx8B8TrsTlCWmhDwU6fyE3uRpwZFvgm0M")

        worksheet = spreadsheet.worksheet('Feed')
        updated_records = pd.DataFrame.from_records(records)

        # Update the Google Sheet with the modified DataFrame
        response = worksheet.append_rows(updated_records.values.tolist())
        print(response)
        print("Promotion added successfully!")
    except gspread.exceptions.GSpreadException as err:
        print(err)
