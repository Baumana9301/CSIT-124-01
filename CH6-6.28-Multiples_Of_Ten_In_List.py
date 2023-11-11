# CSIT-124-01 - LAB 6.28 - MULTIPLES OF TEN IN A LIST

# ANDREW BAUMAN

# Function definition(s)

def is_list_mult10(my_list):
    for num in my_list:
        if num % 10 == 0:
            all_multiples = True
        else:
            all_multiples = False
    return all_multiples

def is_list_no_mult10(my_list):
    for num in my_list:
        if num % 10 == 0:
            no_multiples = False
            break
        else:
            no_multiples = True
    return no_multiples

# Main program

if __name__ == '__main__':
    list_size = int(input())
    my_list = []
    
    for i in range(list_size):
        selint = int(input())
        my_list.append(selint)
    
    result1 = is_list_mult10(my_list)
    result2 = is_list_no_mult10(my_list)
    
    if result1 == True:
        print('all multiples of 10')
    elif result2 == True:
        print('no multiples of 10')
    else:
        print('mixed values')
        
    
