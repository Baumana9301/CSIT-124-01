# 11.17.23

import random

# Word

word_list = ['hello', 'goodbye', 'enter', 'integer', 'float', 'string', 'function']

word = word_list[random.randint(0, 6)]

hidden_word = '-' * len(word)

# Guesses & Difficulty

num_guesses = 0

difficulty_setting = int(input('Please enter the difficulty setting ('
                               '1=Easy, 2=Medium, 3=Hard): '))

if difficulty_setting == 1:
    num_guesses = 10
elif difficulty_setting == 2:
    num_guesses = 6
else:
    num_guesses = 3

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input(f' Enter a character (guess #: {guess}): ')

    if len(user_input) == 1:
        num_occurences = word.count(user_input)

        position = -1
        for occurrence in range(num_occurences):
            position = word.find(user_input, position+1)
            hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]

        guess += 1

if ('-' in hidden_word) == False:
    print('Winner!', end=' ')
else:
    print('Loser!', end=' ')

print(f'The word was {word}.')

