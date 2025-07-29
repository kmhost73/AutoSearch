import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

def push_to_google_sheets(data):
    try:
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not credentials_path:
            raise ValueError("Missing GOOGLE_APPLICATION_CREDENTIALS in .env")

        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
        client = gspread.authorize(creds)

        spreadsheet_id = os.getenv("GOOGLE_SHEET_ID")
        sheet = client.open_by_key(spreadsheet_id).sheet1

        # Prepare the data
        headers = list(data[0].keys())
        values = [[row.get(col, "") for col in headers] for row in data]

        # Clear the sheet and do a bulk update
        sheet.clear()
        sheet.update('A1', [headers] + values)

    except Exception as e:
        import logging
        logging.error(f"Failed to push data to Google Sheets: {e}")
        raise
