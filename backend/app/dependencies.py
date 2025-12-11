#check if the user is who they claim to be
from fastapi import Header, HTTPException
from app.config import supabase

#checks if current user is in the db
#supabase python library is synchronous
def get_current_user(authorization: str = Header(None)):
    #authorization token from request header
    if not authorization:
        raise HTTPException(401, "missing auth token")
    
    token = authorization.replace("Bearer ", "")

    try:
        response = supabase.auth.get_user(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return response.user