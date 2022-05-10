import os
import uuid
from crontab import CronTab


class AirtableManager:

    def create_task(self, phantom_csv: str, airtable_api_key: str,
                    airtable_base_url: str, airtable_table_name: str):
        """Create bash script to execute in the cron task"""
        try:
            filename = f'task_{uuid.uuid1()}.sh'
            directory = 'cron_tasks/airtable'
            if not os.path.exists(directory):
                os.makedirs(directory)
            path = f'{directory}/{filename}'
            script_path = '/root/phantomData/scripts/uploadDataToAirtable.py'
            with open(path, mode='w', encoding='utf-8') as f:
                f.write('#!/bin/bash\n')
                f.write(f'PHANTOM_CSV={phantom_csv} API_KEY={airtable_api_key} BASE_URL={airtable_base_url} '
                        f'TABLE_NAME={airtable_table_name} python3 {script_path}\n')

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
