    auth = request.authorization
    if not auth or not auth_service.verify_password(auth.username, auth.password):
        return False
    return True