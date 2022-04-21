from fastapi import APIRouter, HTTPException

from api.managers.SheetsManager import SheetsManager
from api.routes.generalRoutes import CREATE_TASK_PATH

api = APIRouter()
sheetsManager = SheetsManager()


@api.post(CREATE_TASK_PATH)
def create_task(sheets_url: str = None, phantom_csv: str = None):
    if sheets_url and phantom_csv:
        return {'sheets': sheets_url, 'phantom': phantom_csv}
    else:
        raise HTTPException(status_code=400, detail="Bad request")

