from fastapi import APIRouter

from api.routes.generalRoutes import HEALTH_CHECK

api = APIRouter()


@api.get(HEALTH_CHECK)
def health_check():
    return {"status": "running"}
