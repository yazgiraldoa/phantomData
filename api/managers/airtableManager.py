import os
import uuid
import re
from crontab import CronTab
from fastapi import HTTPException


class AirtableManager:

    def create_task(self, phantom_csv: str, airtable_api_key: str, airtable_base_url: str, airtable_table_name: str):
        """Create bash script to execute in the cron task"""
        try:
            self.validate_urls(phantom_csv, airtable_api_key, airtable_base_url)

            filename = f'task_{uuid.uuid1()}.sh'
            directory = 'cron_tasks/airtable'
            if not os.path.exists(directory):
                os.makedirs(directory)
            path = f'{directory}/{filename}'
            script_path = f"{os.getcwd()}/scripts/uploadDataToAirtable.py"

            with open(path, mode='w', encoding='utf-8') as f:
                f.write('#!/bin/bash\n')
                f.write(f'PHANTOM_CSV={phantom_csv} API_KEY={airtable_api_key} BASE_URL={airtable_base_url} '
                        f'TABLE_NAME={airtable_table_name} python3 {script_path}\n')

            self.schedule_task(path)
            return {"Task scheduled successfully"}
        except Exception as e:
            raise HTTPException(detail=e.__str__(), status_code=400)

    @staticmethod
    def schedule_task(path: str):
        """Schedule the task in crontab"""
        cron = CronTab(user=True)
        job = cron.new(command=f'/bin/bash {os.getcwd()}/{path}')
        job.day.every(1)
        cron.write()

    @staticmethod
    def validate_urls(phantom_csv: str, airtable_api_key: str, airtable_base_url: str):
        """Function to validate URLs before scheduling the task"""
        if not re.search("phantombooster\.\S+csv", phantom_csv):
            raise ValueError("Not a Phantom Buster CSV")
        if not airtable_api_key.startswith("key"):
            raise ValueError("Not an Airtable API Key")
        if not airtable_base_url.startswith("https://airtable.com/app"):
            raise ValueError("Not an Airtable base link")
