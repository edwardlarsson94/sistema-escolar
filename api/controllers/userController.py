from api.models.userModel import get_user

def authenticate_user(username, password):
    user = get_user(username, password)
    if user:
        return True, user
    return False, None
