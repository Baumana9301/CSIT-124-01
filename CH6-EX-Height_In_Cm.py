# Convert height in ft/in -> cm

# Conversion factors

cm_per_inch = 2.54
inch_per_foot = 12

# Function definition

def height_US_to_cm(feet, inches):
    total_inches = (feet * inch_per_foot) + inches
    inch_to_cm = total_inches * cm_per_inch
    return inch_to_cm

# User input

feet_tall = int(input("Please enter how many ft tall you "
                      "are (inches will be input after): "))

inches_rem = int(input("Please enter the remaining inches for your height: "))

# Output

cm_tall = height_US_to_cm(feet_tall, inches_rem)

print(f"You're {cm_tall}cm tall!")


                
