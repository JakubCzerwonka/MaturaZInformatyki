# Funkcja zwracająca największy wspólny dzielnik liczb x i y
def nwd(x, y):

    while y != 0:

        c = x % y
        x = y
        y = c

    return x

# Funkcja zwracająca najmniejszą wspólną wielokrotność liczb n i k
def nww(n, k):

    wynik = n * k // nwd(n, k)

    return wynik


n = int(input("Podaj liczbe n: "))
k = int(input("Podaj liczbe k: "))

print(nww(n, k))
