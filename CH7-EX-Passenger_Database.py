# 11.17.23

# Passenger Database

menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['MER', 'VEN', 'EAR', 'MAR', 'JUP', 'SAT', 'URA', 'NEP']

destination_prompt = ('Availible destinations:\n'
                      '(MER) Mercury\n'
                      '(VEN) Venus\n'
                      '(EAR) Earth\n'
                      '(MAR) Mars\n'
                      '(JUP) Jupiter\n'
                      '(SAT) Saturn\n'
                      '(URA) Uranus\n'
                      '(NEP) Neptune\n'
                      'Enter a destination:\n')

passengers = {}

print('Welcome to the Passenger Database portal.')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]
        else:
            print('Passenger not found.')
    elif user_input == 'print':
        for passenger in passengers:
            print(f'{passenger.title()} --> {passengers[passenger]}')
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()
        
