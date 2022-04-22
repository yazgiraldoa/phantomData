from fastapi import FastAPI
import uvicorn


def make_app():
    from api.controllers import router
    from api.routes.generalRoutes import ROUTE_PATH

    app = FastAPI()
    app.include_router(router=router, prefix=ROUTE_PATH)
    return app


app = make_app()


def start_application():
    uvicorn.run("api:app", port=8080, loop='asyncio')
