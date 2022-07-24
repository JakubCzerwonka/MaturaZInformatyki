def dzielniki(n):

    # Jeśli liczba jest mniejsza od 1, równa 0 lub jest innego typu niż int zwróć komunikat o wprowadzenia poprawnej liczby
    if n == 0:
        return "!!!!Liczba nie może być zerem!!!!"
    elif n < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    elif type(n) != int:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"

    # Utworzenie tablicy do której będą dodawane dzielniki liczby n, oraz stworzenie zmiennej 'k', żeby ją potem wykorzystać w roli dzielnika
    nums = []
    k = 1

    # Wykonuj pętle dopóki liczba jest większa lub równa od dzielnika
    while n >= k:
        # Wykonuj pętle dopóki reszta z dzielenia liczby n przez k będzie równa 0.
        while n % k == 0:
            
            nums.append(k)
            break

        k += 1

    # Funkcja która sortuje liczby od najmniejszej do największej.
    nums.sort()

    # Zwraca tablice dzielników liczby n
    return nums
