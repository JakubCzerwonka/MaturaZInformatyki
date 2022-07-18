def pierwsza(n):

    # Po wprowadzeniu liczby typu np. float liczba konwertuje się na int
    n = int(n)

    # Jeśli liczba jest mniejsza od 1 zwróć komunikat o wprowadzenia poprawnej liczby
    if n < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"

    nums = []
    k = 2

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
    if len(nums) <= 1:
        return "Liczba: ", n, "Rodzaj: ", "Pierwsza"
    # Jeśli liczba ma więcej niż dwa dzielniki, to jest liczbą złożoną.
    if len(nums) > 1:
        return "Liczba: ", n, "Rodzaj: ", "Złożona"
