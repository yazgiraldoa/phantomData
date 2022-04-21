from fastapi import FastAPI
import uvicorn

from controllers import router
from routes.generalRoutes import ROUTE_PATH

app = FastAPI()
app.include_router(router=router, prefix=ROUTE_PATH)


if __name__ == '__main__':
    uvicorn.run("app:app", port=8080, reload=True, loop='asyncio')
