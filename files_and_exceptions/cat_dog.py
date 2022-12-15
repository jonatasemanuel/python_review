def show_content(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = f'Sorry, the file {filename} does not exist.'
        print(msg)
    else:
        print(f'File ({filename}): \n{contents}')


filenames = ['cats.txt', 'dogs.txt', 'joe.txt']
for filename in filenames:
    show_content(filename)