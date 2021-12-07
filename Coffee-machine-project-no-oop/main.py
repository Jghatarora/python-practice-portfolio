from os import truncate
import time


def power_toggle(word):
    pass

def print_report():
    pass

def check_resources():
    pass

def process_coins():
    pass

def check_transaction():
    pass

def make_coffee(x):  
    print(f'making coffee {x}')
    state_machine(True)



def state_machine(state):
    while state:
        try:
            choice = int(input('Welcome, what would you like to drink?\n\
            1: Espresso\n\
            2: Latte\n\
            3: Cappuccino\n\
            4: Check resource values\n\
            5: Power Off\n'))

            if choice == 1:
                make_coffee(choice)
                print('1 2 3')

            elif choice == 4:
                print('choice is 4')
            
            elif choice == 5:
                print('choice is 5')

            else:
                raise ValueError            

        except ValueError:
            print('Not a valid selection!\n')
   
state = True 
state_machine(state)


