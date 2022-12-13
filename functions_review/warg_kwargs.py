# *ARGS                  

def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}'.title())


make_pizza(12,'mushrooms', 'green peppers', 'extracheese')

# **KWARGS


def build_profile(first, last, **user_info):
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
            'Leonardo', 'DaVince',location='DaVince', 
            field='math', era='renaissance') 
print(user_profile)


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', 
                            location='princeton',field='physics') 
print(user_profile)


def build_car(production, model, **car_bio):
    car = dict()
    car['producer_name'] = production
    car['model_name'] = model
    for key, value in car_bio.items():
        car[key] = value
    return car


build_car = build_car('subaru', 'outback', color='blue')
print(build_car)
