from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles


def make_app():
    from api.controllers import router

    app = FastAPI()

    app.include_router(router=router)
    app.mount("/style", StaticFiles(directory="web_dynamic_files/style"), name="style")
    return app


app = make_app()


def start_application():
    uvicorn.run("api:app", port=8080, loop='asyncio', debug='True')
