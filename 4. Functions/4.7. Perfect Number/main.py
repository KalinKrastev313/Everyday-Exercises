def perfect_check (num):
    divisors = [1]
    for divisor in range(2, num):
        if num % divisor == 0:
            divisors.append(divisor)

    if sum(divisors) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")