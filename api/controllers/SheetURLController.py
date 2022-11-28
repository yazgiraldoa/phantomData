from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.managers.airtableManager import AirtableManager
from api.managers.sheetsManager import SheetsManager


api_router = APIRouter()

air_table_task = AirtableManager()
sheet_task = SheetsManager()

templates = Jinja2Templates(directory="api/web_dynamic_files/forms")




@api_router.get('/sheet_url', response_class=HTMLResponse)
def write_sheetURL(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("sheet_url.html", context)


@api_router.post("/sheet_url_submission")
async def handel_sheetURL_form():
    return {"status": "running"}
