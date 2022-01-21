from fastapi import APIRouter
from tdw.nuitka_demo import hello

router = APIRouter()
router.include_router(hello.router, prefix="/hello")
