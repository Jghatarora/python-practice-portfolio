'''My Module Docstring'''
coins_dictionary = {'quarter': 0.25, 'dime': 0.10, 'nickle': 0.05, 'penny': 0.01}
coin_selection = {1: coins_dictionary[0], 2:coins_dictionary[1],\
                  3:coins_dictionary[2], 4:coins_dictionary[3]}
drink_menu = ('espresso', 'latte', 'cappuccino')

class CoffeeMachine():
    '''Class Docstring'''
    def __init__(self, water = 1000, milk = 500, coffee = 500, money = 0):
        super().__init__()
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def __str__(self):
        '''dummy docstring'''
        print(f'{self.water}{self.milk}{self.coffee}{self.money}')

    def process_coin(self, coin_value):
        '''dummy docstring'''
        self.money += coin_value
        print(f'${self.money}')

    def dispense_change(self):
        '''dummy docstring'''


    def off(self, word):
        '''dummy docstring'''


    def user_select(self, selection):
        '''dummy docstring'''


    def transaction_successful(self):
        '''dummy docstring'''


    def make_coffee(self):
        '''dummy docstring'''


    def menu(self):
        '''Menu Docstring'''
        print('Please make your selection\n\
            1:  {drink_menu[0]}\n\
            2:  {drink_menu[1]}\n\
            3:  {drink_menu[2]}\n')

        user_input = input()
        self.user_select(drink_menu[user_input-1])



coffee_machine = CoffeeMachine()

coffee_machine.menu()
user_selection = input('Selection')
