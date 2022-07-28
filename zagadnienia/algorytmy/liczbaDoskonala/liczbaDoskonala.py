def doskonala(n):

    # Suma wszystkich dzielników
    suma = 0
    k = 1

    while k <= n / 2 :

        if n % k == 0:

            suma += k

        k += 1

    if suma == n:

        return n, "Jest liczba doskonala"

    return n, "Nie jest liczba doskonala"



x = int(input("Wpisz liczbe: "))

print(doskonala(x))
