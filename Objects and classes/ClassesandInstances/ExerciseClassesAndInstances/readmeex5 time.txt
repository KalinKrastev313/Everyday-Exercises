Solution of the following exercise: 

Time
Create a class called Time. Upon initialization, it should receive hours, minutes and seconds (numbers). The class should also have class attributes max_hours equal to 23, max_minutes equal to 59 and max_seconds equal to 59. You should also create 3 instance methods:
set_time(hours, minutes, seconds) - update the time with the new values
get_time() - returns "{hh}:{mm}:{ss}"
next_second() - update the time with one second (use the class attributes for validation) and return the new time (using the get_time() method)
Examples
Test Code			Output
time = Time(9, 30, 59)
print(time.next_second())	09:31:00
time = Time(10, 59, 59)
print(time.next_second())	11:00:00
time = Time(23, 59, 59)
print(time.next_second())	00:00:00




