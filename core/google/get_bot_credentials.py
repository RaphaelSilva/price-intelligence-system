# pylint: disable=W0102 dangerous-default-value
"""
This module provides functionality to obtain Google Sheets API credentials
using a service account JSON file. The credentials are used to authenticate
and authorize access to Google Sheets and Google Drive APIs.

Functions:
    credentials(scopes: list = SCOPES) -> Credentials:
        Obtains and returns Google Sheets API credentials using the specified
        scopes. Raises a FileNotFoundError if the credentials file is not found.

Constants:
    SCOPES (list): A list of OAuth 2.0 scopes for Google Sheets and Google Drive APIs.

"""
import os
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


credential_path = os.path.join(os.getcwd(), "credentials/gcp/price-intelligence-system.json")


SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

CREDS = None


def credentials(scopes=SCOPES) -> Credentials:
    if not os.path.exists(credential_path):
        raise FileNotFoundError(f"{credential_path} not found.")

    credentials = Credentials.from_service_account_file(
        credential_path,
        scopes=scopes
    )

    return credentials


def credentials_authorized(scopes=SCOPES) -> gspread.client.Client:
    """
    Obtains and returns Google Sheets API credentials. If valid credentials
    """
    global CREDS
    CREDS = CREDS if CREDS else credentials(scopes)

    if not CREDS.valid:
        CREDS.refresh(Request())

    return gspread.authorize(CREDS)
