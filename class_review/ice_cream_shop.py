from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'Strawbarry', 'Chocolate', 'Bluebarry', 'Grape'
            ]
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f'- {flavor}')


mall_shop = IceCreamStand('The mall', 'Ice cream')
mall_shop.show_flavors()
