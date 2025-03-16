from user import User

users = [User(1, 'Egor', 'mypassword'),
         User(2, 'Jose', 'secret')]

username_table = {u.username: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user
