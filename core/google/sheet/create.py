import gspread
from gspread.spreadsheet import Spreadsheet
from core.constants import GDrive
from core.google.get_bot_credentials import credentials


def new_file(file_name: str, sheet_name: str = None, folder: str = GDrive.folder()) -> Spreadsheet:
    creds = credentials()
    try:
        gc = gspread.authorize(creds)
        spreadsheet = gc.create(file_name, folder)
        if sheet_name:
            spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=20)            
            spreadsheet.del_worksheet(spreadsheet.sheet1)

        permissions = spreadsheet.list_permissions()
        owner = next(filter(lambda x: x['emailAddress'] == 'eng.raphaelsn@gmail.com', permissions), None)
        spreadsheet.transfer_ownership(owner['id'])  
          

        return spreadsheet
    except gspread.exceptions.GSpreadException as err:
        print(err)


if __name__ == "__main__":
    import datetime as dt
    new_file(f'Test-{dt.datetime.now().isoformat()}', 'etl')