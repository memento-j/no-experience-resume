from fastapi import APIRouter, Depends
from app.controllers.profile_controller import get_profile
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/")
def route_get_profile(user = Depends(get_current_user)):
    return get_profile(user)