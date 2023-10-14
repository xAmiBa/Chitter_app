import os
from flask import Flask, render_template, request, redirect
from lib.database_connection import get_flask_database_connection
from lib.User import User
from lib.UserRepository import UserRepository
from lib.Peep import Peep
from lib.PeepRepository import PeepRepository

app = Flask(__name__)

# GET /
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    return render_template('index.html')

# GET /signup
@app.route('/signup', methods=['GET'])
def get_signup():
    connection = get_flask_database_connection(app)
    return render_template('signup.html')

# POST /signup
#   email: string
#   username: string
#   name: string
#   password: string
@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['email']
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    new_user = User(None, email, username, name, password)
    # user validation
    # if not unique: render error
    if repository.validate_if_unique(new_user) == False:
        errors = repository.generate_errors(new_user)    
        return render_template('signup.html', errors=errors)
    
    # if unique: add() 
    else:
        repository.add(new_user)
        message = f"Your signup was successful {new_user.username}! Now log in."
        return render_template('index.html', message=message)

# GET /login
@app.route('/login', methods=["GET"])
def get_login():
    return render_template('login.html')

# POST /login
    #   renders homepage with option to add post
@app.route('/login', methods=["POST"])
def post_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()

    input_username = request.form['username']
    input_password = request.form['password']

    errors = []

    # search if user exist user_valid() and return user by search_by_username()
    if input_password == "" or input_password == None or input_username == "" or input_username == None:
        errors.append("Fields cannot be empty!")

    if repository.username_valid(input_username) == False:
        errors.append("Username is not valid!")
    
    if repository.password_valid(input_username, input_password) == False:
        errors.append("Password is not valid!")
    
    if errors != []:
        return render_template('login.html', errors=errors)
    
    else:
        peep_repository = PeepRepository(connection)
        peeps = peep_repository.all()
        users = UserRepository(connection)
        logged = True
        return render_template(f'homepage.html', users=users, peeps=peeps, logged=logged, user=users.search_by_username(input_username))

# GET /homepage
    # everyone can acces but not post   
@app.route('/homepage', methods=['GET'])
def get_homepage():
    connection = get_flask_database_connection(app)
    users = UserRepository(connection)

    peep_repository = PeepRepository(connection)
    peeps = peep_repository.all()
    return render_template('homepage.html', peeps=peeps, users=users)
    

# POST /post
@app.route('/post', methods=['POST'])
def get_post():
    connection = get_flask_database_connection(app)
    user_id = request.form['user_id']
    content = request.form['content']
    new_peep = Peep(None, content, user_id)
    repository = PeepRepository(connection)
    repository.add(new_peep)
    peeps = repository.all()
    users = UserRepository(connection)
    logged = True
    username = users.search_username_by_user_id(user_id)
    return render_template(f'homepage.html', users=users, peeps=peeps, logged=logged, user=users.search_by_username(username))

# GET /homepage -> logout
@app.route('/logout', methods=['GET'])
def get_logout():
    message = "You just logged out. Goodbye!"
    logged = False
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))