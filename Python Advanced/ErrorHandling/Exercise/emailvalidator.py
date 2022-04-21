from customexceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError


def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain '@'")
    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 chars")

    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


email = input()

while not email == "End":
    if valid_email(email):
        print("Email is valid")
    email = input()

