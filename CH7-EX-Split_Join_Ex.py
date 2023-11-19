# 11.18.23

# Example of split and join built in functions

path = input('Please enter file path: ')

new_separator = input('Enter new separator:\n')

tokens = path.split('\\')

newpath = new_separator.join(tokens)

print(newpath)
