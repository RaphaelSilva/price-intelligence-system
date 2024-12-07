from typing import Optional
import pandas as pd
import gspread
from core.google.get_bot_credentials import credentials_authorized
from gspread.spreadsheet import Spreadsheet


def header(records: list, sheet_name: str, sheet_key: Optional[str] = None, spreadsheet: Optional[Spreadsheet] = None):
    try:
        gc = credentials_authorized()

        spreadsheet = spreadsheet if spreadsheet else gc.open_by_key(sheet_key)

        worksheet = spreadsheet.worksheet(sheet_name)
        header = pd.DataFrame.from_records(records).columns.tolist()

        # Update the Google Sheet with the modified DataFrame
        response = worksheet.append_rows([header])
        if response:
            print(f"Header added to {sheet_name} sheet.")
        return spreadsheet
    except gspread.exceptions.GSpreadException as err:
        print(err)
        raise err


def lines(records: list, sheet_name: str, sheet_key: Optional[str] = None, spreadsheet: Optional[Spreadsheet] = None):
    try:
        gc = credentials_authorized()

        spreadsheet = spreadsheet if spreadsheet else gc.open_by_key(sheet_key)

        worksheet = spreadsheet.worksheet(sheet_name)
        updated_records = pd.DataFrame.from_records(records).values.tolist()


        # Update the Google Sheet with the modified DataFrame
        response = worksheet.append_rows(updated_records)
        if response:
            print(f"Records added to {sheet_name} sheet.")
        return spreadsheet
    except gspread.exceptions.GSpreadException as err:
        print(err)
        raise err


if __name__ == "__main__":
    data = [
        {'Source': 'Magazine Luiza', 'SourceKey': '12345', 'Title': 'Notebook', 'Price': '1000',
            'Link': 'www.magazineluiza.com.br', 'ImageLink': 'www.magazineluiza.com.br/img', 'Date': '15/10/2024'},
        {'Source': 'Americanas', 'SourceKey': '67890', 'Title': 'Smartphone', 'Price': '2000', 
         'Link': 'www.americanas.com.br', 'ImageLink': 'www.americanas.com.br/img', 'Date': '15/10/2024'}
    ]

    header(data, 'etl', '1Eyh3CpweR8CxxuR5zTL_qBbxbh88MWKxlVoTPRMW9BE')
    lines(data, 'etl', '1Eyh3CpweR8CxxuR5zTL_qBbxbh88MWKxlVoTPRMW9BE')
