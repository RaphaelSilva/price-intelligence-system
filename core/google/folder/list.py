from typing import Any, Dict, List
import gspread
from core.constants import GDrive
from core.google.get_bot_credentials import credentials


def folder(folder: str = GDrive.folder()) -> List[Dict[str, Any]]:
    creds = credentials()
    try:
        gc = gspread.authorize(creds)
        files = gc.list_spreadsheet_files(folder_id=folder)
        return files
    except gspread.exceptions.GSpreadException as err:
        print(err)


if __name__ == "__main__":
    folder()
