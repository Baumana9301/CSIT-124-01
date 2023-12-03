# CSIT-124-01 // Project II

# Bubbakoos Ordering System

# Drew Bauman

import random

def menu(num_tacos=0, num_burritos=0, num_enchiladas=0, total=0):
    print('Menu')
    print('1. Tacos $4.99 each')
    print('2. Burritos $8.99 each')
    print('3. Enchiladas $9.99 each')
    print('s for a summary of your oder')
    print('c to complete order')
    print('q to quit\n')
    selection = str(input('Please enter # (1-3, s, c or q): '))
    global order
    order = {'tacos':num_tacos, 'burritos':num_burritos, 'enchiladas':num_enchiladas}
    if selection == 'q':
        print('Have a nice day!')
    elif selection == 'c':
        print(order)
    elif selection == 's':
        pass
    else:
        global quantity
        quantity = int(input('Enter quantity: '))
        if selection == '1':
            print(f'You ordered {quantity} tacos')
            num_tacos += quantity
            order['tacos'] += num_tacos
            menu()
        elif selection == '2':
            print(f'You ordered {quantity} burritos')
            num_burritos += quantity
            order['burritos'] += num_burritos
            menu()
        elif selection == '3':
            print(f'You ordered {quantity} enchiladas')
            num_enchiladas += quantity
            order['enchiladas'] += num_enchiladas
            menu()

print(f'Hello! Welcome to Bubbakoos Burritos!')

name = input('Please tell me your name: ')

idnum = str(random.randrange(1000))

orderid = name + idnum

# Prices

taco_price = 4.99
burrito_price = 8.99
enchiladas_price = 9.99

print(f'Your customer id is: {orderid}')

student = input('Are you an OCC student? (y/n): ')

print(f'Hi {name}, what would you like to order?')

menu()

while 
