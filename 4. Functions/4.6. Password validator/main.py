password1 = input()

def password_checker (password):
    digits_count = 0
    password_lenght = True
    password_char = True
    if not len(password) in range(6, 11):
        password_lenght = False
    for index in range(0, len(password)):
        if not ord(password[index]) in range(48, 58) and not ord(password[index]) in range(65, 91) and not ord(password[index]) in range(97, 123):
            password_char = False
        else:
            if ord(password[index]) in range(48, 58):
                digits_count = digits_count + 1
    if digits_count > 2 and password_lenght is True and password_char is True:
        print("Password is valid")
    else:
        if digits_count < 2:
            print("Password must have at least 2 digits")
        if password_lenght is False:
            print("Password must be between 6 and 10 characters")
        if password_char is False:
            print("Password must consist only of letters and digits")

password_checker(password1)