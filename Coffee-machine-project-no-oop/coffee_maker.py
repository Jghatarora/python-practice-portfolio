class CoffeeMaker():
    '''Creates a template for a money machine'''
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100
        }
    
    def resources_are_sufficient(self, selection):
        '''Check for sufficient resources before dispensing coffee'''
        for item in selection.ingredients:
            if selection.ingredients[item] > self.resources[item]:
                return False
        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]