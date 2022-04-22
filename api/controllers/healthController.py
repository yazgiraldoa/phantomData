from fastapi import APIRouter

from api.routes.generalRoutes import HEALTH_CHECK

api_router = APIRouter()


@api_router.get(HEALTH_CHECK)
def health_check():
    return {"status": "running"}
