# 11.29.23

class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, other):
        if not isinstance(other, Duration):
            return 'Operation not supported. Must add two Duration type instances'
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Duration(total_hours, total_minutes)
    def __str__(self):
        return f'{self.hours} hrs and {self.minutes} min'
    def __int__(self):
        return (self.hours * 60) + self.minutes

first_trip = Duration(5, 30)
second_trip = Duration(8, 40)

print(first_trip + second_trip)
print(first_trip.hours)
print(first_trip)
print(int(first_trip))
