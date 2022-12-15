filename = 'learning_python.txt'
with open(filename) as file_object:
    files = file_object.readlines()
    py_learning = ''
    for file in files:
        py_learning += file.strip()

# print(py_learning)
print(py_learning.replace('Python', 'C'))