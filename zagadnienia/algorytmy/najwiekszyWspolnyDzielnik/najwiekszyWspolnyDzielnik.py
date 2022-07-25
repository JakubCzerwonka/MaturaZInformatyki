def nwd(x, y):

    while y != 0:

        c = x % y
        x = y
        y = c

    return x
    


x = int(input("Podaj pierwszą liczbe: "))
y = int(input("Podaj pierwszą liczbe: "))

print(nwd(x, y))
