from fastapi import APIRouter

from api.controllers import healthController, airtableController, sheetsController, homeController

router = APIRouter()
router.include_router(healthController.api_router)
router.include_router(airtableController.api_router)
router.include_router(sheetsController.api_router)
router.include_router(homeController.api_router)
