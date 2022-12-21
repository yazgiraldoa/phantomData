from fastapi import Request, APIRouter, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.managers.airtableManager import AirtableManager
from api.managers.sheetsManager import SheetsManager

api_router = APIRouter()

air_table_task = AirtableManager()
sheet_task = SheetsManager()

templates = Jinja2Templates(directory="web_dynamic_files/templates")


@api_router.get('/airtable_form/', response_class=HTMLResponse)
def write_airtable(request: Request):
    """Endpoint that retrieves Airtable form"""
    context = {'request': request}
    return templates.TemplateResponse("general_pages/airtable_form.html", context)


@api_router.post("/airtable_submission", status_code=200)
async def handle_airtable_form(phantom_csv: str = Form(...), airtable_api_key: str = Form(...),
                               airtable_base_url: str = Form(...), airtable_table_name: str = Form(...)):
    """Endpoint that receives the configuration of the task to schedule"""
    if phantom_csv and airtable_api_key and airtable_base_url and airtable_table_name:
        return air_table_task.create_task(phantom_csv, airtable_api_key, airtable_base_url,
                                          airtable_table_name)
    else:
        raise HTTPException(status_code=400, detail="Bad request")
