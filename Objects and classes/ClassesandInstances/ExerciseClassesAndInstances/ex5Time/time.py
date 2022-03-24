class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = ""
        lst = [self.hours, self.minutes, self.seconds]
        for item in lst:
            if len(str(item)) < 2:
                result += "0" + str(item)
            else:
                result += str(item)

#Unfinnished
    