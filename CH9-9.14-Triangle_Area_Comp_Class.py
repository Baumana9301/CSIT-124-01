# 11.29.23 - LAB 9.14 - Triangle Area Comparison (Classes)

# Andrew Bauman

# Class

class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0
        
    def set_base(self, base):
        self.base = base
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        area = .5 * (self.base * self.height)
        return area
    
    def print_data(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

# Instantiation

triangle1 = Triangle()
triangle2 = Triangle()

# User input & Assignment

base1 = float(input('Please enter the base for triangle 1: '))
triangle1.set_base(base1)
height1 = float(input('Please enter the height for triangle 1: '))
triangle1.set_height(height1)
area1 = triangle1.get_area()

base2 = float(input('Please enter the base for triangle 2: '))
triangle2.set_base(base2)
height2 = float(input('Please enter the height for triangle 2: '))
triangle2.set_height(height2)
area2 = triangle2.get_area()

# Output

print(f'Triangle with smaller area: ')

if area1 > area2:
    triangle2.print_data()
else:
    triangle1.print_data()



