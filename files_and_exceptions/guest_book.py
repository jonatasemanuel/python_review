filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    while True:
        name = str(input("What's your name (type 'q' to quit): "))
        if name == 'q':
            break
        else: 
            print(f'Hello {name}')
            file_object.write(f'\n{name}')
