filename = 'alice.txt'
with open(filename) as file_object:
    contents = file_object.read()
    appears = contents.lower().count('the')

print(appears)
