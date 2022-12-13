def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)
    

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


def show_magicians(magicians_name):
    print(magicians_name)


def make_great(great_list):
    for name in great_list:
        great_magicians.append('The great '+ name)
    print(great_magicians)


magicians_name = ['David Copperfield', 'Doug Henning', 'Penn & Teller', 'David Blaine']
great_magicians = []
make_great(magicians_name[:])
show_magicians(magicians_name)
