from fastapi import APIRouter
from services.services import ChessboardService

# Create an instance of APIRouter with a specific prefix and tags
router = APIRouter(prefix = '/chess', tags=['chess'])

# Create an instance of the ChessboardService class to interact with chessboard-related logic
chessboardService = ChessboardService()

@router.post("/queen")
async def get_queen_valid_moves(request: dict):
    valid_moves = chessboardService.get_queen_valid_moves(request)
    return {"valid_moves": valid_moves}

@router.post("/knight")
async def get_knight_valid_moves(request: dict):
    valid_moves = chessboardService.get_knight_valid_moves(request)
    return {"valid_moves": valid_moves}

@router.post("/rook")
async def get_rook_valid_moves(request: dict):
    valid_moves = chessboardService.get_rook_valid_moves(request)
    return {"valid_moves": valid_moves}

@router.post("/bishop")
async def get_bishop_valid_moves(request: dict):
    valid_moves = chessboardService.get_bishop_valid_moves(request)
    return {"valid_moves": valid_moves}