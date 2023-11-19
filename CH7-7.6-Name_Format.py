# 11.18.23 - 7.6 LAB - Name format - Drew Bauman

# Prompt: Many documents use a specific format for a person's name.
# Write a program that reads a person's name in the following format:
# firstName middleName lastName (in one line)
# and outputs the person's name in the following format:
# lastName, firstInitial.middleInitial.

# User input

name = input('')

# Split to list

name_tokens = name.split()

# Output

if len(name_tokens) == 2:
    print(f'{name_tokens[1]}, {name_tokens[0][0]}.')
else:
    print(f'{name_tokens[2]}, {name_tokens[0][0]}.{name_tokens[1][0]}.')

