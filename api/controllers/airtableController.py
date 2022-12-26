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


@api_router.post("/airtable_submission", status_code=201)
async def handle_airtable_form(request: Request):
    """Endpoint that receives the configuration of the task to schedule"""
    requestBody = await request.json()
    try:
        phantom_csv = requestBody["phantom_csv"]
        airtable_api_key = requestBody["airtable_api_key"]
        airtable_base_url = requestBody["airtable_base_url"]
        airtable_table_name = requestBody["airtable_table_name"]
    except KeyError:
        raise HTTPException(status_code=400, detail="Bad request")

    response = air_table_task.create_task(phantom_csv, airtable_api_key, airtable_base_url,
                                          airtable_table_name)
    return {"status_code": 201, "detail": response}
