from fastapi import FastAPI
from fastapi import APIRouter
from routers import chessBoardRouter

app = FastAPI()

app.include_router(chessBoardRouter.router)
