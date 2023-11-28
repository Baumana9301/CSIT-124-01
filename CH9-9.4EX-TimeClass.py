# 11.27.23

class Time:
    est_offset = 0
    
    def __init__(self):
        self.hours = 00
        self.minutes = 00

    def print_time(self):
        offset_hours = self.hours + self.est_offset

        print(f'Time -- {offset_hours}:{self.minutes}')

time1 = Time()
time1.hours = 10
time1.minutes = 30

time2 = Time()
time2.hours = 16
time2.minutes = 45

# EST

print('Eastern Standard Time (EST):')
time1.print_time()
time2.print_time()

# GMT

Time.est_offset = 5

print('Greenwich Mean Time (GMT):')
time1.print_time()
time2.print_time()
