import json


filename = 'fav_number.json'
with open(filename) as file_object:
    fav_number = json.load(file_object)
    print(f'Your favorite number is {fav_number}') 