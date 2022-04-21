from fastapi import APIRouter
from api.controllers import healthController, sheetsController

router = APIRouter()
router.include_router(healthController.api)
router.include_router(sheetsController.api)
