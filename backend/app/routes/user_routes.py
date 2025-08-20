from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user_model import UserCreate, UserResponse
from app.auth import verify_jwt  
from app.services.user_service import insert_user_service, get_user_by_email, get_all_users_from_db
from fastapi import Query
from typing import List

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
    

@router.get(
    "/user",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
async def get_user(email: str = Query(..., description="Email of the user"), 
                   jwt_payload: dict = Depends(verify_jwt)):
    try:
        user = get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get(
    "/users",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK
)
async def get_all_users(jwt_payload: dict = Depends(verify_jwt)):
    try:
        users = get_all_users_from_db()
        return users
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))