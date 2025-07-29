import os
import time
import logging
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def push_to_google_sheets(data):
    try:
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        spreadsheet_id = os.getenv("GOOGLE_SHEET_ID")

        if not credentials_path or not os.path.exists(credentials_path):
            raise FileNotFoundError("Service account credentials.json missing")

        creds = Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        headers = list(data[0].keys())
        values = [[row.get(col, "") for col in headers] for row in data]
        body = { "values": [headers] + values }

        # Clear sheet
        sheet.values().clear(
            spreadsheetId=spreadsheet_id,
            range="Sheet1"
        ).execute()

        # Push with retry logic
        for attempt in range(3):
            try:
                sheet.values().update(
                    spreadsheetId=spreadsheet_id,
                    range="Sheet1!A1",
                    valueInputOption="RAW",
                    body=body
                ).execute()
                logging.info("✅ Successfully pushed to Google Sheets.")
                break
            except Exception as e:
                logging.warning(f"Retry {attempt+1}: {e}")
                time.sleep(2 ** attempt)
        else:
            raise RuntimeError("❌ Final push to Sheets failed.")

    except Exception as e:
        logging.error(f"Fatal error in push_to_google_sheets: {e}")
        raise
