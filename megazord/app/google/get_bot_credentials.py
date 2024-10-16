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
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'credentials-bot.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key("11RRrpwKYwYOx8B8TrsTlCWmhDwU6fyE3uRpwZFvgm0M")

worksheet = spreadsheet.get_worksheet_by_id('Feed')

for line in worksheet.get_all_records():
    print(line)
