from playwright.sync_api import Page, expect
import pytest

def test_index_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    title_tag = page.locator('h1')
    expect(title_tag).to_have_text('Welcome to Chitter!')

    page.click('text=Signup to Chitter')
    signup_title_tag = page.locator('h1')
    expect(signup_title_tag).to_have_text('Signup to Chitter!')

def test_signup_form(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click('text=Signup')
    page.fill("input[name='email']", "test_user@gmail.com")
    page.fill("input[name='username']", "User1")
    page.fill("input[name='name']", "Test name")
    page.fill("input[name='password']", "testpassword123!")
    
    page.click("text=Sign up")

    title_element = page.locator("h3")
    expect(title_element).to_have_text("Your signup was successful User1! Now log in.")


def test_signup_form_email_error(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name='email']", "aminaba666@gmail.com")
    page.fill("input[name='username']", "User1")
    page.fill("input[name='name']", "Test name")
    page.fill("input[name='password']", "testpassword123!")
    page.click("text=Sign up")

    title_element = page.locator("li")
    expect(title_element).to_have_text("This email is already registered!")

def test_signup_form_username_error(db_connection, page, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name='email']", "test_user@gmail.com")
    page.fill("input[name='username']", "Davido999")
    page.fill("input[name='name']", "Test name")
    page.fill("input[name='password']", "testpassword123!")
    page.click("text=Sign up")

    title_element = page.locator("li")
    expect(title_element).to_have_text("This username is taken, try another one!")

def test_login_page(db_connection, test_web_address, page):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")
    title_element = page.locator('h1')
    expect(title_element).to_have_text("Login to Chitter!")


def test_username_login_fail(db_connection, test_web_address, page):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")

    page.fill("input[name='username']", "Wrong username")
    page.fill("input[name='password']", "password_amina33")

    page.click("text=Log in")

    li_tag = page.locator("li")
    expect(li_tag).to_have_text(["Username is not valid!", "Password is not valid!"])


def test_password_login_fail(db_connection, test_web_address, page):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")

    page.fill("input[name='username']", "xAmiBa")
    page.fill("input[name='password']", "wrong password")

    page.click("text=Log in")

    li_tag = page.locator("li")
    expect(li_tag).to_have_text("Password is not valid!")


def test_login_success(db_connection, test_web_address, page):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")
    page.fill("input[name='username']", "xAmiBa")
    page.fill("input[name='password']", "password_amina33")

    page.click("text=Log in")

    title_tag = page.locator("h3")
    expect(title_tag).to_have_text("See what's happening xAmiBa...")


def test_see_all_peeps_chronologicaly(db_connection, test_web_address, page):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}/home")

    peeps = page.locator(".t-peep")
    expect(peeps).to_have_text([
        'What a day, 5k run done! @xAmiBa',
        'Anyone knows good restaurants in Central London?',
        '#partytime Happy bDay to me!',
        'Boris Johnson is crazy...',
        'I learned SQL today, it was fun!'])



def test_get_new_post(db_connection, test_web_address, page):

    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")
    page.fill("input[name='username']", "xAmiBa")
    page.fill("input[name='password']", "password_amina33")

    page.click("text=Log in")

    page.fill("input[name='content']", "New test post on chitter.")
    page.click("text=Add peep")

    peeps = page.locator(".t-peep")
    expect(peeps).to_have_text(['New test post on chitter.',
                                'What a day, 5k run done! @xAmiBa',
                                'Anyone knows good restaurants in Central London?',
                                '#partytime Happy bDay to me!',
                                'Boris Johnson is crazy...',
                                'I learned SQL today, it was fun!'])

def test_if_logout_button_exist(page, db_connection, test_web_address):
    db_connection.seed('seeds/chitter.sql')
    page.goto(f"http://{test_web_address}")

    page.click("text=Login to Chitter")
    page.fill("input[name='username']", "xAmiBa")
    page.fill("input[name='password']", "password_amina33")

    page.click("text=Log in")

    page.click("text=Log out")

    title_tag = page.locator('h3')
    expect(title_tag).to_have_text('You just logged out. Goodbye!')