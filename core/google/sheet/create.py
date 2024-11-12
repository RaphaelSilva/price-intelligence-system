import gspread
from gspread.spreadsheet import Spreadsheet
from core.google.get_bot_credentials import credentials


def new_file(file_name: str, folder: str = "1CcUaKifkZH90TXDYVsEo1jY_kt4DnrG4") -> Spreadsheet:
    creds = credentials()
    try:
        gc = gspread.authorize(creds)
        spreadsheet = gc.create(file_name, folder)

        return spreadsheet
    except gspread.exceptions.GSpreadException as err:
        print(err)
