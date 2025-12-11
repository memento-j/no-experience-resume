#but if i stop, i'll never be good
from app.config import supabase

def get_profile(user):
    response = supabase.table("profiles").select("*").eq("id", user.id).single().execute()
    return response.data