from lib.UserRepository import UserRepository
from lib.User import User


"""
When I add user object,
database is updated
"""
def test_add_user(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    repository.add(User(None, "test_email@gmail.com", "Test username", "Test name", "Test password"))
    assert repository.all() == [User(1, 'aminaba666@gmail.com', 'xAmiBa', 'Amina Ba', 'password_amina33'),
                                User(2, 'davidQQQ@gmail.com', 'Davido999', 'David', 'password_david777'),
                                User(3, 'joe_python@gmail.com', 'Crazy_Joe', 'Joe Smith', 'password_joe8!'),
                                User(4, "test_email@gmail.com", "Test username", "Test name", "Test password")]



"""
When I validate user object email and username are unique,
true or false is returned

"""
def test_validation(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    test_user = User(None, "test_email@gmail.com", "Test username", "Test name", "Test password")
    assert repository.validate_if_unique(test_user) == True

    test_user1 = User(None, "davidQQQ@gmail.com", "Test username", "Test name", "Test password")
    assert repository.validate_if_unique(test_user1) == False

    test_user2 = User(None, "test_email@gmail.com", "Crazy_Joe", "Test name", "Test password")
    assert repository.validate_if_unique(test_user2) == False



"""
If user object is not valid,
error messages are returned
"""
def test_error_messages(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    test_user = User(None, "test_email@gmail.com", "Test username", "Test name", "Test password")
    assert repository.generate_errors(test_user) == []

    test_user1 = User(None, "davidQQQ@gmail.com", "Test username", "Test name", "Test password")
    assert repository.generate_errors(test_user1) == ["This email is already registered!"]

    test_user2 = User(None, "test_email@gmail.com", "Crazy_Joe", "Test name", "Test password")
    assert repository.generate_errors(test_user2) == ["This username is taken, try another one!"]
    
    # test_user3 = User(None, "test_email@gmail.com", "", "Test name", "")
    # assert repository.generate_errors(test_user3) == ["Please add username.", "Please add password."]
    
    test_user4 = User(None, None, "Crazy_Jdoe", "Test name", "Test password")
    assert repository.generate_errors(test_user4) == ["Please add email."]

"""
When I pass username as string
true is returned if this username exist in database
false is returned if not
"""
def tests_username_valid(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)

    assert repository.username_valid("xAmiBa") == True
    assert repository.username_valid("ggdgdg") == False

"""
When I pass username as string
user object is returned
"""
def tests_search_by_username(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)

    assert repository.search_by_username("xAmiBa") == User(1, 'aminaba666@gmail.com', 'xAmiBa', 'Amina Ba', 'password_amina33')


"""
When I pass password and user as a string
and password is valid, True is returned
otherwise False
"""
def tests_password_valid(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    assert repository.password_valid("xAmiBa", "password_amina33") == True
    assert repository.password_valid("xAmiBa", "pass55") == False

"""
When i search by user_id
the user name is returned
"""
def tests_password_valid(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    assert repository.search_username_by_user_id(2) == "Davido999"
