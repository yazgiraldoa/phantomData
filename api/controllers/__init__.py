from fastapi import APIRouter

from api.controllers import healthController,AirtableController,SheetController,SheetURLController,IndexController

router = APIRouter()
router.include_router(healthController.api_router)
router.include_router(AirtableController.api_router)
router.include_router(SheetController.api_router)
router.include_router(SheetURLController.api_router)
router.include_router(IndexController.api_router)

