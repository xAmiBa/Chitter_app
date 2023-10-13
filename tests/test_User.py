from lib.User import User

"""
When I create new user object
all values are assigned to variables
"""

def test_new_object_created():
    user = User(2, "test_email@gmail.com", "Test username", "Test name", "Test password")
    assert user.id == 2
    assert user.email == "test_email@gmail.com"
    assert user.name == "Test name"
    assert user.username == "Test username"
    assert user.password == "Test password"

def test_users_equal():
    user = User(2, "test_email@gmail.com", "Test username", "Test name", "Test password")
    user1 = User(2, "test_email@gmail.com", "Test username", "Test name", "Test password")
    assert user == user1