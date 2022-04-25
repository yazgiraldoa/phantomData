from fastapi import APIRouter, HTTPException

from api.managers.SheetsManager import SheetsManager
from api.routes.generalRoutes import CREATE_TASK_PATH

api_router = APIRouter()
sheetsManager = SheetsManager()


@api_router.post(CREATE_TASK_PATH)
def create_task(sheets_url: str = None, phantom_csv: str = None):
    """Endpoint that receives the configuration of the task to schedule"""
    if sheets_url and phantom_csv:
        response = sheetsManager.create_import_task(sheets_url, phantom_csv)
        if response == 'Ok':
            return {'status': 'Task scheduled successfully'}
        return response
    else:
        raise HTTPException(status_code=400, detail="Bad request")
