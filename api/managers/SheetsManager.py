import uuid

import gspread as gspread
import os


class SheetsManager:

    def create_import_task(self, sheet_url: str, phantom_csv: str):
        """Execute the script that imports the data from Phantom Buster and upload it to Google Sheets"""
        id = uuid.uuid1()
        filename = f'task_{id}.sh'

        with open(f'./cronTasks/{filename}', mode='w', encoding='utf-8') as f:
            f.write('#!/bin/bash\n')
            f.write(f'SHEETS_URL={sheet_url} PHANTOM_CSV={phantom_csv} python3 phantomBusterData.py\n')

        return filename

    def connect_sheets(self):
        credentials = {
            "type": os.getenv("TYPE"),
            "project_id": os.getenv("PROJECT_ID"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID"),
            "private_key": os.getenv("PRIVATE_KEY"),
            "client_email": os.getenv("CLIENT_EMAIL"),
            "client_id": os.getenv("CLIENT_ID"),
            "auth_uri": os.getenv("AUTH_URI"),
            "token_uri": os.getenv("TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
        }

        gc = gspread.service_account_from_dict(credentials)
        sh = gc.open_by_url(os.getenv('SHEETS_URL'))
        return sh
