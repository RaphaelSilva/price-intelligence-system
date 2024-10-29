# pylint: disable=W0102 dangerous-default-value
"""
This module provides functionality to obtain Google Sheets API credentials.

Functions:
    credentials(scopes: list = _SCOPES) -> Credentials:
        Obtains and returns Google Sheets API credentials. If valid credentials
        are not available, it initiates an authorization flow to obtain new
        credentials and saves them for future use.

Constants:
    SCOPES (list): The scopes required for accessing Google Sheets and Google Drive APIs.    
"""
import os.path
import gspread

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

credential_path = os.path.join(os.getcwd(), "credentials/gcp/credentials.json")
token_path = os.path.join(os.getcwd(), "credentials/gcp/token.json")


# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


def credentials(scopes=SCOPES) -> Credentials:  
    """
    Obtains and returns Google Sheets API credentials. If valid credentials
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if os.path.exists(credential_path):
                flow = InstalledAppFlow.from_client_secrets_file(
                    credential_path, scopes
                )
                creds = flow.run_local_server(port=0)
            else:
                raise FileNotFoundError("credentials.json not found.")
        # Save the credentials for the next run
        with open(token_path, "w", encoding="utf-8") as token:
            token.write(creds.to_json())
    return creds


def credentials_authorized(scopes=SCOPES) -> gspread.client.Client:
    """
    Obtains and returns Google Sheets API credentials. If valid credentials
    """
    creds = credentials(scopes)

    if not creds.valid:
        creds.refresh(Request())

    return gspread.authorize(creds)
