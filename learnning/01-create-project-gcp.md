https://cloud.google.com/python/docs/reference/cloudresourcemanager/0.30.5/project

https://cloud.google.com/docs/authentication?hl=pt-BR&_gl=1*nymxro*_ga*Nzc3NjcxNjI3LjE3MjU1NDQxMDA.*_ga_WH2QY8WWF5*MTczMDIyMDQyOC4xMS4xLjE3MzAyMjEyNzYuNTUuMC4w

# To allow a Python script to access a Google Sheet
you need to set up a Google Cloud project, enable the Google Sheets API, create service account credentials, and use a Python library like "gspread" to interact with your spreadsheet using the API key, essentially granting your Python application authorized access to read and write data from your Google Sheet. 

## Key steps:
- Create a Google Cloud Project: Go to the Google Cloud Console and create a new project if you don't have one already. 
- Enable the Google Sheets API: Navigate to "APIs & Services" > "Library" in your project, search for "Google Sheets API" and enable it. 
- Create Service Account Credentials:
Go to "APIs & Services" > "Credentials". 
Click "Create Credentials" and select "Service account". 
Give your service account a name, and under "Roles", select an appropriate access level (like "Editor" for full read/write access). 
Download the JSON key file which will contain your service account credentials. 
- Install gspread library:
Open your terminal and run pip install gspread 
- Code setup:
Import necessary modules:
Código

        import gspread

        from google.oauth2 import service_account
- Authorize with credentials.
Código

        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']

        creds = service_account.Credentials.from_service_account_file('your_credentials.json', scopes=scope) 

        gc = gspread.authorize(creds)
Access your Google Sheet:
Open the spreadsheet:
Código

        sh = gc.open_by_key("YOUR_SHEET_ID")  
Replace "YOUR_SHEET_ID" with the unique identifier found in your Google Sheet URL. 
Access a specific worksheet:
Código

        worksheet = sh.worksheet("Sheet1")  
"Sheet1" is the name of the sheet within your Google Sheet. 
Read and write data:
Get data from a cell:
Código

        cell_value = worksheet.cell(row=1, col=2).value  
Write data to a cell.
Código

        worksheet.update_cell(row=1, col=2, value="New data") 
Important Considerations:
Sharing your sheet:
Make sure your Google Sheet is shared with the service account email you created, giving it the necessary access level. 
Authentication flow:
If you are building a web application, you might need to implement a more complex authentication flow using OAuth2 to handle user login and authorization. 