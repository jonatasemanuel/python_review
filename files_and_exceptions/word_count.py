def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read() 
    except FileNotFoundError:
        msg = f'Sorry, the file {filename} does not exist.'
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {str(num_words)} words.")


filenames = ['alice.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)
