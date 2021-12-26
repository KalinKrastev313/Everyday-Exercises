percent = int(input())

def printing (perc):
    if perc == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        signs = perc//10
        print(perc, end = "")
        print("% [", end = "")
        print("%"*signs , end = "")
        print("."*(10 - signs), end = "")
        print("]")
        print("Still loading...")

printing(percent)