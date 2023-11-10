# CSIT-124-01 - LAB 6.22 - Swapping Variables

# Andrew Bauman

# Define a function named swap_values that takes four integers as parameters
#     and swaps the first with the second, and the third with the fourth values.
# Then write a main program that reads four integers from input, calls
#     function swap_values() to swap the values,
#     and prints the swapped values on a single line separated with spaces.

# Function definition

def swap_values(int1, int2, int3, int4):
    return f'{int2} {int1} {int4} {int3}'

# User Input

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# Output

print(swap_values(num1, num2, num3, num4))

    
    
        

