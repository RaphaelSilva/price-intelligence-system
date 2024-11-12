import pandas as pd
import gspread
from core.google.get_bot_credentials import credentials


def lines(records: list, sheet_key: str, sheet_name: str):
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
