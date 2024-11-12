from typing import Any, Dict, List
import gspread
from core.google.get_bot_credentials import credentials


def folder(folder: str = "1CcUaKifkZH90TXDYVsEo1jY_kt4DnrG4") -> List[Dict[str, Any]]:
    creds = credentials()
    try:
        gc = gspread.authorize(creds)
        files = gc.list_spreadsheet_files(folder)
        if files:
            for file in files:
                print(file)
        return files
    except gspread.exceptions.GSpreadException as err:
        print(err)


if __name__ == "__main__":
    folder()
