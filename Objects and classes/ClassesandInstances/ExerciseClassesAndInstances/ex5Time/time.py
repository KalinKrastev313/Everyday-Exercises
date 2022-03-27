from datetime import time, timedelta
import datetime

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.datetime_object = datetime(100, 1, 1, hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.datetime_object += timedelta(seconds=1)
        return Time.get_time()

time = Time(9, 30, 59)
print(time.next_second())

#Unfinished
