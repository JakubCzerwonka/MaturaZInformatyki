def pierwsza(n):

    # Jeśli liczba jest mniejsza od 1, równa 0 lub jest innego typu niż int zwróć komunikat o wprowadzenia poprawnej liczby
    if n == 0:
        return "!!!!Liczba nie może być zerem!!!!"
    elif n < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    elif type(n) != int:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    

    # Utworzenie tablicy do której będą dodawane dzielniki liczby n oraz stworzenie zmiennej 'k', żeby ją potem wykorzystać w roli dzielnika
    nums = []
    k = 1

    # Wykonuj pętle dopóki liczba jest większa lub równa od dzielnika
    while n >= k:
        # Wykonuj pętle dopóki reszta z dzielenia liczba n przez k będzie równa 0.
        while n % k == 0:

            # Dodaje liczbę przez którą reszta dzielenia n przez k będzie równa 0 do tablicy. (Tablica zawiera dzielniki liczby n)
            nums.append(k)
            break

        k += 1      

    # Funkcja która sortuje liczby od najmniejszej do największej.
    nums.sort()

    # Jeśli liczba ma tylko dwa dzielniki (1 i samą siebie), to jest liczbą pierwszą. W przypadku liczby 1 ma ona tylko jeden dzielnik.
    if len(nums) <= 2:
        return "Liczba: ", n, "jest liczbą pierwszą"
    # Jeśli liczba ma więcej niż dwa dzielniki, to jest liczbą złożoną.
    if len(nums) > 2:
        return "Liczba: ", n, "jest liczbą złożoną"

    
x = int(input("Podaj liczbe: "))

print(pierwsza(x))
