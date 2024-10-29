"""
This module contains a function to add promotion records to a Google Sheet.

Functions:
    add_promotion(records: list): Adds promotion records to a Google Sheet.

Usage:
    Run this module to add promotion records to a Google Sheet.
"""
import pandas as pd
import gspread
from core.google.get_bot_credentials import credentials


def lines(records: list, sheet_key: str, sheet_name: str):
    """
    Adds records to a Google Sheet.
    This function takes a list of records, appends them to an existing
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

        spreadsheet = gc.open_by_key(sheet_key)

        worksheet = spreadsheet.worksheet(sheet_name)
        updated_records = pd.DataFrame.from_records(records)

        # Update the Google Sheet with the modified DataFrame
        response = worksheet.append_rows(updated_records.values.tolist())
        if response:
            print(f"Records added to {sheet_name} sheet.")
    except gspread.exceptions.GSpreadException as err:
        print(err)
