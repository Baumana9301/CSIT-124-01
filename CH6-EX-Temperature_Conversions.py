# Converts temperature from C to F

# Conversion equations
    # F = (C * (9/5)) + 32
    # C = (F - 32) * (5/9)

# Function Definition(s)

def C_to_F(tempC):              # Celcius to Fahrenheit
    F = (tempC * (9/5)) + 32
    return F

def F_to_C(tempF):              # Fahrenheit to Celcius
    C = (tempF - 32) * (5/9)
    return C

# User Interaction

inquiry = input("Hello! If you're looking to convert from Celcius to "
                "Fahrenheit please enter the key 'F', and if you're "
                "looking to convert from Fahrenheit to Celcius please "
                "enter the key 'C': ")

if inquiry == 'F':
    C_temp = float(input("We will be converting from C -> F. Please enter "
                         "the temperature to be converted in C: "))
    F_temp = C_to_F(C_temp)
    print(f"{C_temp:.02f} Celcius is equal to {F_temp:.02f} degrees Fahrenheit.")
elif inquiry == 'C':
    F_temp = float(input("We will be converting from F -> C. Please enter "
                         "the temperature to be converted in F: "))
    C_temp = F_to_C(F_temp)
    print(f"{F_temp:.02f} degrees Fahrenheit is equal to {C_temp:.02f} "
          "Celcius.")
else:
    print('Invalid entry.')





                
