from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user_model import UserCreate, UserResponse
from app.auth import verify_jwt  
from app.services.user_service import insert_user_service

router = APIRouter()

@router.post(
    "/user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UserCreate, jwt_payload: dict = Depends(verify_jwt)):
    try:
        created_user = insert_user_service(user.email, user.name, getattr(user, "username", None))
        return created_user
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
