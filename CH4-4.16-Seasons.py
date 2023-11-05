# CSIT-124-01 CH4 4.16 LAB - Seasons

# Take in date as input and output the season in the northern hemisphere.

# Input str for month, int for day.

# Input

month = input('Please input a month: ')
day = int(input('Please input a day of the month: '))

# Def

springmonths = [ 'March', 'April', 'May', 'June' ]
summermonths = [ 'July', 'August', 'September' ]
autumnmonths = [ 'October', 'November', 'December' ]
wintermonths = [ 'January', 'February', ]

# Branching & Output

if 0 < day < 32:
    if month in springmonths:
        if month == 'March':
            if 20 < day < 32:
                print('Spring')
            else:
                print('Winter')
        elif month == 'June':
            if day < 21:
                print('Spring')
            else:
                print('Summer')
        else:
            print('Spring')
    elif month in summermonths:
        if month == 'September':
            if day < 22:
                print('Summer')
            else:
                print('Autumn')
        else:
            print('Summer')
    elif month in autumnmonths:
        if month == 'December':
            if day < 21:
                print('Autumn')
            else:
                print('Winter')
        else:
            print('Autumn')
    elif month in wintermonths:
        print('Winter')
    else:
        print('Invalid')
else:
    print('Invalid')




          
