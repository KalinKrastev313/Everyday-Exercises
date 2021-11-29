number_of_snowballs = int(input())
snowball_best = 0
best_quality = 0
best_snow = 0
best_time = 0

for N in range (0, number_of_snowballs, 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow//snowball_time)**snowball_quality
    if snowball_value > snowball_best:
        snowball_best = int(snowball_value)
        best_quality = int(snowball_quality)
        best_snow = int(snowball_snow)
        best_time = int(snowball_time)

print(f"{best_snow} : {best_time} = {snowball_best} ({best_quality})")