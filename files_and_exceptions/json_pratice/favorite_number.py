import json


def new_fav_number():
    filename = 'fav_number.json'
    with open(filename, 'w') as file_object:
        fav_number = input('What is yout favorite number? ')
        json.dump(fav_number, file_object)

def favorite_number():
    try:
        filename = 'fav_number.json'
        with open(filename) as file_object:
            fav_number = json.load(file_object)
            if fav_number:
                print(f'Your favorite number is {fav_number}')
    except:
        new_fav_number()


favorite_number()
new_fav_number()
favorite_number()


