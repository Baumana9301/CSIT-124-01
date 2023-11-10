# CSIT-124-01 - LAB 6.20 - STEP COUNTER

# Andrew Bauman

# Funcion definition

def feet_to_steps(num_feet):
    num_steps = num_feet * (1 / 2.5)
    return int(num_steps)

# User Input

feet_walked = float(input())

# Output

feet_to_steps(11)

print(feet_to_steps(feet_walked))
