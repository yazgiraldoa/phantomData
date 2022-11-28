from fastapi import Request, APIRouter, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.managers.airtableManager import AirtableManager
from api.managers.sheetsManager import SheetsManager

api_router = APIRouter()

air_table_task = AirtableManager()
sheet_task = SheetsManager()

templates = Jinja2Templates(directory="api/web_dynamic_files/forms")

"""This controller is used to connect with airtable HTML form to show the form
and direct the user to the authentication page after submission"""


@api_router.get('/airtable_form/', response_class=HTMLResponse)
def write_airtable(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("airtable_form.html", context)


@api_router.post("/air_table_submission")
async def handel_airtable_form(phantom_csv: str = Form(...), airtable_api_key: str = Form(...),
                               airtable_base_url: str = Form(...), airtable_table_name: str = Form(...)):
    if phantom_csv and airtable_api_key and airtable_base_url and airtable_table_name:
        # response = air_table_task.create_task(phantom_csv, airtable_api_key, airtable_base_url, airtable_table_name)
        # #print(response)
        # if response == 'Ok':
        return {"run successfully"}
        # return response
    else:
        raise HTTPException(status_code=400, detail="Bad request")
