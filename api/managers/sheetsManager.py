import os
import uuid
import re
import subprocess
from crontab import CronTab
from fastapi import HTTPException
from fastapi.openapi.models import Response


class SheetsManager:

    def create_task(self, sheet_url: str, phantom_csv: str = None, search_url: str = None):
        """Create bash script to execute in the cron task"""

        try:
            directory = 'cron_tasks/sheets'
            if not os.path.exists(directory):
                os.makedirs(directory)
            filename = f'task_{uuid.uuid1()}.sh'
            path = f'{directory}/{filename}'

            self.validate_urls(sheet_url, phantom_csv, search_url)

            if phantom_csv:
                script_path = self.upload_data(path, sheet_url, phantom_csv)
            else:
                script_path = self.update_search(path, sheet_url, search_url)

            #subprocess.check_output(f"/bin/bash {os.getcwd()}{path}", stderr=subprocess.STDOUT, shell=True)
        except Exception as e:
            return HTTPException(detail=e.__str__(), status_code=400)
        else:
            self.schedule_task(script_path)
            return Response(content="Task scheduled successfully", status_code=200)

    @staticmethod
    def schedule_task(path: str):
        """Schedule the task in crontab"""
        cron = CronTab(user=True)
        job = cron.new(command=f'/bin/bash {path}')
        job.day.every(1)
        cron.write()

    @staticmethod
    def upload_data(path: str, sheet_url: str, phantom_csv: str):
        """Create bash script to run the task that uploads information to Sheets"""

        script_path = f"{os.getcwd()}/scripts/uploadDataToSheets.py"
        with open(path, mode='w', encoding='utf-8') as f:
            f.write('#!/bin/bash\n')
            f.write(f'SHEETS_URL="{sheet_url}" PHANTOM_CSV="{phantom_csv}" python3 {script_path}\n')

        return script_path

    @staticmethod
    def update_search(path: str, sheet_url: str, search_url: str):
        """Create bash script to run the task that updates search url for Phantom Buster"""
        script_path = f"{os.getcwd()}/scripts/updateSearchLink.py"
        with open(path, mode='w', encoding='utf-8') as f:
            f.write('#!/bin/bash\n')
            f.write(f'SHEETS_URL="{sheet_url}" SEARCH_URL="{search_url}" python3 {script_path}\n')

        return script_path

    @staticmethod
    def validate_urls(sheet_url: str, phantom_csv: str, search_url: str):
        """Function to validate URLs before scheduling the task"""
        if not sheet_url.startswith("https://docs.google.com/spreadsheets/"):
            raise ValueError("Not a Google spreadsheet link")
        if phantom_csv:
            if not re.search("phantombooster\.\S+csv", phantom_csv):
                raise ValueError("Not a Phantom Buster CSV")
        if search_url:
            if not search_url.startswith("https://www.linkedin.com/sales/search/people?query="):
                raise ValueError("Not a LinkedIn Sales Navigator search link")
