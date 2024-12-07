import pandas as pd
import gspread
from gspread.spreadsheet import Spreadsheet
from core.google.get_bot_credentials import credentials


def sheet(sheet_id: str) -> Spreadsheet:
    creds = credentials()
    try:
        gc = gspread.authorize(creds)

        spreadsheet = gc.open_by_key(sheet_id)

        return spreadsheet
    except gspread.exceptions.GSpreadException as err:
        print(err)

    
def worksheet(sheet_id: str, sheet_name: str) -> Spreadsheet:
    spreadsheet = sheet(sheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet



