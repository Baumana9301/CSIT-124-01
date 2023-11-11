# CSIT-124-01 - LAB 6.29 - OUTPUT VALUES IN A LIST BELOW A USER DEFINED AMOUNT

# ANDREW BAUMAN

# Function definition(s)

def get_user_values(x=0):
    my_list = [ ]
    
    list_l = int(input())
    
    for i in range(list_l):
        intsel = int(input())
        my_list.append(intsel)

    threshold_value = int(input())

    return my_list, threshold_value

def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    new_list = [ ]
    for n in user_values:
        if n <= upper_threshold:
            new_list.append(n)
    return new_list


# Main program

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    
    for value in res_values:
        print(value)

