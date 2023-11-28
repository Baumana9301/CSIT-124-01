# 11.25.23

# class Time:
    # Class that represents time of day
    # def __init__(self):
        # self.hours = 0
        # self.minutes = 0

# my_time = Time()
# my_time.hours = 7
# my_time.minutes = 15

# print(f'{my_time.hours} hours', end=' ')
# print(f'and {my_time.minutes} minutes')

class Person:
    def __init__(self):
        self.first = ''
        self.last = ''

    def get_full_name(self):
        return f'{self.first} {self.last}'

person1 = Person()
user_first_name = input('Please input your first name: ')
user_last_name = input('Please input your last name: ')

person1.first = user_first_name
person1.last = user_last_name
print(person1.get_full_name())

