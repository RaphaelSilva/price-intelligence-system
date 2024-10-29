"""
This script updates Google Sheets using the gspread library and Google OAuth2 credentials.

Modules:
    gspread: A Python API for Google Sheets.
    google.oauth2.service_account: A module to handle service account credentials.

Constants:
    scopes (list): A list of scopes required for accessing Google Sheets and Google Drive.

Variables:
    credentials (Credentials): Service account credentials loaded from a JSON file.
    gc (gspread.Client): An authorized gspread client using the provided credentials.

Usage:
    Ensure that 'credentials-bot.json' file is present in the same directory as this script.
    The file should contain the service account credentials.
"""
import os
import gspread
from google.oauth2.service_account import Credentials


credentials_path = os.path.join(os.getcwd(), "credentials/gcp/price-intelligence-system.json")


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

if not os.path.exists(credentials_path):
    raise FileNotFoundError(f"{credentials_path} not found.")

credentials = Credentials.from_service_account_file(
    credentials_path,
    scopes=scopes
)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key("1dTgR_RhGPO7P35Ub5QwMP8udApas7sCRWnI_gGGEl6A")

worksheet = spreadsheet.worksheet('bipa')

for line in worksheet.get_all_records():
    print(line)
