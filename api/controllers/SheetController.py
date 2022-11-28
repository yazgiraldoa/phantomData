from fastapi import Request, APIRouter, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.managers.airtableManager import AirtableManager
from api.managers.sheetsManager import SheetsManager
from scripts import uploadDataToSheets

api_router = APIRouter()

air_table_task = AirtableManager()
sheet_task = SheetsManager()

templates = Jinja2Templates(directory="api/web_dynamic_files/forms")

"""This controller is used to connect with sheet HTML form to show the form
and direct the user to the authentication page after submission
it also contains a google authentication controller to enable access to the user
using his email"""


@api_router.get('/sheet_form', response_class=HTMLResponse)
def write_airtable(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("sheet_form.html", context)


@api_router.post("/sheet_submission")
async def handel_airtable_form(sheets_url: str = Form(...), phantom_csv: str = Form(...)):
    if sheets_url and phantom_csv:
        response = sheet_task.create_task(sheets_url, phantom_csv)
        if response == 'Ok':
            return {'status': 'Task scheduled successfully'}
        else:
            raise HTTPException(status_code=400, detail="Bad request")


@api_router.post("/google_connection")
async def start_connection_with_sheet():
    uploadDataToSheets.start_connection()
