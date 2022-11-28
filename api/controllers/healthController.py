from fastapi import APIRouter

from api.routes.generalRoutes import HEALTH_CHECK

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {"status": "running"}
