from lib.User import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users;")
        users = [User(row['id'], row['email'], row['username'], row['name'], row['password']) for row in rows]
        return users

    def add(self, user_object):
        self._connection.execute("INSERT INTO users (email, username, name, password) VALUES (%s, %s, %s, %s);",
                                 [user_object.email, user_object.username, user_object.name, user_object.password])

    # SIGNUP method validating if username and email are unique
    def validate_if_unique(self, user_object):
        rows = self._connection.execute("SELECT * FROM users;")
        users = [User(row['id'], row['email'], row['username'], row['name'], row['password']) for row in rows]

        for user in users:
            if user_object.email == user.email:
                return False
            elif user_object.username == user.username:
                return False
        return True

    # SUGNUP method generating error messages if username or email are not unique
    def generate_errors(self, user_object):
        rows = self._connection.execute("SELECT * FROM users;")
        users = [User(row['id'], row['email'], row['username'], row['name'], row['password']) for row in rows]
        errors = []
        for user in users:
            if user_object.email == user.email:
                errors.append("This email is already registered!")

            if user_object.username == user.username:
                errors.append("This username is taken, try another one!")

            if user_object.email == "" or user_object.email == None:
                errors.append("Please add email.")

            if user_object.name == "" or user_object.name == None:
                errors.append("Please add name.")

            if user_object.username == "" or user_object.username == None:
                errors.append("Please add username.")

            if user_object.password == "" or user_object.password == None:
                errors.append("Please add password.")
        if errors == []:
            return []
        return list(set(errors))

    # LOGIN method validating if username exists
        # returns Flase or True
    
    def username_valid(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s;",
                                        [username])
        if rows == []:
            return False
        if rows != []:
            return True

    # LOGIN method returning object by username
    # returns user object
    def search_by_username(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s;",
                                        [username])
        row = rows[0]
        user = User(row['id'], row['email'], row['username'], row['name'], row['password'])
        return user

    # LOGIN method checking is password matches user
    # returns True or Flase
    def password_valid(self, username, password):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s;",
                                        [username])
        if rows == []:
            return False
        
        row = rows[0]
        user = User(row['id'], row['email'], row['username'], row['name'], row['password'])

        if user.password == password:
            return True
        else:
            return False

    # HOMEPAGE when passing user_id the user name is returned
    def search_username_by_user_id(self, user_id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s;",
                                        [user_id])
        row = rows[0]
        return row['username']
