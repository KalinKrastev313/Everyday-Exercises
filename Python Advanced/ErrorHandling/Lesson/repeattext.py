def repeat_text(text, count_str):
    return text*int(count_str)


text = "Hello"
count = "abc"

try:
    print(repeat_text(text, count))
except ValueError:
    print("Variable must be an integer")