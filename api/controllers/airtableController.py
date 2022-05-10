from fastapi import APIRouter, HTTPException

from api.managers.airtableManager import AirtableManager
from api.routes.generalRoutes import UPLOAD_TO_AIRTABLE_PATH

api_router = APIRouter()
airtableManager = AirtableManager()


@api_router.post(UPLOAD_TO_AIRTABLE_PATH)
def upload_to_airtable(
        phantom_csv: str = None,
        airtable_api_key: str = None,
        airtable_base_url: str = None,
        airtable_table_name: str = None
        ):
    """Endpoint that receives the configuration of the task to schedule"""
    if phantom_csv and airtable_api_key and airtable_base_url and airtable_table_name:
        response = airtableManager.create_task(phantom_csv, airtable_api_key, airtable_base_url, airtable_table_name)
        if response == 'Ok':
            return {'status': 'Task scheduled successfully'}
        return response
    else:
        raise HTTPException(status_code=400, detail="Bad request")
