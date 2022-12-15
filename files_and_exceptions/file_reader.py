"""file_path = '/home/joemachine/devspace/python_review/files_and_exceptions/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)"""


# Line to line
"""filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)"""


# Into a list, using the readlines() method
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
        
print(lines)

