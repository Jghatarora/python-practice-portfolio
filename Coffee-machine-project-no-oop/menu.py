class MenuItem():
    
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'coffee': coffee,
            'milk': milk
        }


class Menu():


    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 20, 0, 1.50),
            MenuItem("latte", 200, 25, 150, 2.50 ),
            MenuItem("cappuccino", 250, 25, 50, 3.00)
        ]

    def get_items(self):
        '''This method reports back the menu choices for the user'''
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_item(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, item not found.\n")

    

