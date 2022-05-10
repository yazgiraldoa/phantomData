import os
import uuid
from crontab import CronTab


class SheetsManager:

    def create_task(self, sheet_url: str, phantom_csv: str):
        """Create bash script to execute in the cron task"""
        try:
            filename = f'task_{uuid.uuid1()}.sh'
            directory = 'cron_tasks/sheets'
            if not os.path.exists(directory):
                os.makedirs(directory)
            path = f'{directory}/{filename}'
            script_path = '/root/phantomData/scripts/uploadDataToSheets.py'
            with open(path, mode='w', encoding='utf-8') as f:
                f.write('#!/bin/bash\n')
                f.write(f'SHEETS_URL={sheet_url} PHANTOM_CSV={phantom_csv} python3 {script_path}\n')

            self.schedule_task(path)
            return 'Ok'
        except Exception as e:
            return e.__str__()

    def schedule_task(self, path: str):
        """Schedule the task in crontab"""
        cron = CronTab(user=True)
        job = cron.new(command=f'/bin/bash /root/phantomData/{path}')
        job.hour.every(3)
        cron.write()
