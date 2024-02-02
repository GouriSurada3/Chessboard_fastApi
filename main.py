from fastapi import FastAPI
from fastapi import APIRouter
from routers import chessBoardRouter

# from services import ChessboardService

app = FastAPI()

app.include_router(chessBoardRouter.router)