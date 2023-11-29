# 11.28.23

# This code sums evaluated x values and multiplies them by delta x

# For assistance with Riemann sums

import math

c = input('Hello! Please enter any letter to continue and "q" to quit: ')
numlist = []

while c != 'q':
    num = float(input('Please enter a number to add to the list: '))
    numlist.append(num)
    c = input('Please enter any letter to continue and "q" if you are all finished: ')

numlist_sum = sum(numlist)

print(f'Your sum is: {numlist_sum}')

delta_x = float(input('Please enter your calculation for delta x: '))

print(f'Your Riemann sum is: {(delta_x * numlist_sum):.2f}')




    
    
