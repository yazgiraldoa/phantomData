from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles


def make_app():
    from api.controllers import router
    from api.routes.generalRoutes import ROUTE_PATH

    app = FastAPI()

    app.include_router(router=router)
    app.mount("/style", StaticFiles(directory="api/web_dynamic_files/style"), name="style")
    return app


app = make_app()


def start_application():
    uvicorn.run("api:app", port=8080, loop='asyncio')
