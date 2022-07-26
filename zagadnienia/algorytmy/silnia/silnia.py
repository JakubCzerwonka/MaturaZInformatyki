def silnia(n):

    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)



x = int(input("Podaj liczbe której chcesz obliczyć silnie: "))

print(silnia(x))
