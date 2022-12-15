import json


def get_stored_username():

    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():

        username = get_stored_username()
        if username:
            print(f"Wecome back, {username}!")
        else:
            get_new_username()
            print(f"We'll remember you when you come back, {username}")


def get_new_username():

    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        return username


greet_user()
