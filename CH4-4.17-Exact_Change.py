# CSIT-124-01 LAB 4.17 - Exact Change

# Take total change amount as int, output using fewest coins.
# One coin type per line.
# Coin type: Dollars, Quarters, Dimes, Nickels, Pennies
# Use singular and plural coin names as appropriate

# Input

tchange = int(input('Please input the total amount of change: ')) # Total Change

# Branching and Output

if tchange == 0:
    print('No change')
elif (tchange % 100) == 0:
    if tchange == 100:
        print(f'{(tchange / 100):.0f} Dollar')
    else:
        print(f'{(tchange / 100):.0f} Dollars')
