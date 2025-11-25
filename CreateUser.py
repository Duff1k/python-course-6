from service.AuthService import AuthService

if __name__ == "__main__":
    auth = AuthService()

    user1 = auth.create_user("Katie", "meowLove")
    user2 = auth.create_user("katusha", "Love")

