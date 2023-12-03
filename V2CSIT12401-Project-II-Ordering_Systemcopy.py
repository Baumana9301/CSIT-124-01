# CSIT-124-01 // Project II

# Bubbakoos Ordering System

# Drew Bauman

import random

def show_menu():
    print('Menu')
    print('1. Tacos $4.99 each')
    print('2. Burritos $8.99 each')
    print('3. Enchiladas $9.99 each')
    print('s for a summary of your order')
    print('c to complete order')
    print('q to quit\n')

def subtotal(x, y, z):
    return x - y - z

def show_summary(x):
    amount = []
    print('Your order is: ')
    for i, q in x.items():
        if i == 'tacos':
            print(f' {q}  {i} = ${(q * taco_price):.2f}')
            amount.append(q * taco_price)
        if i == 'burritos':
            print(f' {q}  {i} = ${(q * burrito_price):.2f}')
            amount.append(q * burrito_price)
        if i == 'enchiladas':
            print(f' {q}  {i} = ${(q * enchiladas_price):.2f}')
            amount.append(q * enchiladas_price)
    print(f"{'Amount':<20s} \t ${sum(amount):7.2f}")
    if sum(amount) >= 30.0:
        hero_discount = (sum(amount) // 30) * 5
        print(f"{'Hero Discount':<20s} \t ${hero_discount:7.2f}")
    else:
        hero_discount = 0
    if student == 'y':
        student_discount = (sum(amount) - hero_discount)  * 0.05
        print(f"{'Student Discount':<20s} \t ${student_discount:7.2f}")
    else:
        student_discount = 0
    order_subtotal = subtotal(sum(amount), hero_discount, student_discount)
    print(f"{'Subtotal':<20s} \t ${order_subtotal:7.2f}")
    tax_amount = order_subtotal * 0.06625
    print(f"{'Tax':<20s} \t ${tax_amount:7.2f}")
    global total_w_tax
    total_w_tax = tax_amount + order_subtotal
    print(f"{'Order With Tax':<20s} \t ${total_w_tax:7.2f}")

print(f'Hello! Welcome to Bubbakoos Burritos!')

name = input('Please tell me your name: ')

idnum = str(random.randrange(1000))

orderid = name + idnum

# Prices

taco_price = 4.99
burrito_price = 8.99
enchiladas_price = 9.99

order = {'tacos':0, 'burritos':0, 'enchiladas':0}

hero_discount = 0

c_total = 0

print(f'Your customer id is: {orderid}')

student = input('Are you an OCC student? (y/n): ')

print(f'Hi {name}, what would you like to order?')

show_menu()

selection = str(input('Please enter # (1-3, s, c or q): '))

while selection != 'q':
    if selection == '1':
        quantity = int(input('Enter quantity: '))
        order['tacos'] += quantity
        if quantity > 1:
            print(f'You ordered {quantity} tacos')
        else:
            print(f'You ordered {quantity} taco')
        show_menu()
        selection = str(input('Please enter # (1-3, s, c or q): '))
    elif selection == '2':
        quantity = int(input('Enter quantity: '))
        order['burritos'] += quantity
        if quantity > 1:
            print(f'You ordered {quantity} burritos')
        else:
            print(f'You ordered {quantity} burrito')
        show_menu()
        selection = str(input('Please enter # (1-3, s, c or q): '))
    elif selection == '3':
        quantity = int(input('Enter quantity: '))
        order['enchiladas'] += quantity
        if quantity > 1:
            print(f'You ordered {quantity} enchiladas')
        else:
            print(f'You ordered {quantity} enchilada')
        show_menu()
        selection = str(input('Please enter # (1-3, s, c or q): '))
    elif selection == 's':
        show_summary(order)
        show_menu()
        selection = str(input('Please enter # (1-3, s, c or q): '))
    elif selection == 'c':
        show_summary(order)
        points = int(total_w_tax // 10)
        print(f'Points earned: {points}')
        print('Thank you')
        break
    else:
        print('Invalid choice please try again!')
        show_menu()
        selection = str(input('Please enter # (1-3, s, c or q): '))

print(f'Have a nice day {name}!')
    
