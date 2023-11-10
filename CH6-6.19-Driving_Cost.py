# CSIT-124-01 - 6.19 LAB - DRIVING COSTS - FUNCTIONS

# Andrew Bauman

# Function definition

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=0):
    cost_of_driving = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return cost_of_driving

# User Input

mpg = float(input())
price_of_gas = float(input())

# Function Output

print(f'{driving_cost(mpg, price_of_gas, 10):.02f}')

print(f'{driving_cost(mpg, price_of_gas, 50):.02f}')

print(f'{driving_cost(mpg, price_of_gas, 400):.02f}')


