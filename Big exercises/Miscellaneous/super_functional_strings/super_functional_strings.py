s = "aba"


def create_substrings(s):
    sub_strings = []

    for i in range(len(s)):
        for l in range(len(s), i, -1):
            if not s[i:l] in sub_strings:
                sub_strings.append(s[i:l])
    return sub_strings


def distinct(text):
    dist = []
    for char in text:
        #for really long strings containing the whole alphabet
        if len(dist) == 26:
            break
        #adding unique characters
        if not char in dist:
            dist.append(char)
    return len(dist)


def superFunctionalStrings(s):
    sub_strings = create_substrings(s)
    result = 0
    divisor = (10 ** 9 + 7)
    for text in sub_strings:
        f = (len(text) ** distinct(text)) % divisor
        result += f
    return result


print(superFunctionalStrings(s))







