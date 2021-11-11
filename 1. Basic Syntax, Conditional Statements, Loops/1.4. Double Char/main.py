print("Give a string")
word = input()
a=0
for index in word:
    print(word[a]*2, end="")
    a = a+1