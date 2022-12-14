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
            confirm = input(f'You are {username} or not? [ y / n]: ').lower()
            if confirm in 'y yes':
                print(f"Welcome back, {username}!")
            elif confirm in 'no n not':
                get_new_username()
            else:
                print(f'Please, enter Y or N')
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
