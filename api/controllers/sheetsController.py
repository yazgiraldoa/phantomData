from fastapi import Request, APIRouter, HTTPException, Form
from api.managers.airtableManager import AirtableManager
from api.managers.sheetsManager import SheetsManager
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

api_router = APIRouter()

air_table_task = AirtableManager()
sheet_task = SheetsManager()

templates = Jinja2Templates(directory="web_dynamic_files/templates")


@api_router.get('/sheet_form', response_class=HTMLResponse)
def write_sheet(request: Request):
    """Endpoint that retrieves Sheet form"""
    context = {'request': request}
    return templates.TemplateResponse("general_pages/sheet_form.html", context)


@api_router.post("/sheet_submission")
async def handle_sheet_form(request: Request):
    """Endpoint that receives the configuration of the task to schedule"""
    requestBody = await request.json()

    try:
        sheets_url = requestBody["sheets_url"]
        phantom_csv = requestBody["phantom_csv"]
    except KeyError:
        raise HTTPException(status_code=400, detail="Bad request")

    return sheet_task.create_task(sheet_url=sheets_url, phantom_csv=phantom_csv)


@api_router.get('/update_search', response_class=HTMLResponse)
def write_search_url(request: Request):
    """Endpoint that retrieves update search form"""
    context = {'request': request}
    return templates.TemplateResponse("general_pages/update_search_form.html", context)


@api_router.post("/update_search_submission", status_code=200)
async def handle_update_search_form(sheet_url: str = Form(...), search_url: str = Form(...)):
    """Endpoint that receives the configuration of the task to schedule"""
    if sheet_url and search_url:
        return sheet_task.create_task(sheet_url=sheet_url, search_url=search_url)
    else:
        raise HTTPException(status_code=400, detail="Bad request")
