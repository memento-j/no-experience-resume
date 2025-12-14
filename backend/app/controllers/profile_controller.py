#but if i stop, i'll never be good
from app.config import supabase
from schemas.profile_update_schema import ProfileUpdate

def get_profile(user):
    response = supabase.table("profiles").select("*").eq("id", user.id).single().execute()
    return response.data

def update_profile(profile_data: ProfileUpdate, user):
    update_data = profile_data.model_dump(exclude_none=True)

    response = (
        supabase.table("profilees")
        .update(update_data)
        .eq("id", user.id)
        .execute()
    )
    
    return response.data