from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


api_router = APIRouter()


templates = Jinja2Templates(directory="api/web_dynamic_files/forms")


@api_router.get('/index/', response_class=HTMLResponse)
def write_sheetURL(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)
